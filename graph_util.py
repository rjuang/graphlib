def adjacency_matrix(graph, order=None):
    """Construct an adjacency matrix from a given graph.

    :param graph: a graph_types.GraphType to construct adjacency matrix from.
    :param order: array of node ids containing order of adjacency matrix. If
    None, the order is constructed by sorting graph.nodes().
    :return: an array of arrays containing 0's and 1's where a[i][j] is 1 if
    an edge exists from node i to node j. Each row and column corresponds
    to a node where the nodes are sorted by node id in ascending order.
    """
    if order is None:
        order = [n.id() for n in sorted(graph.nodes())]

        # Initialize result adjacency matrix.
    result = [[0]*len(order) for _ in xrange(len(order))]
    index_map = {node_id: index
                 for index, node_id in enumerate(order)}

    for e in graph.edges():
        nodes = e.nodes()
        i = index_map[nodes[0].id()]
        j = index_map[nodes[-1].id()]
        result[i][j] = 1

    return result


def parents(graph, node_id):
    """Returns the parents of the node in the graph.

    :param graph: a graph_types.GraphType the node is in.
    :param node_id: id value of the node to get parents of.
    :return: an array of ids corresponding to the parents of the node.
    """
    result = set()
    for e in graph.edges():
        nodes = e.nodes()
        if nodes[-1].id() == node_id:
            result.add(nodes[0].id())
    return list(result)


def children(graph, node_id):
    """Returns the children of the node in the graph.

    :param graph: a graph_types.GraphType the node is in.
    :param node_id: id of the node to get children of.
    :return: an array of ids corresponding to the children of the node.
    """
    result = set()
    for e in graph.edges():
        nodes = e.nodes()
        if nodes[0].id() == node_id:
            result.add(nodes[-1].id())
    return list(result)


def markov_blanket(graph, node_id):
    """Returns the Markov blanket of a node.

    The Markov blanket of a node is defined as the node's parents, children,
    and parents of children. The node itself is excluded.

    :param graph: a graph_types.GraphType to fetch the markov blanket from.
    :param node_id: id of node to get Markov blanket of.
    :return: an array of nodes representing the Markov blanket of the specified
    node in the graph.
    """
    child_nodes = children(graph, node_id)

    # Add children.
    results = set(child_nodes)

    # Add parents of children.
    for c in child_nodes:
        if c == node_id:
            continue
        results = results.union(parents(graph, c))

    # Add parents.
    results = results.union(parents(graph, node_id))

    # Exclude self.
    results.discard(node_id)

    return list(results)


def neighbor_map(graph, directed=True):
    """Construct and return dictionary mapping nodes to a list of its neighbors.

    :param graph: a graph_types.GraphType to fetch neighbors from.
    :param directed: optional argument (default True) that specifies whether
    edges should be treated as directed or bi-directional.
    :return: a dictionary mapping a node id to a list of neighboring node ids.
    """
    result = {}
    for e in graph.edges():
        nodes = e.nodes()

        from_id = nodes[0].id()
        to_id = nodes[-1].id()

        edges = [(from_id, to_id)]
        if not directed and from_id != to_id:
            edges.append((to_id, from_id))

        for node_id, neighbor_id in edges:
            if node_id not in result:
                result[node_id] = []
            result[node_id].append(neighbor_id)
    return result


def is_connected(graph, start_id, end_id, directed=True):
    """Returns True if a path exists between the start and end node ids.

    :param graph: a graph_types.GraphType containing information about the
    graph.
    :param start_id: starting node id.
    :param end_id: ending node id.
    :param directed: optional argument (default True) that specifies whether
    edges should be treated as directed or bi-directional.

    :return: True if a path exists between start_id and end_id in the graph.
    """
    neighbors = neighbor_map(graph, directed=directed)
    id_queue = [start_id]
    visited = {}
    while id_queue:
        node_id = id_queue.pop()
        if node_id in visited:
            continue
        visited[node_id] = True

        if node_id not in neighbors:
            continue

        if end_id in neighbors[node_id]:
            return True
        id_queue.extend(neighbors[node_id])

    return False