import sys

from random import choice
from collections import defaultdict


a2_path = "../a2.in"


def sets_that_contains(set_list, edge):
    sets = []

    for vertices_set in set_list:
        if edge[0] in vertices_set or edge[1] in vertices_set:
            sets.append(vertices_set)

    if len(sets) != 2:
        raise ValueError("Impossible state, there should be only 2 sets")

    return sets


def karger(edges, vertices_count):
    vertices_sets = [{i} for i in range(1, vertices_count + 1)]
    set_for_element = {next(iter(s)): s for s in vertices_sets}

    while len(vertices_sets) > 2:
        random_edge = choice(edges)

        s1 = set_for_element[random_edge[0]]
        s2 = set_for_element[random_edge[1]]

        vertices_sets.remove(s1)
        s2.update(s1)

        # update set dict
        for elem in s2:
            set_for_element[elem] = s2

        # clean self loops
        for edge in edges[:]:
            if edge[0] in s2 and edge[1] in s2:
                edges.remove(edge)

    return (vertices_sets[0], vertices_sets[1])


def cut_len(edges, cut):
    cut_len = 0

    for edge in edges:
        if edge[0] in cut[0] and edge[1] in cut[1] or \
           edge[0] in cut[1] and edge[1] in cut[0]:

           cut_len += 1

    return cut_len

def cut_in(cut, cuts):
    '''Returns True if cut in already in the list of cuts'''

    for cut2 in cuts:
        if cut[0] == cut2[0] or cut[0] == cut2[1]:
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
    for i in range(5500):
        cut = karger(edges[:], vertices_count)
        cut_l = cut_len(edges, cut)

        if cut_l < min_cut_len:
            min_cuts = [cut]
            min_cut_len = cut_l
        elif cut_l == min_cut_len and not cut_in(cut, min_cuts):
            min_cuts.append(cut)

    print(min_cut_len, len(min_cuts))
