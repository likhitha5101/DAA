# -*- coding: utf-8 -*-


class Node(object):

    __slots__ = ['_itemNode', '_nextNode']

    def __init__(self, itemNode=None, nextNode=None):
        self._itemNode = itemNode
        self._nextNode = nextNode

    def __str__(self):
        return str(self._itemNode)

    def setItem(self, itemNode=None):
        self._itemNode = itemNode

    def setNext(self, nextNode=None):
        self._nextNode = nextNode

    def getItem(self):
        return self._itemNode

    def getNext(self):
        return self._nextNode
