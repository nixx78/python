# Python 2.x
# class OldBaseService(object):
#     name = 'name'


class BaseService:

    # Class attribute
    service = 'BaseService'

    # Constructor
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def process(self, param: str):
        raise NotImplementedError


class PersonService(BaseService):

    def __init__(self, name: str):
        BaseService.__init__(self, name + 'chld')

    def get_name(self):
        return '(' + BaseService.get_name(self) + ':child)'

    def process(self, param: str):
        return self.get_name() + ':' + param + ':' + 's'


# ==============================
baseService = BaseService('baseService')

service = PersonService('service')

print('Type: [{0}] service.process: [{1}]'.format(type(service), service.process('param')))
print('name:', service.name)
print(BaseService.service)

print('Is instance of BaseSevice:', isinstance(service, BaseService))
print('Is instance of PersonService:', isinstance(service, PersonService))

