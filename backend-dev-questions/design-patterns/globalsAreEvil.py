# Bad
HOST = 'localhost'

class Report:
    def __init__(self, text):
        self.text = text

# Bad
class Database:
    def __init__(self):
        self.HOST = HOST

    def get_host(self):
        return self.HOST


# Good
class DatabaseNoGlobal:
    def __init__(self, HOST):
        self.HOST = HOST

    def get_host(self):
        return self.HOST


if __name__ == '__main__':
    database = Database()
    # Where is host coming from?
    print(database.get_host())

    HOST = 'localhost'
    PORT = '5432'
    database = Database(HOST)
