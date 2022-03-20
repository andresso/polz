import random


class Util:
    def __init__(self):
        pass

    @staticmethod
    def word_projection_on_edge(word: str, edge: list) -> str:
        projection = ""
        for sigma in word:
            if sigma in edge:
                projection += sigma
            else:
                pass
        return projection

    def word_projections(self, word, non_comm_graph):
        # All edges of the non-commutative graph
        all_edges = ["".join(i) for i in non_comm_graph]
        projections = [self.word_projection_on_edge(word, edge) for edge in all_edges]
        return projections

    def is_congruent(self, word_1: str, word_2: str, non_comm_graph):
        all_edges = ["".join(i) for i in non_comm_graph]
        if sorted(word_1) != sorted(word_2):
            return False
        for edge in all_edges:
            if self.word_projection_on_edge(word_1, edge) != self.word_projection_on_edge(word_2, edge):
                return False
        return True

    @staticmethod
    def generate_sequence(length, alphabet, probabilities=None):
        if probabilities is None:
            probabilities = [1.0/len(alphabet) for i in alphabet]

        n_samples = 50
        pool = []
        sequence = ""
        for i in range(len(alphabet)):
            part = [alphabet[i] for j in range(int(n_samples * probabilities[i]))]
            pool += part
        for i in range(length):
            sequence += random.choice(pool)
        return sequence
