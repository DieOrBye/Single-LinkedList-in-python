# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:48:29 2020

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
            print(curr.data,end=' ')
            curr=curr.next
    def delete(self,data):
        temp = self.head 
        prev = self.head 
        if temp.data == data: 
            if temp.next is None: 
                print("Can't delete the node as it has only one node") 
            else: 
                temp.data = temp.next.data 
                temp.next = temp.next.next
            return
        while temp.next is not None and temp.data != data: 
            prev = temp 
            temp = temp.next
        if temp.next is None and temp.data !=data: 
            print("Can't delete the node as it doesn't exist")
        elif temp.next is None and temp.data == data: 
            prev.next = None
        else: 
            prev.next = temp.next
llist = LinkedList() 
llist.push(3) 
llist.push(2) 
llist.push(6) 
llist.push(5) 
llist.push(11) 
llist.push(10) 
llist.push(15) 
llist.push(12) 
  
print("Given Linked List: ", end = ' ') 
llist.printList() 
print("\n\nDeleting node 10:") 
llist.delete(10) 
print("Modified Linked List: ", end = ' ') 
llist.printList() 
print("\n\nDeleting first node") 
llist.delete(12) 
print("Modified Linked List: ", end = ' ') 
llist.printList()
        