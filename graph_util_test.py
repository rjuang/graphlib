import basic_graph
import graph
import graph_util
import unittest

class GraphUtilTest(unittest.TestCase):

  def assert_maps_equal(self, expected, actual):
    self.assertEqual(len(expected), len(actual), msg='Map length mismatch.')
    for exp_key in expected:
      self.assertTrue(exp_key in actual, msg='Did not find %s in %s' % (
        exp_key, actual))

      exp_value = sorted(expected[exp_key])
      actual_value = sorted(actual[exp_key])

      self.assertEqual(
        exp_value, actual_value ,
        msg='Expected element with key %s to contain %s. Contains %s.' % (
          exp_key, exp_value, actual_value))

  def test_adjacency_matrix(self):
    factory = basic_graph.Factory()
    g = graph.from_string(factory, 'A->A, B->B, C->C, E->E, A->E')
    adj = graph_util.adjacency_matrix(g)

    expected_adj = [
      [1, 0, 0, 1],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ]
    self.assertEqual(expected_adj, adj)

    g = graph.from_string(factory, 'A->B->C->D->E, A->C, A->D')
    adj = graph_util.adjacency_matrix(g)
    expected_adj = [
      [0, 1, 1, 1, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0]
    ]
    self.assertEqual(expected_adj, adj)

  def test_parents(self):
    factory = basic_graph.Factory()
    g = graph.from_string(factory, 'A->A, B->B, C->C, E->E, A->E, F')
    self.assertEqual(['A'], graph_util.parents(g, 'A'))
    self.assertEqual(['A', 'E'], sorted(graph_util.parents(g, 'E')))
    self.assertEqual([], graph_util.parents(g, 'F'))

  def test_children(self):
    factory = basic_graph.Factory()
    g = graph.from_string(factory, 'A->A, B->B, C->C, E->E, A->E, F')
    self.assertEqual(['A', 'E'], sorted(graph_util.children(g, 'A')))
    self.assertEqual(['E'], graph_util.children(g, 'E'))
    self.assertEqual([], graph_util.parents(g, 'F'))

  def test_markov_blanket(self):
    factory = basic_graph.Factory()
    g = graph.from_string(factory, 'A->A, B->B, C->C, E->E, A->E, F->E')
    self.assertEqual(['E', 'F'], sorted(graph_util.markov_blanket(g, 'A')))

    g = graph.from_string(
      factory, 'x1->x8, x1->x4, x2->x4, x3->x4, x4->x5, x4->x6, x7->x6')
    self.assertEqual(['x1', 'x2', 'x3', 'x5', 'x6', 'x7'],
                     sorted(graph_util.markov_blanket(g, 'x4')))

  def test_neighbor_map(self):
    factory = basic_graph.Factory()
    g = graph.from_string(factory, 'A->A, B->B, C->C, E->E, A->E, F->E')
    expected_map = {
      'A': ['A', 'E'],
      'B': ['B'],
      'C': ['C'],
      'E': ['E'],
      'F': ['E'],
    }
    self.assert_maps_equal(expected_map, graph_util.neighbor_map(g))

    expected_map = {
      'A': ['A', 'E'],
      'B': ['B'],
      'C': ['C'],
      'E': ['A', 'E', 'F'],
      'F': ['E'],
    }
    self.assert_maps_equal(expected_map, graph_util.neighbor_map(
      g, directed=False))

  def test_is_connected(self):
    factory = basic_graph.Factory()
    g = graph.from_string(factory, 'A->A, B->E, C->C, E->E, E->C, F->E')
    self.assertTrue(graph_util.is_connected(g, 'A', 'A'))
    self.assertTrue(graph_util.is_connected(g, 'B', 'E'))
    self.assertTrue(graph_util.is_connected(g, 'E', 'C'))
    self.assertTrue(graph_util.is_connected(g, 'F', 'E'))
    self.assertTrue(graph_util.is_connected(g, 'C', 'C'))
    self.assertTrue(graph_util.is_connected(g, 'B', 'C'))
    self.assertTrue(graph_util.is_connected(g, 'F', 'C'))
    self.assertFalse(graph_util.is_connected(g, 'B', 'B'))
    self.assertFalse(graph_util.is_connected(g, 'F', 'F'))
    self.assertFalse(graph_util.is_connected(g, 'C', 'B'))
    self.assertTrue(graph_util.is_connected(g, 'C', 'B', directed=False))


if __name__ == '__main__':
  unittest.main()
