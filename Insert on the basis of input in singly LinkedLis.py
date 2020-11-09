# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:33:51 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data,k):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        if k==0:
            new_node.next=self.head
            self.head=new_node
        if k==1:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node
    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=' ')
            curr=curr.next
ll=LinkedList()
lst=[int(i) for i in input().split('->')]
for i in range(len(lst)-1):
    ll.insert(lst[i],lst[i+1])
print('Generated LinkedList: ')
ll.printList()


# Input: 9->0->5->1->6->1->2->0->5->0
# Output: 5 2 9 5 6