class BaseService:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def process(self, param: str):
        raise NotImplementedError


class PersonService(BaseService):

    def get_name(self):
        return '(' + BaseService.get_name(self) + ':child)'

    def process(self, param: str):
        return self.get_name() + ':' + param + ':' + 's'


service = PersonService('service')
print(service.process('param'))
