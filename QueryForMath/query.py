count = 0
p1 = []
p2 = []
Answer = []

class MyQuery:

    def __init__(self, p1, p2, check):
        self.p1 = p1
        self.p2 = p2
        self.check = check
        print('Object was created')

    def docID(self, p1):
        # if p1.size(
        # p1 = p1[count]
        # print(len(p1))
        pass

    def Intersect(self):
        positionP1 = 0
        positionP2 = 0
        while positionP1 < len(p1) and positionP2 < len(p2):
            if p1[positionP1] == p2[positionP2]:
                Answer.append(p1[positionP1])
                positionP1 += 1
                positionP2 += 1
            elif p1[positionP1] < p2[positionP2]:
                positionP1 += 1
            else: positionP2 += 1
        print("Output of Intersection Query = ", Answer)

    def Union(self):
        positionP1 = 0
        positionP2 = 0
        checkFullP1 = 0
        checkFullP2 = 0
        checkAdd = 0
        while positionP1 < len(p1) and positionP2 < len(p2):
            if p1[positionP1] == p2[positionP2]:
                Answer.append(p1[positionP1])
                positionP1 += 1
                positionP2 += 1
            elif p1[positionP1] < p2[positionP2]:
                Answer.append(p1[positionP1])
                positionP1 += 1
            elif p1[positionP1] > p2[positionP2] and checkFullP1 == 0:
                    checkAdd = 0
                    for i in range(len(Answer)):
                        if p2[positionP2] == Answer[i]:
                            checkAdd += 1
                    if checkAdd == 0 :
                        Answer.append(p2[positionP2])
                    else:
                        positionP2 += 1
            if positionP2 == len(p2):
                positionP2 -= 1

            if p1[positionP1] >= p2[positionP2] and checkFullP2 == 1:
                Answer.append(p1[positionP1])
                positionP1 += 1
            if positionP2 == len(p2) - 1:
                checkFullP2 = 1
                positionP2 = len(p2)-1
            if positionP1 == len(p1) - 1:
                checkFullP1 = 1
                positionP1 = len(p1)-1
        print("Output from Union Query = ",Answer)

    def Not(self,p2,p1):
        positionP1 = 0
        positionP2 = 0
        while positionP1 < len(p1) and positionP2 < len(p2):
            if p1[positionP1] == p2[positionP2]:
                positionP1 += 1
                positionP2 += 1
            elif p1[positionP1] > p2[positionP2]:
                positionP2 += 1
            elif p1[positionP1] < p2[positionP2]:
                Answer.append(p1[positionP1])
                positionP1 += 1
        print("Output of Not Query(p2-p1) = ", Answer)


p1.append(1)
p1.append(2)
p1.append(3)
p1.append(4)
p1.append(13)
p1.append(16)
p1.append(21)
p1.append(32)
p1.append(34)
p1.append(60)
p1.append(61)
p1.append(64)
p1.append(65)
p1.append(66)
p1.append(69)

p1.append(128)
p1.append(129)
p1.append(130)

p2.append(1)
p2.append(2)
p2.append(3)
p2.append(5)
p2.append(8)
p2.append(13)
p2.append(21)
p2.append(34)
p2.append(35)
p2.append(36)
p2.append(37)
p2.append(38)
p2.append(39)
p2.append(40)
p2.append(41)
p2.append(42)
p2.append(43)
p2.append(44)
p2.append(60)
p2.append(62)
p2.append(66)
p2.append(129)
#
# for i in range (len(p2)):
#       if p2[i] == 1:
#         print("Test")


Aom = MyQuery(p2, p1, True)
# Aom.docID(p1)
# Aom.docID(p2)
# try:
#     print(Aom.p1[9])
# except IndexError:
#     print("Error")
# print(Aom.p1[9])
print("P1 = ",p1)
print("P2 = ",p2)
Aom.Intersect()
Answer = []
Aom.Union()
Answer = []
Aom.Not(p1,p2)

# print(Aom.p1[3])
# print(Aom.p1)
# print(Aom.p2)
