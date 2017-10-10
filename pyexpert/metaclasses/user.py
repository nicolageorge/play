from library import Base

# assert hasattr(Base, 'foo'), 'you broke it fool!'

class Derived(Base):
    def bar(self):
        return 'bar'
