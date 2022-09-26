from typing import List
import dataset
from dataset import Table
from abc import ABCMeta, abstractmethod

db = dataset.connect()
print('db connected')


class DB(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, table_name):
        self.table: Table = db[table_name]  # type: ignore

    def insert(self, data: dict):
        self.table.insert(data)

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

    def insert_ignore(self, row: dict, keys: dict, ensure=None, types=None):
        return self.table.insert_ignore(row, keys, ensure=None, types=None)
