# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 06:50:59 2019

@author: John Oyegbite
"""
# SOLVED!
"""
Problem:
    Design a data structure that supports all following operations in average O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:
    // Init an empty set.
    RandomizedSet randomSet = new RandomizedSet();
    
    // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.insert(1);
    
    // Returns false as 2 does not exist in the set.
    randomSet.remove(2);
    
    // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(2);
    
    // getRandom should return either 1 or 2 randomly.
    randomSet.getRandom();
    
    // Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(1);
    
    // 2 was already in the set, so return false.
    randomSet.insert(2);
    
    // Since 2 is the only number in the set, getRandom always return 2.
    randomSet.getRandom();
"""
from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set_dict = {}
        self.set_list = []
        self.size = 0
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.set_dict:
            self.set_dict[val] = self.size
            self.set_list.append(val)
            self.size += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set_dict:
            val_idx = self.set_dict[val]  # Get the index of value to be removed
            last_val = self.set_list[self.size-1]  # Get the last value in the list
            self.set_list[val_idx], self.set_list[self.size-1] = self.set_list[self.size-1], self.set_list[val_idx]  # swap value to remove with last value; Now the last value is the value to be removed
            self.set_list.pop()  # now, remove the last value
            self.set_dict[last_val] = val_idx  # update the index of the swapped value
            del self.set_dict[val]  # delete the required val
            self.size -= 1  # update the size of the set
            return True
        return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.set_list[randint(0, self.size-1)]


if __name__ == "__main__":
    # Your RandomizedSet object will be instantiated and called as such:
    random_set = RandomizedSet()
    print(random_set.insert(1)) # True
    print(random_set.remove(2)) # False 
    print(random_set.insert(2)) # True
    print(random_set.getRandom()) #
    print(random_set.remove(1)) # True
    print(random_set.insert(2)) # False
    print(random_set.getRandom()) #
    
