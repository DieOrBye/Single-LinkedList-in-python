# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 04:16:48 2020

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
    def search(self,key):
        curr=self.head
        while curr!=None:
            if curr.data==key:
                return True
            else:
                curr=curr.next
        return False
LL=LinkedList()
LL.push(5)
LL.push(9)
LL.push(7)
LL.push(3)
LL.push(4)
if LL.search(4):
    print('Yes its in the List')
else:
    print('Not found in this list')
                