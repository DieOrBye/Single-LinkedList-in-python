# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:55:01 2020

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
    def append(self,new_data):
        new_node=Node(new_data)
        last=self.head
        while last.next!=None:
            last=last.next
        last.next=new_node
    def deletekey(self,k):
        temp=self.head
        if temp.data==k:
                self.head=temp.next
                temp=None
                return
        while temp!=None:
            if temp.data==k:
                break
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp=None
        
    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end='->')
            curr=curr.next
        print('None')
    def rearrange(self,k):
        c=0
        curr=self.head
        while curr!=None:
            if curr.data==k:
                c=c+1
            curr=curr.next
        for i in range(c):
            self.deletekey(k)
            self.append(k)
ll=LinkedList()
ll.push(60)
ll.push(10)
ll.push(40)
ll.push(30)
ll.push(10)
ll.push(20)
ll.push(10)
ll.printList()
ll.rearrange(10)
ll.printList()