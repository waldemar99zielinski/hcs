import sys
from collections import defaultdict

OPERATION = 0
TRANSACTION = 1
RESOURCE = 2

READ = "r"
WRITE = "w"

history_string_array = sys.argv[1:]

history = []

temp_transaction = defaultdict(list)

# input validation
for i, value in enumerate(history_string_array, start=0):
    if i % 3 == OPERATION:
        temp_transaction = []
        if value != READ and value != WRITE:
            sys.exit("invalid input operation should be either r or w")
        temp_transaction.append(value)
    if i % 3 == TRANSACTION:
        if type(int(value)) != int:
            sys.exit("invalid input transaction should be an int")
        temp_transaction.append(value)
    if i % 3 == RESOURCE:
        temp_transaction.append(value)
        history.append(temp_transaction)

# conflict graph creation - contains conflicting operation between each transaction
# conflict is present only if two different transactions are preformig operation on the same resource and at least one of them is a read
graph = defaultdict(set)
transactions = set()

for i in range(len(history)):
    transactions.add(history[i][TRANSACTION])
    for j in range(i + 1, len(history)):
        if history[i][RESOURCE] != history[j][RESOURCE]:
            continue
        if history[i][TRANSACTION] == history[j][TRANSACTION]:
            continue
        if history[i][OPERATION] == READ and history[j][OPERATION] == READ:
            continue
        graph[history[i][TRANSACTION]].add(history[j][TRANSACTION])

# use DFS algorithm to traverse graph and detect cycle
def is_cyclic_rec(graph, vertex, visited, current_path_visited):
    if vertex not in graph:
        return False

    # mark current vertex as visited
    # and add it to current path
    visited[vertex] = True
    current_path_visited[vertex] = True

    # for each conflict to current transacion
    # check its conflicts
    # current_path_visited then graph is cyclic
    for conflict in graph[vertex]:
        if visited[conflict] == False:
            if is_cyclic_rec(graph, conflict, visited, current_path_visited) == True:
                return True
        elif current_path_visited[conflict] == True:
            return True

    # after recursive search of current vertex paths
    # at this point it is not cyclic
    # and can be removed from the current path
    current_path_visited[vertex] = False
    return False

# keep track of current path and visited overall
visited = dict.fromkeys(transactions, False)
current_path_visited = dict.fromkeys(transactions, False)

# only if graph is acyclic history is conflict serializable
for vertex in graph:
    if visited[vertex] == False:
        if is_cyclic_rec(graph, vertex, visited, current_path_visited) == True:
            print("false")
            sys.exit(0)
print("true")