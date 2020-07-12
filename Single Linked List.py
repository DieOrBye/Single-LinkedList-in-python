class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(10)
b=Node(25)
c=Node(65)
print(a)
print(a.next)
print(a.data)
a.next=b #creating referrence to the next node/next pointer is pointing towards b
print("         after implementing b")
print("")
print(b)
print(a)
print(a.next)
b.next=c #creating referrence to the next node/next pointer is pointing towards c
print("")
print("         after implementing c")
print("")
print(c)
print(b)
print(b.next)