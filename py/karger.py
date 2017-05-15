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

    while len(vertices_sets) > 2:
        random_edge = choice(edges)

        s1, s2 = sets_that_contains(vertices_sets, random_edge)
        s12 = s1 | s2

        vertices_sets.remove(s1)
        vertices_sets.remove(s2)
        vertices_sets.append(s12)

        # clean self loops
        for edge in edges[:]:
            if edge[0] in s12 and edge[1] in s12:
                edges.remove(edge)

    return (vertices_sets[0], vertices_sets[1])


def cut_len(edges, cut):
    cut_len = 0

    for edge in edges:
        if edge[0] in cut[0] and edge[1] in cut[1] or \
           edge[0] in cut[1] and edge[1] in cut[0]:

           cut_len += 1

    return cut_len



if __name__ == "__main__":
    with open(a2_path) as f:
        vertices_count, edge_count = next(f).split()
        vertices_count, edge_count = int(vertices_count), int(edge_count)

        edges  = [tuple(line.split()) for line in f]
        edges = [(int(v1), int(v2)) for v1, v2 in edges]

        # dict with default value to 0
        cut_len_dict = defaultdict(int)
        for i in range(20000):
            cut = karger(edges[:], vertices_count)
            cut_l = cut_len(edges, cut)
            cut_len_dict[cut_l] += 1

        print(cut_len_dict)
