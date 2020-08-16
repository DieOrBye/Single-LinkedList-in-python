# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 07:55:05 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node(15)
    second=Node(4)
    third=Node(39)
    llist.head.next=second
    second.next=third
    llist.printList()
