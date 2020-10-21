# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:42:33 2020

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
    def printList(self,y=None):
        if self.head==None:
           curr=y 
        else:
            curr=self.head
        while curr!=None:
            print(curr.data,end='->')
            curr=curr.next
        print('None',end='')
    def partition(self,x):
        smallhead=None
        smalllast=None
        greathead=None
        greatlast=None
        equalhead=None
        equallast=None
        while self.head!=None:
            if self.head.data==x:
                if equalhead==None:
                    equalhead=equallast=self.head
                else:
                    equallast.next=self.head
                    equallast=equallast.next
            elif self.head.data<x:
                if smallhead==None:
                    smalllast=smallhead=self.head
                else:
                    smalllast.next=self.head
                    smalllast=self.head
            else:
                if greathead==None:
                    greatlast=greathead=self.head
                else:
                    greatlast.next=self.head
                    greatlast=self.head
            self.head=self.head.next
        if greatlast!=None:
            greatlast.next=None
        if smallhead==None:
            if equalhead==None:
                return greathead
            else:
                equallast.next=greathead
                return equalhead
        if equalhead==None:
            smalllast.next=greathead
            return smallhead
        smalllast.next=equalhead
        equallast.next=greathead
        return smallhead
            
ll=LinkedList()
ll.push(50)
ll.push(2)
ll.push(30)
ll.push(5)
ll.push(4)
ll.push(10)
print('Given LinkedLIst: ')
ll.printList()
print('\nLinkedList after partition:')
ll.printList(ll.partition(3))


                
                
                
                
                
                
                
                
                
                
                
                
                
                
                    