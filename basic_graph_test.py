import unittest
import basic_graph


class BasicGraphTest(unittest.TestCase):
    def test_node(self):
        self.assertEqual('abcd', basic_graph.Node('abcd').id())
        self.assertEqual(None, basic_graph.Node(None).id())

    def test_edge(self):
        edge = basic_graph.Edge(basic_graph.Node(1), basic_graph.Node(2))
        expected_pair = [basic_graph.Node(1), basic_graph.Node(2)]
        self.assertEqual(expected_pair, edge.nodes())

    def test_graph(self):
        edge1 = basic_graph.Edge(basic_graph.Node(1), basic_graph.Node(2))
        edge2 = basic_graph.Edge(basic_graph.Node(2), basic_graph.Node(1))

        nodes = [basic_graph.Node(3), basic_graph.Node(2), basic_graph.Node(1),
                 basic_graph.Node(2)]

        graph = basic_graph.Graph(nodes, [edge2, edge1])
        expected_nodes = set([basic_graph.Node(1), basic_graph.Node(2),
                              basic_graph.Node(3)])
        self.assertEqual(expected_nodes, graph.nodes())
        self.assertEqual(3, len(graph.nodes()))

        expected_edges = set([edge1, edge2])
        self.assertEqual(expected_edges, graph.edges())
        self.assertEqual(2, len(graph.edges()))

    def test_factory(self):
        factory = basic_graph.Factory()
        node = factory.create_node(1)
        edge = factory.create_edge(node, node)
        graph = factory.create_graph([node, node], [edge, edge])

        self.assertIsInstance(node, basic_graph.Node)
        self.assertIsInstance(edge, basic_graph.Edge)
        self.assertIsInstance(graph, basic_graph.Graph)
        self.assertEqual(1, node.id())
        self.assertEqual([node, node], edge.nodes())
        self.assertEqual([node], list(graph.nodes()))
        self.assertEqual([edge], list(graph.edges()))


if __name__ == '__main__':
    unittest.main()
