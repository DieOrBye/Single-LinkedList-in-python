# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:14:51 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=Node
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
    def duplicates(self):
        curr=self.head
        head=prev=Node(None)
        head.next=curr
        while curr!=None and curr.next!=None:
            if curr.data==curr.next.data:
                while curr and curr.next and curr.data==curr.next.data:
                    curr=curr.next
                curr=curr.next
                prev.next=curr
            else:
                prev=prev.next
                curr=curr.next
ll=LinkedList()
ll.push(53)
ll.push(53)
ll.push(49)
ll.push(35)
ll.push(28)
ll.push(28)
ll.push(23)
ll.printList()
ll.duplicates()
ll.printList()
        
        