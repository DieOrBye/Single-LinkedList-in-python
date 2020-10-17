# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 01:46:36 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.arbit=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def reverse(self):
        prev=None
        curr=self.head
        nex=None
        while curr!=None:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        self.head=prev
    def arbitPointer(self):
        self.reverse()
        max=self.head
        temp=self.head.next
        while temp!=None:
            temp.arbit=max
            if max.data<temp.data:
                max=temp
            temp=temp.next
        return self.reverse()
    def printList(self):
        curr=self.head
        print('Node\tNextPointer\tArbitPointer')
        while curr!=None:
            print(curr.data,'\t\t',end='')
            if curr.next!=None:
                print(curr.next.data,'\t\t',end='')
            else:
                print('None','\t\t',end='')
            if curr.arbit!=None:
                print(curr.arbit.data,'\t\t',end='')
            else:
                print('None',end='')
            print('\n')
            curr=curr.next
ll=LinkedList()
ll.push(3)
ll.push(2)
ll.push(10)
ll.push(5)
ll.arbitPointer()
ll.printList()
                    
                    
            
        