# TODO:
# Query for latest entry
# fix writing
# test schema

# SCHEMA:
# PARTITION KEY = date
# ROW KEY = an int that increases by 1
# stock is an attribute
# pos, neu, neg are attributes

from azure.storage.table import TableService, Entity
import datetime


class TableAccess():
    def __init__(self, account, azurekey):
        self.account = account
        self.azurekey = azurekey
        self.table_service = TableService(account_name=account, account_key=azurekey)

    def create_table(self, table_name):
        self.table_service.create_table(table_name)

    def write_to_table(self, stock, pos, neu, neg):
        now = datetime.datetime.now()
        task = Entity()
        task.PartitionKey = now.month + "-" + now.date + "-" + now.year
        #task.RowKey = self.get_latest_entry(table_name)
        task.pos = pos
        task.neu = neu
        task.neg = neg
        task.stock = stock
        self.table_service.insert_entity(table_name, task)

    def query_table(self, table_name):
        pass

    def delete_entity(self, table_name):
        pass

    def get_latest_entry(self, table_name):
        #return id of latest entry for rowkey
        pass
