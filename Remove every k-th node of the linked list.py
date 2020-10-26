# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:56:18 2020

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
    def delete(self,k):
        if self.head==None:
            return
        curr=self.head
        prev=None
        c=0
        while curr!=None:
            c=c+1
            if k==c:
                prev.next=curr.next
                c=0
            if curr!=0:
                prev=curr
            curr=curr.next
ll=LinkedList()
for i in range(8,0,-1):
    ll.push(i)
print('Given LinkedList: ')
ll.printList()
ll.delete(3)
print('After Deleting every kth node: ')
ll.printList()