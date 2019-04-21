import random

class MinHeap:
    def __init__(self):
        self.heap = []

    def build_min_heap(self, heap):
        print('build_min_heap {}'.format(', '.join([str(n) for n in heap])))
        l = int(len(heap)/2)
        for i in range(l+1, -1, -1):
            heap = min_heapify(heap, i)

        return heap

    def min_heapify_down(self, heap, i):
        if(i==0):
            left = 1
            right = 2
        else:
            left = 2 * i + 1
            right = 2 * i
        smallest = i
        
        # print('{} max heapify, left: {}, right: {}'.format(i, left, right))
        
        if(left < len(heap) and heap[left] < heap[smallest]):
            smallest = left

        if(right < len(heap) and heap[right] < heap[smallest]):
            smallest = right

        if(smallest != i):
            heap[i], heap[smallest] = heap[smallest], heap[i]
            # print('changed heap {}'.format(', '.join([str(n) for n in heap])))
            heap = self.min_heapify_down(heap, smallest)
            # heap = max_heapify(heap, i)

        return heap

    def min_heapify_up(self, heap, i):
        if(i == 0):
            return heap
        elif(i in (1, 2)):
            parent = 0
        else:
            parent = int(i/2)

        if(heap[parent] > heap[i]):
            heap[i], heap[parent] = heap[parent], heap[i]
            heap = self.min_heapify_up(heap, parent)

        return heap

    def add(self, val):
       self.heap.append(val)
       self.heap = self.min_heapify_up(self.heap, len(self.heap)-1)

    def delete(self, val):
        i = self.heap.index(val)
        last_i = len(self.heap)-1
        self.heap[i], self.heap[last_i] = self.heap[last_i], self.heap[i]
        self.heap.pop()
        self.heap = self.min_heapify_down(self.heap, i)

    def get_min(self):
        return self.heap[0]

    def _extract_min(self):
        li = len(self.heap)-1
        self.heap[0], self.heap[li] = self.heap[li], self.heap[0]
        rv = self.heap.pop()
        self.heap = self.min_heapify_down(self.heap, 0)
        return rv

    def sort(self):
        while(len(self.heap)):
            yield self._extract_min()

    def __str__(self):
        return ', '.join([str(n) for n in self.heap])


def main():
    heap = [1, 2, 3, 4, 9, 9, 5, 6, 7, 8, 90, 9, 10, 11, 12, 13, 14, 15, 16]
    # heap = [1, 2, 3]
    # heap = [1, 2, 3, 4]
    # heap = [random.randint(1, 10000) for i in range(100000)]
    # max_heap = build_max_heap(heap)
    # print(', '.join([str(n) for n in max_heap]))

    h = MinHeap()
    for n in heap:
        h.add(n)

    for n in h.sort():
        print(n)


def hackerrank():
    inputs = int(input())
    h = MinHeap()
    for i in range(inputs):
        command = list(map(int, input().rstrip().split()))
        if(command[0] == 1):
            h.add(command[1])

        if(command[0] == 2):
            h.delete(command[1])

        if(command[0] == 3):
            print(h.get_min())


if __name__ == '__main__':
    hackerrank()