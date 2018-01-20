from count_set import Set
import pickle
import MyAlgo


with open("outfile","rb") as f:
    l = pickle.load(f)

#l = [[1,2,3],[2,3,4],[4,5,6]]
l = MyAlgo.findGroups(l[0])
for s in l:
    print(s._elements)
    print(s._count)
