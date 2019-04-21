import random

class MaxHeap:
    def __init__(self):
        self.heap = []

    def build_max_heap(self, heap):
        print('build_max_heap {}'.format(', '.join([str(n) for n in heap])))
        l = int(len(heap)/2)
        for i in range(l+1, -1, -1):
            heap = max_heapify(heap, i)

        return heap

    def max_heapify_down(self, heap, i):
        if(i==0):
            left = 1
            right = 2
        else:
            left = 2 * i + 1
            right = 2 * i
        largest = i
        
        # print('{} max heapify, left: {}, right: {}'.format(i, left, right))
        
        if(left < len(heap) and heap[left] > heap[largest]):
            largest = left

        if(right < len(heap) and heap[right] > heap[largest]):
            largest = right

        if(largest != i):
            heap[i], heap[largest] = heap[largest], heap[i]
            # print('changed heap {}'.format(', '.join([str(n) for n in heap])))
            heap = self.max_heapify_down(heap, largest)
            # heap = max_heapify(heap, i)

        return heap

    def max_heapify_up(self, heap, i):
        if(i == 0):
            return heap
        elif(i in (1, 2)):
            parent = 0
        else:
            parent = int(i/2)

        if(heap[parent] < heap[i]):
            heap[i], heap[parent] = heap[parent], heap[i]
            heap = self.max_heapify_up(heap, parent)

        return heap

    def add(self, val):
       self.heap.append(val)
       self.heap = self.max_heapify_up(self.heap, len(self.heap)-1)

    def _extract_max(self):
        li = len(self.heap)-1
        self.heap[0], self.heap[li] = self.heap[li], self.heap[0]
        rv = self.heap.pop()
        self.heap = self.max_heapify_down(self.heap, 0)
        return rv

    def sort(self):
        while(len(self.heap)):
            yield self._extract_max()

    def __str__(self):
        return ', '.join([str(n) for n in self.heap])


def main():
    heap = [1, 2, 3, 4, 9, 9, 5, 6, 7, 8, 90, 9, 10, 11, 12, 13, 14, 15, 16]
    # heap = [1, 2, 3]
    # heap = [1, 2, 3, 4]
    # heap = [random.randint(1, 10000) for i in range(100000)]
    # max_heap = build_max_heap(heap)
    # print(', '.join([str(n) for n in max_heap]))

    h = MaxHeap()
    for n in heap:
        h.add(n)

    for n in h.sort():
        print(n)


if __name__ == '__main__':
    main()