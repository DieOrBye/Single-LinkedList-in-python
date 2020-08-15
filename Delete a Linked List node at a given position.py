# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 07:38:28 2020

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
        print('None',end='')
    def delete(self,pos):
        curr=self.head
        if self.head==None:
            return
        if self.head.next==None:
            return
        if pos==0:
            self.head=temp.next
            curr=0
            return
        for i in range(pos-1):
            curr=curr.next
            if curr==None:
                break
        if curr is None:
            return
        if curr.next==None:
            return
        nex=curr.next.next
        curr.next=None
        curr.next=nex
ll = LinkedList() 
ll.push(7) 
ll.push(1) 
ll.push(3) 
ll.push(2) 
ll.push(8)
print('Actual LinkedList:')
ll.printList()
print('\nAfter Dleting given node')
ll.delete(4)
ll.printList()
            
        