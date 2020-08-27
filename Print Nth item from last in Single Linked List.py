# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 05:51:48 2020

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
    def PrintNthFromLast(self,n):
        length=0
        temp=self.head
        while temp!=None:
            length=length +1
            temp=temp.next
        if n>length:
            print('List Out of Index')
        else:
            temp=self.head
            for i in range(length-n):
                temp=temp.next
            return (temp.data)
ll = LinkedList()  
ll.push(20)  
ll.push(4)  
ll.push(15)  
ll.push(35) 
print(ll.PrintNthFromLast(3))