#!/usr/bin/python3
# -*- coding: utf-8 -*-
from problem import problem

def main():
    try:
        filename = input('file: ')
        if filename.isdigit():
            raise ValueError
        p = problem('%s.json' % filename)
        #cadena = p._file["IntSt"]["node"] + " : " + str(p._file["IntSt"]["listNodes"])
        print(p._init_state._md5)
    except ValueError:
        print("Error. Not a valid input")

if __name__ == '__main__':
    main()
