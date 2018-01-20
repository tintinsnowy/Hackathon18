class Set:
    _count = 0
    _elements = None

    def __init__(self, elements=set(), count = 1): 
        self._count = count
        self._elements = elements

    def intersect(self, s):
        left = self._elements.copy()
        right = s._elements.copy()
        mid = set() 

        for l in left.copy():
            if len(right) == 0:
                break;

            for r in right.copy():
                if l == r:
                    mid.add(l)
                    left.remove(l)
                    right.remove(r)

        return Set(left,self._count), Set(mid, self._count + s._count), Set(right,self._count)

    def intersect_update(self, s):
        mid = set()

        for l in self._elements.copy():
            if s.isEmpty():
                break;

            for r in s._elements.copy():
                if l == r:
                    mid.add(l)
                    self._elements.remove(l)
                    s._elements.remove(r)

        return Set(mid, self._count + s._count)

    def isEmpty(self):
        return len(self._elements) == 0
