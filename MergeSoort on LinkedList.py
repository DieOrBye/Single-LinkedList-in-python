# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:47:35 2020

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
    def merge(self,a,b):
        r=None
        if a==None:
            return b
        if b==None:
            return a
        if a.data<=b.data:
            r=a
            r.next=self.merge(a.next,b)
        else:
            r=b
            r.next=self.merge(a,b.next)
        return r
    def sort(self,h):
        if h==None or h.next==None:
            return h
        mid=self.getMiddle(h)
        
        midN=mid.next
        mid.next=None
        
        l=self.sort(h)
        
        r=self.sort(midN)
        
        new=self.merge(l,r)
        return new
    def getMiddle(self,h):
        if h==None:
            return
        slow=h
        fast=h
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
ll=LinkedList()
ll.push(15)
ll.push(10)
ll.push(5)
ll.push(20)
ll.push(3)
ll.push(2)
print('Given List:')
ll.printList()
ll.head=ll.sort(ll.head)
print('After Sorting')
ll.printList()
        