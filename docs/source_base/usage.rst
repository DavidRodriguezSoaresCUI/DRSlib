Usage
=====

Installation and Update
-----------------------

To use DRSlib, first install/update it using pip:

.. code-block:: console
    
    $ pip install -U --pre DRSlib-DavidRodriguezSoaresCUI

The ``--pre`` switch may not be needed when stable releases **DRSlib** are made available.


Usage in your Python scripts
----------------------------

Let's say you want to use the handy ``DRSlib.decorators.timer()`` decorator
to know the execution time of your ``foo()`` function.

Here's how you may implement it::

    import DRSlib 

    ...

    @DRSlib.decorators.timer()
    def foo():
        ''' My great and powerful but slow function '''
        ...

Now every call to ``foo`` will print execution time to stdout !


Another example: You want to ask the user for their age, and decide to use
the convenient ``DRSlib.cli_ui.user_input()``.

You should have a look at documentation for more information on parameter.

Here's how you may implement it::

    from DRSlib.cli_ui import user_input

    ...

    user_age = user_input(
        prompt="Please enter your age",
        accepted=list(range(100)), # accepts ages 1-99
    )
    print(f"Your age is {user_age} !")

These example also illustrates the different ways to import element from DRSlib submodules.


Read the docs !
---------------

Documentation for all of DRSlib's contents is present in their docstring. You may
read them from this automatically generated documentation, the source code or the python interpreter::

    import DRSlib 
    help(DRSlib)
    # Displays DRSlib's docstring and submodule list 
    help(DRSlib.cli_ui)
    # Displays DRSlib.cli_ui's docstring, and docstring (plus some extras) for each element in it
    help(DRSlib.cli_ui.pause)
    # Displays DRSlib.cli_ui.pause's docstring
