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
