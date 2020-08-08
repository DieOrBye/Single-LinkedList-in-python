# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 07:02:46 2020

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
    def delAlt(self):
        if self.head==None:
            return
        else:
            curr=self.head
            nex=self.head.next
            while curr!=None and nex!=None:
                curr.next=nex.next
                nex=None
                curr=curr.next
                if curr!=None:
                    nex=curr.next
ll=LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print('Actual List')
ll.printList()
print('\nAfter deleting Alternatively:')
ll.delAlt()
ll.printList()