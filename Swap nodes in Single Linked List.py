# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 04:38:36 2020

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
    def swap(self,x,y):
        if x==y:
            return
        curry=self.head
        currx=self.head
        prevx=None
        prevy=None
        while currx!=None and currx.data!=x:
            prevx=currx
            currx=currx.next
            
            
        while curry!=None and curry.data!=y:
            prevy=curry
            curry=curry.next
        
        if currx==None or curry==None:
            return
        
        if prevx!=None:
            prevx.next=curry
        else:
            self.head=curry
        
        if prevy!=None:
            prevy.next=currx
        else:
            self.head=currx
            
        temp = currx.next
        currx.next = curry.next
        curry.next = temp
    
    def printList(self): 
        tNode = self.head 
        while tNode != None: 
            print(tNode.data,end=' ') 
            tNode = tNode.next
llist = LinkedList() 
   
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
print ("Linked list before calling swapNodes: ")
llist.printList() 
llist.swap(7, 3) 
print ("\nLinked list after calling swapNodes: ")
llist.printList()