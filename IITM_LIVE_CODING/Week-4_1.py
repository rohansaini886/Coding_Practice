class Indegree:
    def __init__(self):
        self.ind_list = {}
        self.ind_mat = {}
    def Indegree_List(self, d):
        l = self.ind_list
        for i in range(len(d)):
            l[i] = 0
        for i in range(len(d)):
            for j in d[i]:
               l[j] += 1
        return(l)
    def Indegree_Mat(self, d):
        l = self.ind_mat
        for i in range(len(d)):
            l[i] = 0
        for i in range(len(d)):
            for j in range(len(d)):
                if d[j][i] == 1:
                    l[i] += 1
        return(l)
GList=eval(input())
GMat = eval(input())
G = Indegree()
IGL = G.Indegree_List(GList)
IGM = G.Indegree_Mat(GMat)
print('For adjacency list')
for i in range(len(GList)):
    print(i,' = ',IGL[i])
print('For adjacency matrix')
for i in range(len(GMat)):
    print(i,' = ',IGM[i])
