"""Defines a basic graph with simple components."""
import graph_types

class Node(graph_types.NodeType):

  def __init__(self, id):
    self._id = id
    self._data = None

  # @Override
  def id(self):
    return self._id


class Edge(graph_types.EdgeType):

  def __init__(self, start_node, end_node):
    self._start = start_node
    self._end = end_node

  # @Override
  def nodes(self):
    return [self._start, self._end]


class Graph(graph_types.GraphType):

  def __init__(self, nodes, edges):
    self._nodes = set(nodes)
    self._edges = set(edges)

  # @Override
  def nodes(self):
    return self._nodes

  # @Override
  def edges(self):
    return self._edges


class Factory(graph_types.FactoryType):

  # @Override
  def create_node(self, id):
    return Node(id)

  # @Override
  def create_edge(self, start_node, end_node):
    return Edge(start_node, end_node)

  # @Override
  def create_graph(self, nodes, edges):
    return Graph(nodes, edges)