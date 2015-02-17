import graph_types
import unittest


# Test classes for testing abstract class members.
class TestNode(graph_types.NodeType):

    def __init__(self, node_id):
        self._id = node_id

    def id(self):
        return self._id


class TestEdge(graph_types.EdgeType):

    def __init__(self, nodes):
        self._nodes = nodes

    def nodes(self):
        return self._nodes


class TestGraph(graph_types.GraphType):
    def __init__(self, nodes, edges):
        self._nodes = nodes
        self._edges = edges

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges


class GraphTypesTest(unittest.TestCase):

    def test_NodeType(self):
        node_1 = TestNode(1)
        node_2 = TestNode(2)
        node_3 = TestNode(1)

        # Test __eq__
        self.assertEqual(node_1, node_1)
        self.assertEqual(node_1, node_3)
        self.assertEqual(node_3, node_1)
        self.assertNotEqual(node_1, node_2)

        # Test __lt__
        self.assertLess(node_1, node_2)
        self.assertTrue(node_1 < node_2)
        self.assertFalse(node_2 < node_1)
        self.assertFalse(node_1 < node_1)
        self.assertFalse(node_1 < node_3)
        self.assertFalse(node_2 < node_3)

    def test_EdgeType(self):
        edge_1 = TestEdge([TestNode(1), TestNode(2), TestNode(3)])
        edge_2 = TestEdge([TestNode(1), TestNode(2)])
        edge_3 = TestEdge([TestNode(1), TestNode(1)])
        edge_4 = TestEdge([TestNode(1), TestNode(3), TestNode(2)])
        edge_5 = TestEdge([TestNode(1), TestNode(2)])
        edge_6 = TestEdge([TestNode(2), TestNode(1)])

        # Test __eq__
        self.assertEqual(edge_1, edge_1)
        self.assertEqual(edge_2, edge_5)
        self.assertNotEqual(edge_2, edge_6)
        self.assertNotEqual(edge_1, edge_2)

        # Test __lt__
        self.assertLess(edge_2, edge_1)
        self.assertLess(edge_3, edge_2)
        self.assertLess(edge_3, edge_1)
        self.assertLess(edge_1, edge_4)
        self.assertFalse(edge_4 < edge_1)
        self.assertLess(edge_5, edge_6)

    def test_GraphType(self):
        graph_1 = TestGraph([], [])
        graph_1_copy = TestGraph([], [])

        graph_2 = TestGraph([TestNode(i) for i in [1, 2]],
                            [TestEdge([TestNode(i), TestNode(j)])
                             for i, j in [[1, 2], [2, 1]]])
        graph_2_copy = TestGraph([TestNode(i) for i in [1, 2]],
                                 [TestEdge([TestNode(i), TestNode(j)])
                                  for i, j in [[1, 2], [2, 1]]])

        graph_3 = TestGraph([TestNode(i) for i in [1, 2, 3]],
                            [TestEdge([TestNode(i), TestNode(j)])
                             for i, j in [[1, 2], [2, 1]]])

        graph_4 = TestGraph([TestNode(i) for i in [3, 1, 2]],
                            [TestEdge([TestNode(i), TestNode(j)])
                             for i, j in [[2, 1], [1, 2]]])

        self.assertEqual(graph_1, graph_1_copy)
        self.assertEqual(graph_1, graph_1)
        self.assertNotEqual(graph_1, graph_2)
        self.assertEqual(graph_2, graph_2_copy)
        self.assertEqual(graph_2, graph_2)
        self.assertNotEqual(graph_2, graph_3)
        self.assertNotEqual(graph_2, graph_1)

        # Test out of order
        self.assertEqual(graph_3, graph_4)


if __name__ == '__main__':
    unittest.main()
