from collections import defaultdict, Counter
with open("input") as file:
    rows = [line.rstrip().split("-") for line in file.readlines()]

graph = defaultdict(list)
for x, y in rows:
    graph[x].append(y)
    graph[y].append(x)

print(graph)


def is_valid_path(past, next, mode='a'):
    if next in ['start'] or 'end' in past:
        return False
    elif next.isupper() or next not in past:
        return True
    elif mode == 'b':
        p2 = [x for x in past if x.islower() and x != 'start']
        c = Counter(p2)
        try:
            if max(c.values()) < 2:
                return True
            elif c[next] < 1 and max(c.values()) == 2:
                return True
        except:
            return False
        return False


def find_all_paths(start_node, visited):
    vis2 = visited.copy()
    if start_node == 'end':
        return [[start_node]]
    else:
        paths = []
        vis2.append(start_node)
        for start_child in graph[start_node]:
            if is_valid_path(visited, start_child, mode='b'):
                child_paths = find_all_paths(start_child, vis2)
                for path in child_paths:
                    path.insert(0, start_node)
                    paths.append(path)
        return paths


all_paths = find_all_paths('start', [])
print(*[",".join(path) for path in all_paths], sep='\n')
all_paths.sort()
print(len(all_paths))

# A: 2707
count = 0
for path in all_paths:
    c = Counter(path)
    tot = sum([1 for k, v in c.items() if v > 1 and k.islower()])
    if tot < 2:
        count += 1

print(count)


