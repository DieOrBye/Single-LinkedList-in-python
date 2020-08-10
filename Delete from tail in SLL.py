# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:09:21 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def del_tail(self):
        temp=self.head
        if temp==None:
            print('Empty Linked List')
        else:  
             while temp.next.next!=None:
                 temp=temp.next
             temp.next=None
LL=LinkedList()
LL.del_tail()

#will throw error because it doesnot have any value in the linked list