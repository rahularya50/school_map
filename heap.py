from functools import total_ordering


@total_ordering
class WeightedNode:
    def __init__(self, contents, val):
        self.contents = contents
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def export(self):
        return self.contents, self.val


# Heap no longer needed? Re-implement as Fibonacci?
class Heap:
    def __init__(self):
        self.elements = []

    def insert(self, new):
        self.elements.append(new)
        self.up_heap()

    def extract_min(self):
        out = self.elements[0]
        if len(self.elements) > 1:
            self.elements[0] = self.elements.pop()
            self.down_heap()
        else:
            self.elements.pop()
        return out

    def up_heap(self, index=None):
        if index is None:
            index = len(self.elements) - 1
        if index != 0 and self.elements[index] < self.elements[(index + 1) // 2 - 1]:
            self.elements[index], self.elements[(index + 1) // 2 - 1] = self.elements[(index + 1) // 2 - 1], \
                                                                        self.elements[index]
            self.up_heap((index + 1) // 2 - 1)

    def down_heap(self, index=0):
        if index < len(self.elements) // 2 and self.elements[index] > self.elements[index * 2 + 1] or (
                        len(self.elements) > index * 2 + 2 and self.elements[index] > self.elements[index * 2 + 1]):
            if len(self.elements) == index * 2 + 2 or self.elements[index * 2 + 1] < self.elements[index * 2 + 2]:
                self.elements[index], self.elements[index * 2 + 1] = self.elements[index * 2 + 1], self.elements[index]
                self.down_heap(index * 2 + 1)
            else:
                self.elements[index], self.elements[index * 2 + 2] = self.elements[index * 2 + 2], self.elements[index]
                self.down_heap(index * 2 + 2)
