class Node:
  def __init__(self):
    self.data = None
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def addNode(self, data):
    curr = self.head
    if curr is None:
      n = Node()
      n.data = data
      self.head = n
      return

    if curr.data > data:
      n = Node()
      n.data = data
      n.next = curr
      self.head = n
      return

    while curr.next is not None:
      if curr.next.data > data:
        break
      curr = curr.next
    n = Node()
    n.data = data
    n.next = curr.next
    curr.next = n
    return
  def duplicate(self):
        curr=self.head
        if curr==None:
            return
        else:
            while curr.next!=None:
                if curr.data==curr.next.data:
                    new=curr.next.next
                    curr.next = None
                    curr.next = new 
                else: 
                    curr = curr.next
            return self.head
  def __str__(self):
    data = []
    curr = self.head
    while curr is not None:
      data.append(curr.data)
      curr = curr.next
    return "[%s]" %(', '.join(str(i) for i in data))

  # def __repr__(self):
  #   return self.__str__()

ll = LinkedList()
num = int(input("Enter a number: "))
while num != -1:
  ll.addNode(num)
  num = int(input("Enter a number: "))
ll.duplicate()
c = ll.head
while c is not None:
    print(c.data,end=' ')
    c = c.next