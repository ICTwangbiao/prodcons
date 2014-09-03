# -*- coding: utf-8 -*-
'''
    This implementation is used to test the problem about producers and consumers.
    @author: ICTwangbiao
    @date: 2014-09-03
'''

from random import randint
from time import sleep
from Queue import Queue
from mythread import MyThread

def writeQ(queue):
    print 'producing object for Q...',
    queue.put('xxx', 1)
    print 'size now', queue.qsize()

def readQ(queue):
    val = queue.get(1)
    print 'consumed object from Q... size now', queue.qsize()

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(30)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print 'ALL DONE'

if __name__ == '__main__':
    main()





