# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 05:34:52 2020

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
    def getNth(self,index):
        count=0
        curr=self.head
        while curr!=None:
            if count==index:
                return curr.data
            else:
                curr=curr.next
                count=count+1
ll=LinkedList()
ll.push(5)
ll.push(9)
ll.push(7)
ll.push(1)
print(ll.getNth(2))