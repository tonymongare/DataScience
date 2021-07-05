# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:31:57 2021

@author: tonyloi
"""

#implementing a queue using a list
def __init__(self):
    self.queue=[]
    
def enqueue(self,item):
    return self.queue.append(item)


def dequeue(self):
    if len(self.queue)<1:
        return None
    return self.queue.pop(0)

def size(self):
    return len(self.queue)

def display(self):
    return (self.queue)


q= Queue()

q.enque(12)
q.enque(23)
q.enque(34)
q.enque(45)
q.enque(56)

q.display()
q.dequeue()


    
