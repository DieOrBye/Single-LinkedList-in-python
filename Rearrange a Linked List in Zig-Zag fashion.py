# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:47:24 2020

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
            print(curr.data,end='')
            print('->',end='')
            curr=curr.next
        print('None',end='')
    def zigzag(self):
        flag=True
        curr=self.head
        while curr.next!=None:
            if flag:    
                if curr.data>curr.next.data:
                    t=curr.data
                    curr.data=curr.next.data
                    curr.next.data=t                
            else:
                if curr.data<curr.next.data:
                    t=curr.data
                    curr.data=curr.next.data
                    curr.next.data=t
            curr=curr.next
            if flag:
                flag=False
            else:
                flag=True
ll=LinkedList()
ll.push(1)
ll.push(2)
ll.push(6)
ll.push(8)
ll.push(7)
ll.push(3)
ll.push(4)
print('Given List:')
ll.printList()
print('\nAfter Rearrange ZigZag: ')
ll.zigzag()
ll.printList()
            
                
            