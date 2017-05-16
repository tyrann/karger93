import sys

from random import shuffle
from collections import defaultdict

class UFNode:
    def __init__(self, _id):
        self.id = _id
        self.parent = self
        self.rank = 0

    def __repr__(self):
        return "UF({},{},{})".format(self.id, find(self).id, self.rank)

def find(uf):
    if uf.parent is not uf:
        uf.parent = find(uf.parent)

    return uf.parent

def union(uf1, uf2):
    root1 = find(uf1)
    root2 = find(uf2)

    if root1 is not root2:
        if root1.rank < root2.rank:
            root1.parent = root2
        elif root1.rank > root2.rank:
            root2.parent = root1
        else:
            root2.parent = root1
            root1.rank += 1

def karger(edges, vertices_count):
    vertices_list = [UFNode(i) for i in range(1, vertices_count + 1)]

    v_len = vertices_count

    shuffle(edges)

    i = 0

    while v_len > 2:
        random_edge = edges[i]
        root1 = find(vertices_list[random_edge[0] - 1])
        root2 = find(vertices_list[random_edge[1] - 1])

        if root1 is not root2:
            union(root1, root2)
            v_len -= 1

        i += 1

    return (vertices_list)

def sets_and_cut_len(edges, cut_tree):
    '''From a cut_tree constructed by union-find,
    return the length of the cut, and the two disjoint
    sets of vertices'''
    cut_l = 0

    cut_dict = defaultdict(set)

    for edge in edges:
        root1 = find(cut_tree[edge[0] - 1])
        root2 = find(cut_tree[edge[1] - 1])
        cut_dict[root1.id].add(edge[0])
        cut_dict[root2.id].add(edge[1])

        if root1 is not root2:
            cut_l += 1

    set1, set2 = list(cut_dict.values())

    return cut_l, set1, set2

def cut_in(set1, set2, cuts):
    '''Returns True if cut in already in the list of cuts'''

    for cut2 in cuts:
        if set1 == cut2[0] or set1 == cut2[1]:
            return True

    return False

if __name__ == "__main__":
    vertices_count, edge_count = next(sys.stdin).split()
    vertices_count, edge_count = int(vertices_count), int(edge_count)

    edges  = [tuple(line.split()) for line in sys.stdin]
    edges = [(int(v1), int(v2)) for v1, v2 in edges]

    min_cuts = []
    min_cut_len = vertices_count

    # dict with default value to 0
    cut_len_dict = defaultdict(int)
    for i in range(15500):
        cut_tree = karger(edges[:], vertices_count)

        cut_l, set1, set2 = sets_and_cut_len(edges, cut_tree)

        if cut_l < min_cut_len:
            min_cuts = [(set1, set2)]
            min_cut_len = cut_l
        elif cut_l == min_cut_len and not cut_in(set1, set2, min_cuts):
            min_cuts.append((set1, set2))

    print(min_cut_len, len(min_cuts))
