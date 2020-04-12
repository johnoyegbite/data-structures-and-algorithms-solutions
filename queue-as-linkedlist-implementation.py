# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:24:47 2019

@author: USER
"""
# SOLVED!
class Data(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class QueueAsLinkedList(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.EMPTY = None
        self.length = 0
    
    def is_empty(self):
        return self.front == self.rear == self.EMPTY
        
    def enqueue(self, data):
        elem = Data(data)
        if self.is_empty():
            self.front = elem
            self.rear = elem
        else:
            self.rear.next = elem
            elem.prev = self.rear 
            self.rear = elem
        self.length += 1
        
    def dequeue(self):
        if self.is_empty():
            return self.EMPTY
        data_deleted = self.front.data
        if self.front.next:
            self.front = self.front.next
        else:
            self.front = self.EMPTY
            self.rear = self.EMPTY
        self.length -= 1
        return data_deleted
        
    def front_data(self):
        if not self.is_empty():
            return self.front.data
        return None
    
    def size(self):
        return self.length
    
    def __str__(self):
        print("-----Queue Info.-----")
        if not self.is_empty():
            front = self.front
            queue = ""
            pointer = ""
            while front.next:
                pointer
                queue = queue + pointer + str(front.data)
                front = front.next
                pointer = " <=> "
            queue = queue + pointer + str(front.data)
            print(queue)
        else:
            print("Empty")
        return ("-----END-----")
        
        
if __name__ == "__main__":
    queue = QueueAsLinkedList()      
          
    l = [4, 2, 6, 10, 78, 5]
    
    for data in l:
        queue.enqueue(data)
        
    print(queue)
    queue.dequeue()
    print(queue.front_data()) # 2
    print()
    
    print(queue)
    queue.dequeue()
    print(queue.front_data()) # 6
    print()
    
    print(queue)
    queue.dequeue()
    print(queue.front_data()) # 10
    print()
    
    print(queue)
    queue.dequeue()
    print(queue.front_data()) # 78
    print()
        
    print(queue)
    queue.dequeue()
    print(queue.front_data()) # 5
    print()
    
    print(queue)
    queue.dequeue()
    print(queue.front_data()) # None
    print()
    
    print(queue)
    queue.enqueue(92)
    print(queue.front_data()) # 92
    print()
    
    print(queue)
    queue.dequeue()
    print(queue.front_data()) # None
    print()
            
s