# IO.py provide Interface to access files. e.g ".node" file.
import numpy as np

class RAWReader(object):
    def __init__(self):
        self.SlicedString = []
    # Initialize
    def open(self, Filename):
        try:
            f = open(Filename, 'r')
        except:
            print('Warning: RAWReader readfile "'+Filename+'" not exist.')
        self.SlicedString = (f.read()).split()
        f.close()
    # Translate file to splited list
    def pop(self):
        if len(self.SlicedString) > 0:
            return self.SlicedString.pop(0)
        else:
            return None
    # Mock C++ >> operator
# A reader mock C++ style

class RAWWriter(object):
    def __init__(self):
        self.SlicedString = []
    # Initialize
    def write(self, Filename):
        f = open(Filename, 'w')
        for word in self.SlicedString:
            f.write(str(word)+" ")
        f.close()
        self.SlicedString = []
    # Translate file to splited list
    def append(self, Word):
        self.SlicedString.append(Word)
    # Mock C++ << operator
    def newline(self):
        self.SlicedString.append('\n')
    # Add a new line
# A writer mock C++ style

def getAMatrix(MyRAWReader):
    rowsize = int(MyRAWReader.pop())
    colsize = int(MyRAWReader.pop())
    ANSER = np.zeros(shape=(rowsize, colsize))
    for row in range(0, rowsize):
        rowlist = []
        for col in range(0, colsize):
            rowlist.append(float(MyRAWReader.pop()))
        ANSER[row] = rowlist
    return ANSER
    # Get one numpy matrix by RAWReader

def writeAMatrix(Matrix, MyRAWWriter):
    rowsize = len(Matrix)
    colsize = len(Matrix[0])
    MyRAWWriter.append(rowsize)
    MyRAWWriter.append(colsize)
    MyRAWWriter.newline()
    for row in range(0, rowsize):
        rowlist = Matrix[row]
        for colelement in Matrix[row]:
            MyRAWWriter.append(colelement)
        MyRAWWriter.newline()
    # Write one numpy matrix by RAWReader