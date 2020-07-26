# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 04:59:14 2020

@author: Souhardya
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.nexxt=None
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
    def rearrange(self):
        curr=self.head
        od=[]
        ev=[]
        i=1
        while curr!=None:
            
            if curr.data%2!=0 and i%2==0:
                od.append(curr)
                
            elif curr.data%2==0 and i%2!=0:
                ev.append(curr)
            
            curr=curr.next
            i=i+1
        while len(od)!=0 and len(ev)!=0:
                od[-1].data,ev[-1].data=ev[-1].data,od[-1].data
                od.pop()
                ev.pop()
        return curr
ll=LinkedList()
ll.push(8)
ll.push(7)
ll.push(6)
ll.push(5)
ll.push(3)
ll.push(2)
ll.push(1)
print('Actual LinkedList: ')
ll.printList()
print('\nAfter Rearrange: ')
ll.rearrange()
ll.printList()

                
        