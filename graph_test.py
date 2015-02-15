import unittest
import basic_graph
import graph


class TestGraph(unittest.TestCase):
    def test_graph_Builder(self):
        # TODO(radford): Add test cases for builder.
        pass

    def test_graph_from_string(self):
        factory = basic_graph.Factory()
        g1 = graph.from_string(factory, "A->B, B->C, C->D, D->B")

        # Construct expected values.
        expected_node_list = ['A', 'B', 'C', 'D']
        expected_edge_list = [['A', 'B'],
                              ['B', 'C'],
                              ['C', 'D'],
                              ['D', 'B']]

        nodes = [n.id() for n in g1.nodes()]
        edges = [[n.id() for n in e.nodes()] for e in g1.edges()]

        self.assertEqual(sorted(expected_node_list), sorted(nodes))
        self.assertEqual(sorted(expected_edge_list), sorted(edges))

        g2 = graph.from_string(factory, " A->B-> C -> D->B, E, F ")
        expected_node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        expected_edge_list = [['A', 'B'],
                              ['B', 'C'],
                              ['C', 'D'],
                              ['D', 'B']]

        nodes = [n.id() for n in g2.nodes()]
        edges = [[n.id() for n in e.nodes()] for e in g2.edges()]

        self.assertEqual(sorted(expected_node_list), sorted(nodes))
        self.assertEqual(sorted(expected_edge_list), sorted(edges))


if __name__ == '__main__':
    unittest.main()
