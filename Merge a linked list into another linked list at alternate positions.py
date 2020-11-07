# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:07:38 2020

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
            print(curr.data,end='->')
            curr=curr.next
        print('None')
    def Merge(self,b):
        a=self.head
        x=b.head
        while a!=None and x!=None:
            a_next=a.next
            x_next=x.next
            x.next=a_next
            a.next=x
            a=a_next
            x=x_next
        b.head=x
        
        
l1=LinkedList()
l2=LinkedList()
l1.push(3)
l1.push(2)
l1.push(1)
print('1st LinkedList:')
l1.printList()
for i in range(8,3,-1):
    l2.push(i)
print('Second LinkedList')
l2.printList()
print('After Merge First List')
l1.Merge(l2)
l1.printList()
print('After Merge second List')
l2.printList()

