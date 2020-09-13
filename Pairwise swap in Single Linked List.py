# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 06:01:22 2020

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
    def pairwiseswap(self):
        temp=self.head
        if temp==None:
            return
        else:
            while temp!=None and temp.next!=None:
                temp.data,temp.next.data=temp.next.data,temp.data
                temp=temp.next.next
    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=' ')
            curr=curr.next
ll=LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print('Linked List before swapping by pair')
ll.printList()
print('\nLinked List after swapping by pair')
ll.pairwiseswap()
ll.printList()