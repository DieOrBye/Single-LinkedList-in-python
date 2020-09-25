# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 04:36:34 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

def push(key):
        new_node=Node()
        new_node.data=key
        new_node.next=None
        return new_node
def printList(Node):
        
        while Node!=None:
            print(Node.data,end=' ')
            Node=Node.next
def reverseandMerge(a,b):
    if a==None and b==None:
        return
    res=None
    while a!=None and b!=None:
        if(a.data<=b.data):
            new_node=a.next
            a.next=res
            res=a
            a=new_node
        else:
            new_node=b.next
            b.next=res
            res=b
            b=new_node
    while (a!=None):
        new_node=a.next
        a.next=res
        res=a
        a=new_node
    while (b!=None):
        new_node=a.next
        b.next=res
        res=b
        b=temp
    return res

    
            

a=None
b=None
a=push(5)
a.next=push(6)
a.next.next=push(7)
b=push(1)
b.next=push(2)
b.next.next=push(3)
print('1st Linked List: ')
printList(a)
print('\n2nd Linked List: ')
printList(b)
print('\n After reverse and Merge')
res=reverseandMerge(a,b)
printList(res)
