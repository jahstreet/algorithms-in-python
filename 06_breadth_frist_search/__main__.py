from collections import deque


def bfs(connections_graph: dict, name: str):
    checked = set(name)
    queue = deque()
    queue += connections_graph[name]
    while len(queue) > 0:
        candidate = queue.popleft()
        if candidate not in checked:
            if sells_mango(candidate):
                return candidate
            checked.add(candidate)
            if connections_graph.get(candidate):
                queue += connections_graph[candidate]
    return None


def sells_mango(name: str):
    return name[-1] == "m"


if __name__ == '__main__':
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    print(bfs(graph, "you"))  # thom
