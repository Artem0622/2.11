#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    def foo(typ):
        def bar(spisok):
            if typ == list:
                return list(map(int, spisok.split()))
            return tuple(map(int, spisok.split()))
        return bar

    print(foo(list)('1 2 3 4 5 6 7 8 9 10'))
    print(foo(tuple)('1 2 3 4 5 6 7 8 9 10'))
