# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 02:27:32 2020

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
    def pallindrome(self):
        curr=self.head
        temp=[]
        while curr!=None:
            temp.append(str(curr.data))
            curr=curr.next
        string=''.join(temp)
        return self.checkPallindrome(string)
    def checkPallindrome(self,s):
        if s==s[::-1]:
            return True
        else:
            return False
ll=LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(2)
ll.push(1)
print('LinkedList is Pallindrome = ',ll.pallindrome())    