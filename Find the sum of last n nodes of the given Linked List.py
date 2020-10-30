# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:52:22 2020

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
    def add(self,n):
        c=0
        temp=self.head
        while temp!=None:
            c=c+1
            temp=temp.next
        curr=self.head
        while c!=n:
            c=c-1
            curr=curr.next
        lst=[]
        while curr!=None:
            lst.append(curr.data)
            curr=curr.next
        return sum(lst)
ll=LinkedList()
ll.push(14)
ll.push(16)
ll.push(5)
ll.push(9)
ll.push(7)
ll.push(15)
ll.printList()
print(ll.add(4))