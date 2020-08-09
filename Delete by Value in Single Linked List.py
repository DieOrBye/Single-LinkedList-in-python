# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:35:10 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def del_value(self,item):
        if self.head!=None:
            if self.head.data==item:
                self.head==self.head.next
                return
            temp=self.head
            while temp.next!=None:
                if temp.next.data==item:
                    break
                temp=temp.next
                if temp.next==None:
                    print('Not Found')
                else:
                    temp.next=temp.next.next
        else:
             print('Linked List is Empty')
LL=LinkedList()
LL.del_value(100)
                    