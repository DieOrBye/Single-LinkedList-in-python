# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:03:18 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self, new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def middle(self):
        length=0
        temp=self.head
        while temp!=None:
            temp=temp.next
            length=length +1
        temp=self.head
        for i in range(int(length/2)):
            temp=temp.next
        return temp.data
ll=LinkedList()
ll.push(5)
ll.push(7)
ll.push(9)
ll.push(3)
ll.push(4)
print(ll.middle())