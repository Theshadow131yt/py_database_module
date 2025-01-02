# Imports:
from .main import DBManager
import src

# Metadata:
__author__ = "TheShadow131YT"
__version__ = "0.0.0"
__dependencies__ = []

# Code:
db_manager = DBManager()

__all__ = [db_manager]
__all__.extend(src.__all__)