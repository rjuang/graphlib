def adjacency_matrix(graph, order=None):
  """ Construct an adjacency matrix from a given graph.

  :param graph: a graph_types.GraphType to construct adjacency matrix from.
  :param order: array of node ids containing order of adjacency matrix. If None,
  the order is constructed by sorting graph.nodes().
  :return: an array of arrays containing 0's and 1's where a[i][j] is
  1 if an edge exists from node i to node j. Each row and column corresponds
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