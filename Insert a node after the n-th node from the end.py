# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:17:43 2020

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
    def insert(self,x,n):
        if self.head==None:
            return

        newNode=Node(n)
        curr=self.head
        l=0
        i=1
        while curr!=None:
            l=l+1
            curr=curr.next
        curr=self.head
        for i in range(l-n):
            curr=curr.next
        newNode.next=curr.next
        curr.next=newNode
ll=LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(1)
ll.printList()
ll.insert(3,2)
ll.printList()
        
        
            