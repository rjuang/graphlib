import graph_types

class Builder(graph_types.BuilderType):
  """Builder for an immutable graph."""

  def __init__(self, factory):
    """Construct a graph builder.

    :param factory: Factory instance to use to build the graph. (e.g.,
      basic_graph.Factory())
    :return: a graph builder for the specified factory type.
    """
    self._factory = factory
    self._nodes = {}
    self._edges = {}

  # @Override
  def node(self, id):
    if id in self._nodes:
      return self._nodes[id]

    node = self._factory.create_node(id)
    self._nodes[id] = node
    return node

  # @Override
  def edge(self, start_node_id, end_node_id):
    key = (start_node_id, end_node_id)
    if key in self._edges:
      return self._edges[key]

    start_node = self.node(start_node_id)
    end_node = self.node(end_node_id)
    edge = self._factory.create_edge(start_node, end_node)
    self._edges[key] = edge
    return edge

  # @Override
  def build(self):
    nodes = self._nodes.values()
    edges = self._edges.values()
    return self._factory.create_graph(nodes, edges)


def from_string(factory, str):
    """Construct a graph from a string specifier.
    "A->B->C, B->C, D -> E, E -> F, G, H"

    :param factory graph factory instance to use to construct graph.
    :param str string describing graph to construct.

    :return: a graph.
    """

    builder = Builder(factory)
    node_sequences = [s.split('->') for s in str.split(",")]

    for seq in node_sequences:
      last_id = None
      for s in seq:
        id = s.strip()
        builder.node(id)
        if last_id is not None:
          builder.edge(last_id, id)
        last_id = id

    return builder.build()
