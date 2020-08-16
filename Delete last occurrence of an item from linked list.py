# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 03:22:10 2020

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
    def lastOccur(self,x):
        temp=self.head
        prev=None
        while temp!=None:
            if temp.data==x:
                ptr=temp
            temp=temp.next
        if ptr!=None and ptr.next==None:
            temp=self.head
            while temp.next!=ptr:
                temp=temp.next
            temp.next=None
        if ptr!=None and ptr.next!=None:
            ptr.data=ptr.next.data
            temp=ptr.next
            ptr.next=ptr.next.next
        return self.printList()
ll=LinkedList()
ll.push(4)
ll.push(4)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print('Entered LikedList: ')
ll.printList()
print('\nAfter Deleting Last occurance:')
ll.lastOccur(4)
