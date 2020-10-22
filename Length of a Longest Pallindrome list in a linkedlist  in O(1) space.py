# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:35:39 2020

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
    def common(self,a,b):
        c=0
        while a!=None and b!=None:
            if a.data==b.data:
                c=c+1
            a=a.next
            b=b.next
        return c
    def pallindrome(self):
        result=0
        prev=None
        curr=self.head
        while curr!=None:
            next=curr.next
            curr.next=prev
            result=max(result,2*self.common(prev,next)+1)
            result=max(result,2*self.common(curr,next))
            prev=curr
            curr=next
        return result
ll=LinkedList()
ll.push(15)
ll.push(2)
ll.push(4)
ll.push(3)
ll.push(4)
ll.push(2)
ll.printList()
print(ll.pallindrome())