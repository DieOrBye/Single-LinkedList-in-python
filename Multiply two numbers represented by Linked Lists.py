# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:25:08 2020

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
            print(curr.data,end='->')
            curr=curr.next
        print('None')
    def multiply(self,lst):
        firstNumber=0
        secondNumber=0
        curr=self.head
        while curr!=None:
            firstNumber=(firstNumber*10+curr.data)
            curr=curr.next
        temp=lst.head
        while temp!=None:
            secondNumber=(secondNumber*10+temp.data)
            temp=temp.next
        return firstNumber*secondNumber
ll=LinkedList()
ll.push(6)
ll.push(4)
ll.push(9)
ll2=LinkedList()
ll2.push(4)
ll2.push(8)
print(ll.multiply(ll2))            