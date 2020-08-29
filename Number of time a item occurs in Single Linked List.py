# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:15:01 2020

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
    def duplicate(self,key):
        temp=self.head
        count=0
        while temp!=None:
            if temp.data==key:
                count=count+1
                temp=temp.next
            else:
                temp=temp.next
        return count
ll=LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(1)
ll.push(1)
ll.push(4)
ll.push(1)
print(ll.duplicate(1))