#! /usr/bin/python


class my_priority_queue (object) :
    def __init__ (self) :
        self.a = []

    def empty (self):
        return (len(self.a) == 0)

    def qsize (self):
        return len(self.a)

    def put (self,x):
        self.a.append(x)

    def get (self):
        r = min(self.a)
        self.a.remove(r)
        return r
