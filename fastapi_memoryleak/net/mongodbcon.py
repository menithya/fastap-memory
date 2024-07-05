
from pymongo import MongoClient
class MongoDBConns:
    """All connections and data exchange from mongodb"""

    def __init__(
        self, mongodb_uri: str = "", mongodb_db: str = ""
    ):
        self.client = MongoClient(mongodb_uri)
        self.db = self.client[mongodb_db]