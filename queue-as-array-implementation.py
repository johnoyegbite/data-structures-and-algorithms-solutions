# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 07:56:11 2019

@author: USER
"""
# SOLVED!
class QueueAsArray(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.front_index = -1
        self.rear_index = -1
        self.EMPTY = -1
        self.empty_at_x = False
        
    def is_full(self):
        # for circular list interpretation
        return ((self.rear_index+1) % self.capacity) == self.front_index
    
    def is_empty(self):
        empty_at_beginning = self.front_index == self.rear_index == self.EMPTY
        return empty_at_beginning
    
    def has_one_child(self):
        return self.front_index == self.rear_index and self.front_index != self.EMPTY
        
    def enqueue(self, data):
        if self.is_full():
            raise Exception(f"Queue is full: '{data}' can't be added")
        if self.is_empty():
            self.front_index = 0
            self.rear_index = 0
        else:
            # for circular list interpretation
            self.rear_index = (self.rear_index+1) % self.capacity
        # rear index normally should be at the RHS of front index
        # if is at the LHS, then queue has an empty space at the LHS
        if self.rear_index < self.front_index: # rear index normally should be at the RHS of the front index
                                              # if is at the LHS, then queue has an empty space at the LHS
            self.queue[self.rear_index] = data
        elif self.empty_at_x and self.front_index == self.rear_index:
            self.queue[self.rear_index] = data
        else:
            self.queue.append(data)
        
    def empty_queue(self):
        self.front_index, self.rear_index = -1, -1
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.queue[self.front_index]
            if self.has_one_child():
                self.empty_queue()
                self.empty_at_x = True
            else:
                self.front_index = (self.front_index+1) % self.capacity
            return data
    
    def front(self):
        if not self.is_empty():
            return self.queue[self.front_index]
        return None
    
    def __str__(self):
        print("-----Queue Info.-----")
        print(f"Front index: {self.front_index}")
        print(f"Rear index: {self.rear_index}")
        print(f"Queue: {self.queue}")
        return ("-----END-----")
  

if __name__ == "__main__":
    queue = QueueAsArray(6)      
          
    l = [4, 2, 6, 10, 78, 5]
    
    for data in l:
        queue.enqueue(data)
        
    print(queue)
    queue.dequeue()
    print(queue.front()) # 2
    
    print(queue)
    queue.dequeue()
    print(queue.front()) # 6
    
    print(queue)
    queue.dequeue()
    print(queue.front()) # 10
    
    print(queue)
    queue.dequeue()
    print(queue.front()) # 78
    
    print(queue)
    queue.dequeue()
    print(queue.front()) # 5
    
    print(queue)
    queue.dequeue()
    print(queue.front()) # None
    
    print(queue)
    queue.enqueue(92)
    print(queue.front()) # 92
    
    print(queue)
    queue.dequeue()
    print(queue.front()) # None
    