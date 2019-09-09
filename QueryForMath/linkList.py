Answer = []
class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0
    def CurrentNode(self):
        return self.head
    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


class MyQuery:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        print('Object was created')

    def docID(self, p1):
        # if p1.size(
        # p1 = p1[count]
        # print(len(p1))
        pass

    def Intersect(self,p1):
        print(LinkedList.CurrentNode(p1))
        while self.p1.head is not None and self.p2.head is not None:
            if p1[positionP1] == p2[positionP2]:
                Answer.append(p1[positionP1])
            #     positionP1 += 1
            #     positionP2 += 1
            # elif p1[positionP1] < p2[positionP2]:
            #     positionP1 += 1
            # else:
            #     positionP2 += 1

            # pass


P1 = LinkedList()
print("Inserting P1")
P1.addNode(1)
P1.addNode(2)
P1.addNode(3)

P2 = LinkedList()
print("Inserting P2")
P2.addNode(1)
P2.addNode(2)
P2.addNode(3)

Q = MyQuery(P1,P2)
Q.Intersect(P1)
P1.getSize()