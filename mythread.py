# -*- coding: utf-8 -*-
'''
    This file defines my thread class to make threads work.
    @author: ICTwangbiao
    @date: 2014-09-03
'''

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func

    def getResult(self):
        return self.res

    def run(self):
        print 'starting', self.name, 'at:', ctime()
        self.res = apply(self.func, self.args)
        print self.name, 'finished at:', ctime()

