"""
Base class for undirected graphs.

The Graph class allows any hashable object as a node
and can associate key/value attribute pairs with each undirected edge.

Self-loops are allowed but multiple edges are not (see MultiGraph).

For directed graphs see DiGraph and MultiDiGraph.

This module provides a base class for undirected graphs along with
methods for adding, removing, and querying nodes and edges.

Classes:
- Graph: Base class for undirected graphs.

Example:
    >>> G = Graph()
    >>> G.add_node(1)
    >>> G.add_edge(1, 2)
    >>> G.has_edge(1, 2)
    True
"""
from typing import Any, Iterator

import python_ta


class Graph:
    """A class for representing an undirected graph."""
    nodes: dict
    edges: dict

    def __init__(self) -> None:
        """Initialize the Graph."""
        self.nodes = {}  # Dictionary to store nodes and their attributes
        self.edges = {}  # Dictionary to store edges and their attributes

    def add_node(self, node: Any, **attr: Any) -> None:
        """Add a node to the graph.

        Parameters:
            node: hashable
                The node to add.
            attr: dict, optional
                Node attributes.

        """
        if node not in self.nodes:
            self.nodes[node] = attr

    def remove_node(self, node: Any) -> None:
        """Remove a node from the graph.

        Parameters:
            node: hashable
                The node to remove.

        """
        if node in self.nodes:
            del self.nodes[node]
            for edge in list(self.edges.keys()):
                if node in edge:
                    del self.edges[edge]

    def add_edge(self, u: Any, v: Any, **attr: Any) -> None:
        """Add an edge to the graph.

        Parameters:
            u, v: hashable
                Nodes to connect with the edge.
            attr: dict, optional
                Edge attributes.

        """
        if (u, v) not in self.edges and (v, u) not in self.edges:
            self.edges[(u, v)] = attr

    def remove_edge(self, u: Any, v: Any) -> None:
        """Remove an edge from the graph.

        Parameters:
            u, v: hashable
                Nodes connected by the edge.

        """
        if (u, v) in self.edges:
            del self.edges[(u, v)]
        elif (v, u) in self.edges:
            del self.edges[(v, u)]

    def has_node(self, node: Any) -> bool:
        """Check if the graph contains the given node.

        Parameters:
            node: hashable
                The node to check.

        Returns:
            bool:
                True if the graph contains the node, False otherwise.

        """
        return node in self.nodes

    def has_edge(self, u: Any, v: Any) -> bool:
        """Check if the graph contains the given edge.

        Parameters:
            u, v: hashable
                Nodes connected by the edge.

        Returns:
            bool:
                True if the graph contains the edge, False otherwise.

        """
        return (u, v) in self.edges or (v, u) in self.edges

    def neighbors(self, node: Any) -> set:
        """Get the neighbors of a node.

        Parameters:
            node: hashable
                The node to get neighbors for.

        Returns:
            set:
                A set of neighboring nodes.

        """
        nbrs = set()
        for edge in self.edges:
            if node in edge:
                nbrs.add(edge[0] if edge[1] == node else edge[1])
        return nbrs

    def clear(self) -> None:
        """Remove all nodes and edges from the graph."""
        self.nodes.clear()
        self.edges.clear()

    def clear_edges(self) -> None:
        """Remove all edges from the graph."""
        self.edges.clear()

    def __iter__(self) -> Iterator:
        """Iterate over the nodes. Use: 'for n in G'.

        Returns
        -------
        niter : iterator
            An iterator over all nodes in the graph.
        """
        return iter(self.nodes)

    def __contains__(self, n: Any) -> bool:
        """Returns True if n is a node, False otherwise. Use: 'n in G'.
        """
        try:
            return n in self.nodes
        except TypeError:
            return False

    def __len__(self) -> int:
        """Returns the number of nodes in the graph. Use: 'len(G)'.

        Returns
        -------
        nnodes : int
            The number of nodes in the graph.

        See Also
        --------
        number_of_nodes: identical method
        order: identical method
        """
        return len(self.nodes)

    def __getitem__(self, n: Any) -> set:
        """Returns a dict of neighbors of node n.  Use: 'G[n]'.

        Parameters
        ----------
        n : node
           A node in the graph.
        """
        return self.neighbors(n)


if __name__ == "__main__":
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
