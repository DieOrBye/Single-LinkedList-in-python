# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 02:45:22 2020

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
    def delete(self):
        curr=self.head.next
        prev=self.head
        while prev!=None and curr!=None:
            if prev.data>curr.data:
                prev.next=curr.next
                curr=None
                prev=prev.next
                if prev!=None:
                    curr=prev.next
               
            else:
                prev=prev.next
                curr=curr.next
        self.head=self.head.next  
ll=LinkedList()
ll.push(3)
ll.push(2)
ll.push(6)
ll.push(5)
ll.push(11)
ll.push(10)
ll.push(15)
ll.push(12)
print('Actual List')
ll.printList()
ll.delete()
print('\nAfter deleting')
ll.printList()

                
                