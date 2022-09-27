import os
from typing import List
import dataset
from dataset import Table
from abc import ABCMeta, abstractmethod

# get env
username = os.environ.get("MARIADB_USERNAME", "user")
password = os.environ.get("DB_PASSWORD", "password")
hostname = os.environ.get("MARIADB_HOSTNAME", "localhost")
database = os.environ.get("MARIADB_DATABASE", "flipflap")


# connect to database
db = dataset.connect(
    f"mysql://{username}:{password}@{hostname}/{database}?charset=utf8mb4")

print('db connected')


class DB(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, table_name):
        self.table: Table = db[table_name]  # type: ignore

    def insert(self, data: dict):
        self.table.insert(data)

    def insert_many(self, data: List[dict]):
        self.table.insert_many(data)

    def update(self, data: dict, keys: List[str]):
        self.table.update(data, keys)

    def delete(self, keys: dict):
        self.table.delete(**keys)

    def find_one(self, keys: dict):
        return self.table.find_one(**keys)

    def find_query(self, keys: dict):
        return self.table.find(**keys)

    def find_all(self):
        return self.table.find()

    def query(self, query: str, *args, **kwargs):
        return db.query(query, *args, **kwargs)

    def insert_ignore(self, row: dict, keys: list, ensure=None, types=None):
        return self.table.insert_ignore(row, keys, ensure=None, types=None)
