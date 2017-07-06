inp = [
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]


class Sudoku(object):
    def __init__(self, lst):
        self._data = lst
        self._size = len(lst[0])

    def check_columns(self):
        inverted_matrix = list(zip(*self._data))
        for i in range(self._size-1):
            if len(set(inverted_matrix[i])) != self._size:
                return False
        return True

    def check_rows(self):
        for i in range(self._size-1):
            if len(set(self._data[i])) != self._size:
                return False
        return True

    def is_valid(self):
        if self.check_columns() and self.check_rows() and self._size != 1:
            return True
        else:
            return False

sudo = Sudoku(inp)
print sudo.is_valid()
