#!/bin/python3
'''
Jesse loves cookies. He wants the sweetness of all his cookies to be greater than value.
To do this, Jesse repeatedly mixes two cookies with the least sweetness. 
He creates a special combined cookie with:
sweetness 1 x Least sweet cookie  2 x 2nd least sweet cookie

He repeats this procedure until all the cookies in his collection have a sweetness.
You are given Jesse's cookies. Print the number of operations required to give the cookies a sweetness.
Print  if this isn't possible.

Input Format
cookies desired_sweetness

The first line consists of integers , the number of cookies and , the minimum required sweetness, separated by a space. 
The next line contains  integers describing the array  where  is the sweetness of the  cookie in Jesse's collection.

Constraints

Output Format

Output the number of operations that are needed to increase the cookie's sweetness . 
Output  if this isn't possible.

Sample Input

6 7
1 2 3 9 10 12
Sample Output

2
'''
import os
import sys


class MinHeap:
    def __init__(self):
        self.heap = []

    def load_heap(self, heap):
        self.heap = self.build_min_heap(heap)

    def build_min_heap(self, heap):
        # print('build_min_heap {}'.format(', '.join([str(n) for n in heap])))
        l = int(len(heap)/2)
        for i in range(l+1, -1, -1):
            heap = self.min_heapify_down(heap, i)

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

    def extract_min(self):
        li = len(self.heap)-1
        self.heap[0], self.heap[li] = self.heap[li], self.heap[0]
        rv = self.heap.pop()
        self.heap = self.min_heapify_down(self.heap, 0)
        return rv

    def sort(self):
        while(len(self.heap)):
            yield self.extract_min()

    def __str__(self):
        return ', '.join([str(n) for n in self.heap])

    def __len__(self):
        return len(self.heap)



#
# Complete the cookies function below.
#
def cookies(k, A):
    h = MinHeap()
    h.load_heap(A)

    cnt = 0
    while(k > h.get_min() and len(h) > 1):
        lf1 = h.extract_min()
        lf2 = h.extract_min()
        rez = lf1 + (2*lf2)
        h.add(rez)
        cnt += 1

    if(len(h) == 1 and h.get_min() < k):
        return -1

    return cnt

    #
    # Write your code here.
    #

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
