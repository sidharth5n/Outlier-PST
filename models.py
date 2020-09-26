import time
from utils import show

class Node:

    def __init__(self, key = None):
        """Each node consists of a data/key, count of the occurrences of the data/key
        pointer to the first child, pointer to an adjacent sibling"""
        self.data = key
        self.count = 1
        self.child = None
        self.next = None
        self.prob = 0

    def incrementCount(self):
        """Increments the count of the data or key associated with the node"""
        self.count += 1

    def setChild(self, child):
        """Set the child pointer to the first child"""
        self.child = child

    def setNext(self, sibling):
        """Sets the next pointer to the next sibling"""
        self.next = sibling
    
    def setProb(self, )

    def getData(self):
        """Returns the data or key associated with the node"""
        return(self.data)

    def getCount(self):
        """Returns the count of the data or key associated with the node"""
        return(self.count)

    def getChild(self):
        """Returns the first child of the node"""
        return(self.child)

    def getNext(self):
        """Returns the adjacent sibling of the node"""
        return(self.next)

class PST:

    def __init__(self):
        """Initialize tree with empty root node"""
        self.root = Node()

    def find(self, current, key):
        """Finds the node with the given key"""
        while current != None:
            if current.getData() == key:
                return current
            current = current.getNext()
        return current

    def fit(self, data, size):
        """ Build a tree on the given data
        
        Parameters
        ----------
        data : List or str
               Data to be fit
        size : int
               Maximum depth of tree or length of buffer
        """
        
        # Check input data types
        if not (isinstance(data, list) or isinstance(data, str)):
            raise Exception("Data should be string or list, but given {}".format(type(data)))
        elif not isinstance(size, int):
            raise Exception("Buffer size should be an integer, but given {}".format(type(size)))
        # Fit PST on the data
        else:
            start = time.time()
            for i in range(len(data)):
                # Fill buffer
                S = data[i:i+size]
                parent = self.root
                for j in range(len(S)):
                    # get children
                    current = parent.getChild()
                    # find node corresponding to given data
                    temp = self.find(current, S[j])
                    # if node exists, increment its count
                    if temp != None:
                        temp.incrementCount()
                    # node does not exist, create one
                    else:
                        temp = Node(S[j])
                        temp.setNext(current)
                        parent.setChild(temp)
                    parent = temp
            print("Fit complete in {:0.4f} s".format(time.time() - start))
                
                
        