class Node: 
    # Smiður, frumstillir d og núllstillir bendana prv og nxt
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # Endurkvæmt fall sem bætir aftast á listann.   
    def append(self,d):
        if self.nxt is None:
            data = Node(d)
            self.nxt = data
            data.prv = self
        else:
            self.nxt.append(d)

    # Endurkvæmt fall sem prentar listann.
    def printList(self):
        if self.nxt is None:
            print(self.data, end=" ")
        else:
            print(self.data, end=" ")
            self.nxt.printList()
                 
    # Endurkvæmt fall sem athuga hvort stak d er í listanum.
    def find(self, d):
        if self.nxt is None:
            if self.data == d:
                return True
            else:
                return False
        elif self.data == d:
                return True
        else:
            return self.nxt.find(d)

    # Endurkvæmt fall sem eyðir staki d úr listanum.
    def delete(self, d):
        if self.nxt is None:
            if self.data == d:
                self.prv.nxt = None
                self.prv = None
                return True
            else:
                return False
        if self.data == d:
            self.prv.nxt = self.nxt
            self.nxt.prv = self.prv
            return True
        else:
            return self.nxt.delete(d)



class DLL:
    # Smiður, núllstillir Haus listans
    def __init__(self):
        self.head = None

    # Bætir við fremst á listann, hnúturinn verður Head -> förum ekki í Node klasann.
    def push(self,d):
        if self.head is None:
            data = Node(d)
            self.head = data
        else:
            data = Node(d)
            self.head.prv = data
            data.nxt = self.head
            self.head = data
    
    # Bætir við aftast á listann -> kallar á endurkvæmnt fall í Node.
    def append(self, d):
        if self.head is None:
            self.head = Node(d)
        else:
            self.head.append(d)

    # Prentar listann allan á skjá -> kallar á endurkvæmt fall í Node.
    def printList(self):
        if self.head is None:
            print("Empty")
        else:
            self.head.printList()
    
    # Finnur stak d í ef til -> kallar á endurkvæmnt fall í Node.
    def find(self, d):
        if self.head is None:
            return False
        else:
            return self.head.find(d)

    # Eyðir staki d úr lista ef til -> kallar á endurkvæmnt fall í Node.
    def delete(self, d):
        if self.head is None:
            return False
        elif self.head.data == d:
            self.head = self.head.nxt
            self.head.prv.nxt = None
            self.head.prv = None
            return True
        else:
            return self.head.delete(d)

# Keyrslurútína
dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7         
dbl.push(1)             # 1 5 7 
dbl.push(0)             # 0 1 5 7 
dbl.append(10)          # 0 1 5 7 10
dbl.printList()         
print()
print(dbl.delete(5))   # 0 1 7 10
dbl.printList() 
print()
print(dbl.find(5))      # False
print(dbl.find(7))      # True
