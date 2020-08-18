# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 04:01:28 2020

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
        new_node.next = self.head 
        self.head = new_node
    def countNode(self):
        temp=self.head
        count=0
        while temp!=None:
            temp=temp.next
            count=count+1
        return count
LL=LinkedList()
LL.push(5)
LL.push(8)
LL.push(7)
LL.push(2)
print(LL.countNode())
        
        
            