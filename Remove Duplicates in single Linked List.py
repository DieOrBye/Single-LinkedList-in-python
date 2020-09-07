# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:01:24 2020

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
    
    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.next
    def duplicate(self):
        curr=self.head
        if curr==None:
            return
        else:
            while curr.next!=None:
                if curr.data==curr.next.data:
                    new=curr.next.next
                    curr.next = None
                    curr.next = new 
                else: 
                    curr = curr.next
            return self.head
ll=LinkedList()
ll.push(9)
ll.push(7)
ll.push(7)
ll.push(4)
ll.push(4)
ll.push(3)
ll.push(3)
print('Ceated List')
ll.printList()
print('\nAfter removing duplicates')
ll.duplicate()
ll.printList()