# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 06:04:05 2020

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
    def sortedL(self):
        count=[0,0,0]
        curr=self.head
        while curr!=None:
            count[curr.data]=count[curr.data]+1
            curr=curr.next
        temp=self.head
        i=0
        while temp!=None:
            if count[i]==0:
                i=i+1
            else:
                temp.data=i
                count[i]=count[i]-1
                temp=temp.next
ll=LinkedList()
ll.push(1)
ll.push(1)
ll.push(2)
ll.push(0)
ll.push(2)
ll.push(0)
ll.push(1)
print('Actual LinkedList: ' )
ll.printList()
print('\nAfter sorted:')
ll.sortedL()
ll.printList()