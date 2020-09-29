# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:15:44 2020

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
            print(curr.data,end=' ')
            curr=curr.next
    def rotate(self,k):
        curr=self.head
        count=1
        if k==0:
            return
        else:
            while (count<k and curr!=None):
                curr=curr.next
                count=count+1
            if curr.next==None:
                return
            kthNode=curr
            while curr.next!=None:
                curr=curr.next
            curr.next=self.head
            self.head=kthNode.next
            kthNode.next=None
ll=LinkedList()
ll.push(60)
ll.push(50)
ll.push(40)
ll.push(30)
ll.push(20)
ll.push(10)
print('Actual LinkedList: ' )
ll.printList()
print('\nAfter Rotate:')
ll.rotate(4)
ll.printList()

            
            
                
        
        