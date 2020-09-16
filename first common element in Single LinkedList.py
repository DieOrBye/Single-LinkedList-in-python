# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:39:16 2020

@author: Souhardya
"""
class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
def push(head_ref, new_data): 
    new_node = Node(new_data) 
    new_node.data = new_data 
    new_node.next = head_ref 
    head_ref = new_node 
    return head_ref  
def firstCommon(head1, head2): 
      
     
    while(head1 != None): 
        p = head2 
  
     
        while(p != None): 
            if (p.data == head1.data): 
                return head1.data 
            p = p.next
        head1 = head1.next
    return 0 
if __name__=='__main__':  
    head1 = None
    head1 = push(head1, 30) 
    head1 = push(head1, 15) 
    head1 = push(head1, 9) 
    head1 = push(head1, 6)
    head1=push(head1,3)
    head2 = None
    head2 = push(head2, 30) 
    head2 = push(head2, 15) 
    head2 = push(head2, 10)
    print(firstCommon(head1, head2))