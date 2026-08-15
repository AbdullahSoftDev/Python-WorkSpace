# Directory structure:
# my_package/
#     __init__.py
#     module1.py
#     module2.py
#     subpackage/
#         __init__.py
#         module3.py

# In __init__.py:
__all__ = ['module1', 'module2']

# Import from package
import my_package.module1

from my_package import module2

from my_package.subpackage import module3

# Package initialization
# __init__.py can contain:
__version__ = "1.0.0"
__author__ = "Your Name"