# Imports:
from abc import ABC, abstractmethod

# Code:
class DBConnection:
    """
    Abstract base class for all database connections.

    Classes that inherit from this class must implement the methods required to make the connection,
    close the connection, and perform queries specific to the type of database they are supporting.
    """
    # Internal methods:
    def __init__(self, name: str, driver: str) -> None:
        """
        Initializes an instance of a database connection.

        Args:
            - name (str): The name of the connection.
            - driver (str): The drive to used in the connection.
        """
        pass

    # Privates methods:
    @abstractmethod
    def _connect(self) -> bool:
        """
        Abstract methods to connect to a database.

        Returns:
            - True if connection is connected successfully, False otherwise.
        """
        raise NotImplementedError("The children class is not implemented the method '_connect'.")
    
    @abstractmethod
    def _disconnect(self) -> bool:
        """
        Abstract methods to disconnect to a database.

        Returns:
            - True if connection is disconnected successfully, False otherwise.
        """
        raise NotImplementedError("The children class is not implemented the method '_disconnect'.")

    # Publics methods:
    @abstractmethod
    def query(self, query: str) -> any:
        """
        Abstract methods to execute a query in the database.

        Args:
            - query (str): The query to execute in the database.
        """
        raise NotImplementedError("The children class is not implemented the method 'query'.")