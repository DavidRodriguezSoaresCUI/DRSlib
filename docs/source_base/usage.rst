Usage
=====

Installation and Update
-----------------------

To use DRSlib, first install/update it using pip:

.. code-block:: console
    
    $ pip install -U --pre DRSlib-DavidRodriguezSoaresCUI

The ``--pre`` switch may not be needed when stable releases **DRSlib** are made available.


Dependencies
------------

**DRSlib** was built to not have many dependency outside of standard library, 
but function ``DRSlib.path_tools.windows_list_logical_drives`` has an 
*optional* dependency (``win32api``) you can install in one of these ways:

- .. code-block:: console
    
    $ pip install -r requirements-windows.txt

- .. code-block:: console
    
    $ pip install pywin32

Note: there is a required package (``send2trash``) that should have been installed 
with ``DRSlib``. If not :

.. code-block:: console
    
    $ pip install send2trash

**Building documentation** requires installing packages ``sphinx`` and ``furo`` you can install in one of these ways:

- .. code-block:: console
    
    $ pip install -r requirements-documentation.txt

- .. code-block:: console
    
    $ pip install sphinx furo



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


Building documentation
----------------------

Should be as simple as going to directory ``docs`` and running the ``sphinx-full-rebuild``
that correspond to your OS (if you are on Windows/Linux). Note: see **Dependencies** for 
how to install required modules to build documentation.