# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:05:58 2021

@author: tonyloi
"""
#implementing a stack using a list

def create_stack(stack):
    stack=[]
    
    
def check_empty(stack):
    return len(stack)==0

def append_item(stack, item):
    return stack.append(item)
    print("appended item is" +item)

    
def pop_item(stack):
    if check_empty(stack):
        return "stack is empty"
    
    return stack.pop()

stack = create_stack()


#live example on using list to implement stack

stack=[]

print("Initial stack")

print(stack.append('a'))
print(stack.append('b'))
print(stack.append('c'))

print('\n This stack after appending')


print(stack.pop('a'))
print(stack.pop('b'))

print(stack.pop('c'))

print('\n this is stack is empty')

print(stack)


#implementing stack uisng the dequeque method

from collections import deque

stack = deque()

print('\nthis stack is empty')


print(stack.append(12))
print(stack.append(34))
print(stack.append(44))

print('\n this is stack after appending')


#pop out every element

print(stack.pop(12))
print(stack.pop(34))
print(stack.pop(44))

print('\n this is the empty stacka after poping')

from queue import LifoQueue

stack=LifoQueue(max_size=3)

#stack size using qsize()
stack.qsize()


print('\n Using put method to fill stack')
print(stack.put('a'))
print(stack.put('b'))
print(stack.put('c'))


print('Full', stack.full())
print('size',stack.qsize())


print('\n removin stack elements')
print(stack.get())
print(stack.get())
print(stack.get())

print('\n cheking if stack is empty')
print(stack.isEmpty())









