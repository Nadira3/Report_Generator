#!/usr/bin/python3
"""
    find_module module
"""

import pkgutil
import importlib
import inspect


def classFind(package_name='models'):
    """
        finds all the classes/modules in a
        parent module
    """

    # Import the package
    package = importlib.import_module(package_name)
    class_list = []

    # Use pkgutil to walk through the modules
    for importer, modname, ispkg in \
            pkgutil.walk_packages(
                    path=package.__path__, prefix=package.__name__ + '.'):
        # Import the module
        module = importlib.import_module(modname)

        # Get all classes defined in the module
        classes = inspect.getmembers(module, inspect.isclass)

        # Add the existing class to a class list
        clist = [class_name for class_name, class_objects in classes]
        class_list.extend(clist)

    return class_list
