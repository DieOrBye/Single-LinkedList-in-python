# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 06:43:10 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        selfnext=None
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
    def reverse(self,head,k):
        curr=head
        prev=None
        next=None
        count=0
        while (count<k and curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count=count+1
        if head!=None:
            head.next=curr
        count=0
        while (count<k-1 and curr!=None):
            curr=curr.next
            count=count+1
        if curr!=None:
            curr.next= self.reverse(curr.next,k)
        return prev
llist = LinkedList() 
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1)
print('Before reverse')
llist.printList()
llist.head=llist.reverse(llist.head,3)
print('\nAfter Reversing')
llist.printList()