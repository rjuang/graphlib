import basic_graph
import graph
import graph_util
import unittest

class GraphUtilTest(unittest.TestCase):

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

if __name__ == '__main__':
  unittest.main()
