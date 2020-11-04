# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:41:28 2020

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
def Merge(l1,l2):
        temp=None
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.data<=l2.data:
            temp=l1
            temp.next=Merge(l1.next,l2)
        else:
            temp=l2
            temp.next=Merge(l1,l2.next)
        return temp
l1=LinkedList()
for i in range(50,0,-10):
    l1.push(i)
print('First List is:')
l1.printList()
l2=LinkedList()
l2.push(60)
l2.push(35)
l2.push(18)
l2.push(15)
l2.push(5)
print('Second List is: ')
l2.printList()
l3=LinkedList()
l3.head=Merge(l1.head,l2.head)
l3.printList()
