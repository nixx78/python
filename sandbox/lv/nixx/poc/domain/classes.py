class Person:
    def __init__(self, pers_id: int, name: str, surname: str):
        self.txnId = pers_id
        self.name = name
        self.surname = surname

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
