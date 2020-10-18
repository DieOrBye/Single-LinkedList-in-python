# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:17:54 2020

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
    def rearrange(self):
        if self.head==None:
            return 'Empty'
        odd=self.head
        even=self.head.next
        evenF=even
        while True:
            if odd==None or  even==None or even.next==None:
                odd.next=evenF
                break
            odd.next=even.next
            odd=even.next
            if odd.next==None:
                even.next=None
                odd.next=evenF
                break
            even.next=odd.next
            even=odd.next
        result=self.printList()
        return result
    
ll=LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print('After Rearranging: ')
print(ll.rearrange())



        
        
        