# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:37:03 2020

@author: Souhardya
"""
import random
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=' ')
            curr=curr.next
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printRandom(self):
        if self.head==None:
            return 
        if self.head!=None and self.head.next==None:
            print(self.head.data)
        random.seed()
        curr=self.head.next
        n=2
        while curr!=None:
            
            if random.randrange(n)==0:
                result=curr.data
            curr=curr.next
            n=n+1
        print(result)
ll=LinkedList()
ll.push(3)
ll.push(2)
ll.push(1)
ll.printRandom()
        