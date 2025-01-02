# Imports:

# Code:
class DBManager:
    """
    Database connection manager.

    It is responsible for managing connections efficiently. It is capable of managing multiple connections at the same time to different databases.
    """
    # Internal methods:
    def __init__(self) -> None:
        """
        Initializes an instance of a database manager.
        """
        self.connections = {}

    # Privates methods:
    def _add_connection(self, name: str, connection) -> None:
        """
        Add a new connection to a database in the manager.

        Args:
            - name (str): The name of the connection.
            - connection: Instance of the connection.
        """
        self.connections[name] = connection

    # Publics methods:
    def create_connection(self, name: str, driver: str) -> bool:
        """
        Create a new connection to a database.

        Args:
            - name (str): The name of the connection.
            - driver (str): The drive to used in the connection.

        Returns:
            - bool: True if connection created successfully, False otherwise.
        """
        pass

    def get_connetion(self, name: str) -> object | None:
        """
        Obtain an instance of the connection.

        Args:
            - name (str): The name of the connection.

        Returns:
            - object | None: The instance of the connection if exists, else None.
        """
        return self.connections.get(name, None)

db_manager = DBManager()