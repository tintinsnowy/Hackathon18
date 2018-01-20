import queue
from count_set import Set
import pickle

def findGroups(tagsList):
    if len(tagsList)==0:
        return []

    q = queue.Queue()
    q.put(Set(set(tagsList[0])))

    for i in range(1, len(tagsList)):
        s1 = Set(set(tagsList[i]))
        if s1.isEmpty():
            continue

        queueLength = q.qsize()
        for j in range(queueLength):
            s2 = q.get()
            sNew = s1.intersect_update(s2)
            if not s2.isEmpty():
                q.put(s2)
            if not sNew.isEmpty():
                q.put(sNew)
            if s1.isEmpty():
                break
        q.put(s1)

    return list(q.queue)


with open("outfile","rb") as f:
    l = pickle.load(f)

#l = [[1,2,3],[2,3,4],[4,5,6]]
l = findGroups(l[0])
for s in l:
    print(s._elements)
    print(s._count)
