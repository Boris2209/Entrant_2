import heapq        # очередь с приоритетами
from collections import Counter


class Node:
    """узел дерева"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf:
    """лист дерева"""
    def __init__(self, char):
        self.char = char

    def walk(self, code, acc):
        code[self.char] = acc


def huffman_encode(s):
    h = [(freq, Leaf(ch)) for ch, freq in Counter(s).items()]
    heapq.heapify(h)
    while len(h) > 1:
        freq1, left = heapq.heappop(h)
        freq2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, Node(left, right)))

    [(_freq, root)] = h
    code = {}
    root.walk(code, "")
    return code


def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    main()
