class Person:
    def __init__(self, persId, name, surname):
        self.txnId = persId
        self.name = name
        self.surname = surname

    def __str__(self):
        return str(self.__dict__)
