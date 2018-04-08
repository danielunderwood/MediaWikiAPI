import sys

if not (sys.argv[0] in ['pip', 'setup.py']
        or (len(sys.argv) > 1 and sys.argv[1] in ['setup.py', 'egg_info'])
        or any([arg.startswith('import setuptools') for arg in sys.argv])):
    from .config import *
    from .mediawikiapi import *
    from .exceptions import *
    from .language import *

__version__ = "1.1.3"
