class Person:

    def __init__(self, pers_id: int, name: str, surname: str):
        self.txnId = pers_id
        self.name = name
        self.surname = surname

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __lt__(self, other):
        return self.txnId < other.txnId

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.txnId == other.txnId
        return False

    def __hash__(self):
        return hash(self.txnId)
