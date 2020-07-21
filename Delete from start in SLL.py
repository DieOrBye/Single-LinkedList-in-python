# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 08:31:44 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def delete_head(self):
        if self.head==None:
            print('LL is empty')
        else:
            self.head.next=self.head
LL=LinkedList()
LL.delete_head()