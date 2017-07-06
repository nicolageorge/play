# x = iter([1, 2, 3, 4])
# print x
# print x.next()
# print x.next()

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n


    def __iter__(self):
        return self


    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


    # def prev(self):
    #     if self.i > self.n:
    #         i = self.i
    #         self.i -= 1
    #         return i
    #     else:
    #         raise StopIteration()

x = yrange(6)
# print x.next()
# print x.next()
# print x.next()
# # print x.prev()
# # print x.prev()



def some_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

f = some_range(4)

print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
