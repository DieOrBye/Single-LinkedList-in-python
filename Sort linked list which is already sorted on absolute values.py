# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 02:42:51 2020

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
        print('None',end='')
    def sort(self):
        prev=self.head
        curr=self.head.next
        while curr!=None:
            if curr.data<prev.data:
                prev.next=curr.next
                curr.next=self.head
                self.head=curr
                curr=prev
            else:
                prev=curr
            curr=curr.next
        return self.printList()
ll=LinkedList()
ll.push(-5)  
ll.push(5)  
ll.push(4)  
ll.push(3)  
ll.push(-2)  
ll.push(1)  
ll.push(0)
print('Sorted LinkedList with absolute values: ')
ll.printList()
print('\nSorted LinkedList with actual Values:')
ll.sort()