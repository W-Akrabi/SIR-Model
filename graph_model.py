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


class Graph:
    """A class for representing an undirected graph."""

    def __init__(self):
        """Initialize the Graph."""
        self.nodes = {}  # Dictionary to store nodes and their attributes
        self.edges = {}  # Dictionary to store edges and their attributes

    def add_node(self, node, **attr):
        """Add a node to the graph.

        Parameters:
            node: hashable
                The node to add.
            attr: dict, optional
                Node attributes.

        """
        if node not in self.nodes:
            self.nodes[node] = attr

    def add_nodes_from(self, nodes, **attr):
        """Add multiple nodes to the graph.

        Parameters:
            nodes: iterable
                An iterable of nodes.
            attr: dict, optional
                Node attributes.

        """
        for node in nodes:
            self.add_node(node, **attr)

    def remove_node(self, node):
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

    def remove_nodes_from(self, nodes):
        """Remove multiple nodes from the graph.

        Parameters:
            nodes: iterable
                An iterable of nodes to remove.

        """
        for node in nodes:
            self.remove_node(node)

    def add_edge(self, u, v, **attr):
        """Add an edge to the graph.

        Parameters:
            u, v: hashable
                Nodes to connect with the edge.
            attr: dict, optional
                Edge attributes.

        """
        if (u, v) not in self.edges and (v, u) not in self.edges:
            self.edges[(u, v)] = attr

    def add_edges_from(self, ebunch, **attr):
        """Add multiple edges to the graph.

        Parameters:
            ebunch: iterable
                An iterable of edge tuples.
            attr: dict, optional
                Edge attributes.

        """
        for edge in ebunch:
            self.add_edge(*edge, **attr)

    def remove_edge(self, u, v):
        """Remove an edge from the graph.

        Parameters:
            u, v: hashable
                Nodes connected by the edge.

        """
        if (u, v) in self.edges:
            del self.edges[(u, v)]
        elif (v, u) in self.edges:
            del self.edges[(v, u)]

    def remove_edges_from(self, ebunch):
        """Remove multiple edges from the graph.

        Parameters:
            ebunch: iterable
                An iterable of edge tuples to remove.

        """
        for edge in ebunch:
            self.remove_edge(*edge)

    def has_node(self, node):
        """Check if the graph contains the given node.

        Parameters:
            node: hashable
                The node to check.

        Returns:
            bool:
                True if the graph contains the node, False otherwise.

        """
        return node in self.nodes

    def has_edge(self, u, v):
        """Check if the graph contains the given edge.

        Parameters:
            u, v: hashable
                Nodes connected by the edge.

        Returns:
            bool:
                True if the graph contains the edge, False otherwise.

        """
        return (u, v) in self.edges or (v, u) in self.edges

    def neighbors(self, node):
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

    def clear(self):
        """Remove all nodes and edges from the graph."""
        self.nodes.clear()
        self.edges.clear()

    def clear_edges(self):
        """Remove all edges from the graph."""
        self.edges.clear()

    def __iter__(self):
        """Iterate over the nodes. Use: 'for n in G'.

        Returns
        -------
        niter : iterator
            An iterator over all nodes in the graph.
        """
        return iter(self.nodes)

    def __contains__(self, n):
        """Returns True if n is a node, False otherwise. Use: 'n in G'.
        """
        try:
            return n in self.nodes
        except TypeError:
            return False

    def __len__(self):
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

    def __getitem__(self, n):
        """Returns a dict of neighbors of node n.  Use: 'G[n]'.

        Parameters
        ----------
        n : node
           A node in the graph.
        """
        return self.neighbors(n)
