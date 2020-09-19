# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 04:00:08 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def reverse(self):
        curr=self.head
        prev=None
        while curr!=None:     
            next,curr.next=curr.next,prev
            prev,curr=curr,next
        self.head=prev
    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=' ')
            curr=curr.next
ll=LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
print('Before Reverse:')
ll.printList()
print('\nAfter Reverse:')
ll.reverse()
ll.printList()