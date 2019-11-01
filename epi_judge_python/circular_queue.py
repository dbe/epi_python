from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self.start = 0
        self.end = 0
        self.a = [None] * capacity

    def enqueue(self, x):
        if(self.size() + 1 > len(self.a) / 2):
            self.resize()

        self.a[self.end] = x
        self.end = (self.end + 1) % len(self.a)

    def dequeue(self):
        val = self.a[self.start]
        self.start = (self.start + 1) % len(self.a)

        return val

    def size(self):
        if(self.end >= self.start):
            return self.end - self.start
        else:
            return len(self.a) - (self.start - self.end)

    def resize(self):
        new_a = [None] * (2 * len(self.a))
        size = self.size()
        if(self.end < self.start):

            count = 0
            for i in range(self.start, len(self.a)):
                new_a[count] = self.a[i]
                count += 1

            for i in range(0, self.end):
                new_a[count] = self.a[i]
                count += 1
        else:
            count = 0
            for i in range(self.start, self.end):
                new_a[count] = self.a[i]
                count += 1




        self.start = 0
        self.end = size
        self.a = new_a


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
