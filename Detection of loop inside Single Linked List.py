# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:51:54 2020

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
    def detectLoop(self):
        s=set()
        temp=self.head
        while temp!=None:
            if temp in s:
                return True
            else:
                s.add(temp)
                temp=temp.next
        return False
ll=LinkedList()
ll.push(1)
ll.push(6)
ll.push(7)
ll.push(6)
ll.push(30)

# creating loop to test
# ll.head.next.next.next=ll.head

if ll.detectLoop():
    print('Loop inside')
else:
    print('No Loop inside')