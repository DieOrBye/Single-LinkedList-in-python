# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 06:03:18 2020

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
    def reverse(self,head,k):
        temp=head
        prev=None
        count=0
        next=None
        while (temp!=None and count<k):
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
            count=count+1
        if next!=None:
            head.next = self.reverse(next, k)
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