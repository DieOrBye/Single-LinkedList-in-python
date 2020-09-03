# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 03:24:09 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
                
            curr.next=Node(data)
    def createloop(self,n):
        end=self.head
        if self.head==None:
            print('Empty Linked List')
        else:
            while end.next!=None:
                end=end.next
            loop=self.head
        # n in that node which is connected to end node
            for i in range(1,n):
                loop=loop.next
            end.next=loop
    def looplength(self):
        slow=self.head
        fast=self.head
        flag=0
        if self.head==None:
            return 0
        else:
            while(slow.next and fast.next and fast.next.next)!=None:
                if slow==fast and flag!=0:
                    count=1
                    slow=slow.next
                    while slow!=fast:
                        slow=slow.next
                        count=count+1
                    return count
                
                slow=slow.next
                fast=fast.next
                flag=1
            return 0
        
ll=LinkedList()
ll.append(5)
ll.append(7)
ll.append(9)
ll.append(3)
ll.createloop(2)
x=ll.looplength()
if ll.head == None:
    print('Empty')
else:
    print(x)       