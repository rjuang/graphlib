"""Interface for various graph structures."""

class NodeType(object):
  """Represents the node of a graph."""

  def id(self):
    """Returns the node label."""
    raise NotImplementedError('get_label not implemented.')

  def __eq__(self, other):
    return self.id() == other.id()

  def __repr__(self):
    return '[%s: id=%s]' % (self.__class__.__name__, self.id())

  def __lt__(self, other):
    return self.id() < other.id()

  def __hash__(self):
    return self.id().__hash__()


class EdgeType(object):
  """Represents the edge of a graph."""

  def nodes(self):
    """Returns the pair (start_node, end_node) representing the edge."""
    raise NotImplementedError('get not implemented.')

  def __eq__(self, other):
    return self.nodes() == other.nodes()

  def __repr__(self):
    chain_str = '->'.join([str(n.id()) for n in self.nodes()])
    return '[%s: %s]' % (self.__class__.__name__, chain_str)

  def __lt__(self, other):
    other_nodes = other.nodes()
    for i, n in enumerate(self.nodes()):
      if i >= len(other_nodes):
        return False

      if n < other_nodes[i]:
        return True

      if n.id() != other_nodes[i].id():
        return False

    # Everything was equal to other. Check if subset.
    return len(self.nodes()) < len(other_nodes)

  def __hash__(self):
    key = [n.id() for n in self.nodes()]
    return str(key).__hash__()


class GraphType(object):
  """Interface for a graph which is a collection of nodes and edges."""

  def nodes(self):
    """Returns the nodes associated with this graph."""
    raise NotImplementedError('nodes not implemented.')

  def edges(self):
    """Returns the edges associated with this graph."""
    raise NotImplementedError('edges not implemented.')

  def __repr__(self):
    nodes = [n.id() for n in self.nodes()]
    edge_nodes = [e.nodes() for e in self.edges()]
    edges = ['->'.join([n.id() for n in l])
             for l in edge_nodes]

    return '[%s: Nodes={%s}, Edges={%s}]' % (
      self.__class__.__name__,
      ','.join(sorted(nodes)),
      ','.join(sorted(edges)))

  def __eq__(self, other):
    return (sorted(self.nodes()) == sorted(other.nodes()) and
            sorted(self.edges()) == sorted(other.edges()))


class FactoryType(object):
  """Interface for a graph factory for components of a graph."""
  def create_node(self, id):
    """Create a node with the specified id.
    :param id: id of node.
    :return: node instance associated with the specified id
    """
    raise NotImplementedError('create_node not implemented')

  def create_edge(self, start_node, end_node):
    """Create an edge with the specified start and end nodes.
    :param start_node: starting node of edge.
    :param end_node: ending node of edge.
    :return: edge instance linking the specified start and end nodes.
    """
    raise NotImplementedError('create_edge not implemented')

  def create_graph(self, nodes, edges):
    """Create a graph with the specified nodes and edges.
    :param nodes: set of nodes in graph.
    :param edges: set of edges in graph.
    :return: graph instance with the specified nodes and edges.
    """
    raise NotImplementedError('create_graph not implemented')


class BuilderType(object):
  """Interface for a graph builder."""

  def node(self, id):
    """Returns node associated with the specified id.

    If no such instance exists, constructs one before returning.
    :param id: id of node to construct.
    :return: node associated with specified id.
    """
    raise NotImplementedError('node not implemented.')

  def edge(self, start_node_id, end_node_id):
    """Returns edge connecting start_node_id to end_node_id.

    If no such instance exists, constructs one before returning.
    :param start_node_id: id of starting node of edge.
    :param end_node_id: id of ending node of edge.
    :return: edge associated with start_node_id, end_node_id.
    """
    raise NotImplementedError('node not implemented.')

  def build(self):
    """Construct the graph and return constructed graph."""
    raise NotImplementedError('not not implemented.')
