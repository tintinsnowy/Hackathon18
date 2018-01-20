from count_set import Set
import pickle
import MyAlgo
import json


with open("outfile","rb") as f:
    l = pickle.load(f)

#l = [[1,2,3],[2,3,4],[4,5,6]]
l = MyAlgo.findGroups(l[0])
list = list()
for s in l:
    #print(s._elements)
    #print(s._count)
    string_rep = str(s._elements) + ", " + str(s._count)
    #print(string_rep)
    list.append(string_rep)


json_string = json.dumps(list)
print(json_string)