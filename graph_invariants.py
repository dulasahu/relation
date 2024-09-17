from abc import ABC, abstractmethod

class graph_invariants(ABC):

    @abstractmethod
    def algebraic_connectivity(self):
        pass
    @abstractmethod
    def average_degree(self):
        pass
    @abstractmethod
    def chromatic_index(self):
        pass
    @abstractmethod
    def chromatic_number(self):
        pass
    @abstractmethod
    def circumference(self):
        pass
    @abstractmethod
    def clique_number(self):
        pass
    @abstractmethod
    def degeneracy(self):
        pass
    @abstractmethod
    def density(self):
        pass
    @abstractmethod
    def diameter(self):
        pass
    @abstractmethod
    def domination_number(self):
        pass
    @abstractmethod
    def edge_connectivity(self):
        pass
    @abstractmethod
    def feedback_vertex_set_number(self):
        pass
    @abstractmethod
    def genus(self):
        pass
    @abstractmethod
    def girth(self):
        pass
    @abstractmethod
    def group_size(self):
        pass
    @abstractmethod
    def independence_number(self):
        pass
    @abstractmethod
    def index(self):
        pass
    @abstractmethod
    def laplacian_largest_eigenvalue(self):
        pass
    @abstractmethod
    def length_of_longest_induced_path(self):
        pass
    @abstractmethod
    def length_of_longest_path(self):
        pass
    @abstractmethod
    def matching_number(self):
        pass
    @abstractmethod
    def maximum_degree(self):
        pass
    @abstractmethod
    def minium_degree(self):
        pass
    @abstractmethod
    def number_of_arc_orbits(self):
        pass
    @abstractmethod
    def number_of_components(self):
        pass
    @abstractmethod
    def number_of_edge_orbits(self):
        pass
    def number_of_edges(self):
        pass
    @abstractmethod
    def number_of_spanning_tree(self):
        pass
    @abstractmethod
    def number_of_triangles(self):
        pass
    @abstractmethod
    def nunber_of_vertex_orbits(self):
        pass
    @abstractmethod
    def number_of_vertices(self):
        pass
    @abstractmethod
    def number_of_zero_eigenvalues(self):
        pass
    @abstractmethod
    def radius(self):
        pass
    @abstractmethod
    def second_largest_eigenvalue(self):
        pass
    @abstractmethod
    def smallest_eigenvalue(self):
        pass
    @abstractmethod
    def treewidth(self):
        pass
    @abstractmethod
    def vertex_connectivity(self):
        pass
    @abstractmethod
    def vertex_cover_number(self):
        pass


class graph_property_one(graph_invariants):

    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices

    def graph_adjecency_matrix(self):
        pass
    def graph_degree_matrix(self):
        pass
    def graph_laplacian_matrix(self):
        pass
    def number_of_spanning_trees(self):
        vertices_length = len(self.vertices)
        spanning_tree_number = vertices_length**(vertices_length-2)
        return spanning_tree_number
