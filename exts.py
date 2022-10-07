from jinja2 import nodes
from jinja2.ext import Extension

class AllLower(Extension):

    tags = {'allLower'}

    def __init__(self, environment):
        super(AllLower, self).__init__(environment)

        def all_lower(value: str):
            print('value', value)
            return str(value).lower()
        
        environment.filters['allLower'] = all_lower

    def parse(self, parser):

        print('self', self)
        print('parser', parser)
        

        return super().parse(parser)
