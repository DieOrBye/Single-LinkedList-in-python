# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 06:24:36 2020

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
    def skipMdelN(self,M,N):
        curr=self.head
        count=1
        while curr!=None:
            while count<M:
                curr=curr.next
                count=count+1
            
            t=curr.next
            for i in range(1,N+1):
                if t==None:
                    break
                else:
                    t=t.next
            curr.next=t
            curr=t
            count=1
ll=LinkedList()
ll.push(10)
ll.push(9)
ll.push(8)
ll.push(7)
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print('Actual LinkedList')
ll.printList()
print('\nAfter Doing Work')
ll.skipMdelN(2,3)
ll.printList()