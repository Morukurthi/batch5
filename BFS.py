def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:  #creating loop to visit
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,graph,'5')      #function call

