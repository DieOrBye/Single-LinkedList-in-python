# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 06:47:12 2020

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
            print(curr.data,end=' ')
            curr=curr.next
    def move(self):
        curr=self.head
        prev=None
        if curr==None or curr.next==None:
            return 
        while curr!=None and curr.next!=None:
            prev=curr
            curr=curr.next
        prev.next=None
        curr.next=self.head
        self.head=curr
    
ll=LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
ll.move()
ll.printList()
            