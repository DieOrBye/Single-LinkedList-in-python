# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:38:23 2020

@author: USER
"""

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
# creat a node
        new_node=Node(value)
# point it towards the current head node address
        new_node.next=self.head
# reassign it as the head node
        self.head=new_node
        
    def traverse(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
ll=LinkedList()

# these values will be the head node one after another
ll.insert(3)
ll.insert(5)
ll.insert(95)
ll.traverse()

        
        