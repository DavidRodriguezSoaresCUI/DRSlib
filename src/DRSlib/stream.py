"""
Stream toolbox
==============

Brings Java's Stream syntax to Python for readable functional code use
"""
from dataclasses import dataclass
from itertools import chain
from typing import Callable, Collection, Iterable, Any, TypeVar


T = TypeVar("T")
Predicate = Callable[[Any], bool]
IDENTITY = lambda x: x

# Basic accumulators


def list_accumulator(l: list, x: Any) -> list:
    """Accumulator for type list"""
    l.append(x)
    return l


def set_accumulator(s: set, x: Any) -> set:
    """Accumulator for type set"""
    s.add(x)
    return s


ACCUMULATORS: dict[T, Callable[[T, Any], T]] = {
    list: list_accumulator,
    set: set_accumulator,
    tuple: lambda t, x: t + (x,),
}

COMBINERS: dict[T, Callable[[T, T], T]] = {
    list: lambda a, b: a + b,
    set: lambda a, b: a.union(b),
    tuple: lambda a, b: a + b,
}


@dataclass
class Collector:
    """Describes a component that accepts items and stores them in a collection"""

    supplier: Callable[[], Collection]
    """Supplies a mutable collection to put items in"""
    accumulator: Callable[[Collection, Any], None]
    """Adds item in collection"""
    # combiner: Callable
    # """Combine two collections into one"""
    finisher: Callable[[Collection], Collection]
    """Applies mapping to collection after adding is done"""

    def collect(self, items: Iterable) -> Collection:
        """Perform collecting"""
        res = self.supplier()
        for item in items:
            res = self.accumulator(res, item)
        return self.finisher(res)

    # static methods

    @staticmethod
    def to_list() -> "Collector":
        """Returns a collector that stores items in a list"""
        return Collector(
            supplier=list, accumulator=ACCUMULATORS[list], finisher=IDENTITY
        )


class Stream:
    """Holds elements during processing"""

    input: Iterable
    """Contains elements to stream"""

    def __init__(self, of: Iterable) -> None:
        self.input = of

    # static methods
    @staticmethod
    def concat(a: "Stream", b: "Stream") -> "Stream":
        """Creates a new stream that contains all elements from the first stream and
        all the elements of the second stream"""
        return Stream(chain(a.input, b.input))

    # terminal methods

    def all_match(self, predicate: Predicate) -> bool:
        """Returns whether all elements of this stream match the provided predicate."""
        return all(predicate(x) for x in self.input)

    def any_match(self, predicate: Predicate) -> bool:
        """Returns whether all elements of this stream match the provided predicate."""
        return any(predicate(x) for x in self.input)

    def none_match(self, predicate: Predicate) -> bool:
        """Returns whether all elements of this stream match the provided predicate."""
        return not self.any_match(predicate)

    def collect(self, collector: Collector) -> Collection:
        """Use collector to store items into a collection"""
        return collector.collect(self.input)

    def count(self) -> int:
        """Count items in stream"""
        return len(self.input)

    # non-terminal methods

    def filter(self, predicate: Predicate) -> "Stream":
        """Filter out any element that don't match the predicate"""
        res, accumulator = self.__get_collection_and_accumulator()
        for item in self.input:
            if predicate(item):
                res = accumulator(res, item)
        self.input = res
        return self

    def map(self, mapper: Callable) -> "Stream":
        """Filter out any element that don't match the predicate"""
        res, accumulator = self.__get_collection_and_accumulator()
        for item in self.input:
            res = accumulator(res, mapper(item))
        self.input = res
        return self

    def limit(self, max_size: int) -> "Stream":
        """Returns a stream consisting of the elements of this stream,
        truncated to be no longer than max_size in length."""
        if self.count() > max_size:
            res, accumulator = self.__get_collection_and_accumulator()
            for idx, item in enumerate(self.input):
                if idx >= max_size:
                    break
                res = accumulator(res, item)
            self.input = res
        return self

    def skip(self, n: int) -> "Stream":
        """Returns a stream consisting of the elements of this stream,
        truncated to not include the first n elements."""
        if self.count() <= n:
            self.input, _ = self.__get_collection_and_accumulator()
        else:
            res, accumulator = self.__get_collection_and_accumulator()
            for idx, item in enumerate(self.input):
                if idx < n:
                    continue
                res = accumulator(res, item)
            self.input = res
        return self

    # reserved methods

    def __get_collection_and_accumulator(self) -> tuple:
        """Returns empty collection and accumulator"""
        collection_type = type(self.input)
        return collection_type(), ACCUMULATORS[collection_type]


if __name__ == "__main__":
    assert Stream((1, 2, 3)).any_match(lambda x: x % 2 == 0) is True
    assert Stream((1, 2, 3)).all_match(lambda x: x % 2 == 0) is False
    assert Stream.concat(Stream([1, 2, 3]), Stream(["a", "b", "c"])).collect(
        Collector.to_list()
    ) == [1, 2, 3, "a", "b", "c"]
    assert (
        Stream((1, 2, 3)).limit(2).count() == 2
    ), f"count={Stream((1, 2, 3)).limit(2).count()}, res={Stream((1, 2, 3)).limit(2).collect(Collector.to_list())}"
    assert Stream((1, 2, 3)).limit(2).collect(Collector.to_list()) == [1, 2]
    assert Stream((1, 2, 3)).limit(3).count() == 3
    assert Stream((1, 2, 3)).skip(1).count() == 2
    assert Stream((1, 2, 3)).skip(1).collect(Collector.to_list()) == [2, 3]
    assert Stream((1, 2, 3)).skip(3).count() == 0
