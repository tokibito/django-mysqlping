from django.db import connections
from django.db.backends.mysql.base import DatabaseWrapper


class MySQLPingMiddleware:
    """Ping to MySQL, reconnect if client is disconnected.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        for db_name in connections:
            connection = connections[db_name]
            if isinstance(connection, DatabaseWrapper):
                if connection.connection:
                    # Use ping method (PyMySQL or mysqlclient)
                    connection.connection.ping(True)
        response = self.get_response(request)
        return response
