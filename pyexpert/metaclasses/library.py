class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print 'cls', cls
        print 'name', name
        print 'bases', bases
        print 'body', body

        if not 'bar' in body:
            raise TypeError('Bad user class')
        # print 'BaseMeta.__new__', cls, name, bases, body
        return super(BaseMeta, cls).__new__(cls, name, bases, body)


class Base:
    __metaclass__ = BaseMeta
    def foo(self):
        return self.bar()
