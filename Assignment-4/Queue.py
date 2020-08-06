# -*- coding: utf-8 -*-


from Node import Node


class Empty(Exception):
    pass


class LinkedQueue(object):

    __slots__ = ['_front', '_rear', '_size']

    def __init__(self):
        self._front = Node()
        self._rear = self._front
        self._size = 0

    def __str__(self):
        pos = self._front
        res = '<'
        while pos._nextNode is not None:
            res = res + str(pos._nextNode._itemNode) + ', '
            pos = pos._nextNode
        res = res + '>'
        return res

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._front._nextNode is None

    def front(self):
        if self._front._nextNode is None:
            raise Empty("Queue is empty!")
        return self._front._nextNode._itemNode

    def dequeue(self):
        if self._front._nextNode is None:
            raise Empty("Queue is empty!")
        item = self._front._nextNode._itemNode
        self._front = self._front._nextNode
        self._size -= 1
        return item

    def enqueue(self, item):
        self._rear._nextNode = Node(item, None)
        self._rear = self._rear._nextNode
        self._size += 1
        return
