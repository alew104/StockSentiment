# TODO:
# DEFINE DATA SCHEMA
# FINISH THIS WRAPPER module

from azure.storage.table import TableService, Entity

class TableAccess():
    def __init__(self, account, azurekey):
        self.account = account
        self.azurekey = azurekey
        self.table_service = TableService(account_name=account, account_key=azurekey)

    def create_table(self, table_name):
        self.table_service.create_table(table_name)

    def write_to_table(self, table_name, stock, rowkey, date, sentiment):
        task = Entity()
        task.PartitionKey = stock
        task.RowKey = rowkey
        task.date = date
        task.sentiment = sentiment
        self.table_service.insert_entity(table_name, task)

    def query_table(self, table_name):
        pass

    def delete_entity(self, table_name):
        pass
