import csv
import timeit

class Graph:
    def __init__(self):
        pass

    def read(self, v):
        self.data = v
        self.size = len(v)

    def findmin(self, E):
        val = E[0]
        for i in range(len(E)):
            if val[2] > E[i][2]:
                val = E[i]
            return val

    def process(self):
        T = [False] * self.size
        L = []
        E = []
        j=0
        k=0

        for i in range(self.size):
            if i == 0:
                T[i] = True
            else:
                for j in range(len(T)):
                    for k in range(j, len(T)):
                        if T[j] != T[k]:
                            E.append([j, k, self.data[j][k]])
                targetEdge = self.findmin(E)
                L.append(targetEdge)
                T[targetEdge[0]] = True
                T[targetEdge[1]] = True
                E = []

        print(L)
        length = 0
        for ele in L:
            length = length + ele[2]
        print("Minimum Spanning Tree length is: ", length)


v=[]
with open('graph.csv', 'r', newline='') as file:
    myreader = csv.reader(file, delimiter=',')
    for rows in myreader:
        r=[]
        for i in rows:
            r.append(int(i))
        v.append(r)
g=Graph()
g.read(v)
g.process()
print(timeit.Timer(g.process).timeit(number=1))