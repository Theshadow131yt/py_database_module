# Imports:
from .main import DBManager, db_manager
import src

# Metadata:
__author__ = "TheShadow131YT"
__version__ = "0.0.0"
__dependencies__ = []

# Code:
__all__ = ["DBManager", "db_manager"]
__all__.extend(src.__all__)