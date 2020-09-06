# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 04:44:05 2020

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
    def pallindrome(self):
        count=0
        end=self.head
        
        curr=self.head
        while end!=None:
            end=end.next
            count=count+1
        end=self.head
        if self.head==None:
            print('Empty Linked List')
        else:
            while end.next!=None:
                end=end.next
            if curr.data==end.data:
                
                    curr=curr.next
                    end.next=None
                    return 'Its a Pallindrome'
            else:
                return 'Not a Pallindrome'
            
LL=LinkedList()
LL.push('n')
LL.push('a')
LL.push('y')
LL.push('b')
LL.push('n')
print(LL.pallindrome())