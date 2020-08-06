# -*- coding: utf-8 -*-


class Point(object):

    __slots__ = ['_x', '_y']

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return "(" + str(self._x) + "," + str(self._y) + ")"

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def distance(self, other):
        x_diff = (self._x - other._x) ** 2
        y_diff = (self._y - other._y) ** 2
        return (x_diff + y_diff) ** 0.5

    def translate(self, x=0, y=0):
        self._x += x
        self._y += y
