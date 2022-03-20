import os
from typing import Dict

import numpy as np
from examples.examples_utils import plot_sequences_complexities

ATM_OPERATIONS_PATH = "./atm_operations.txt"


def generate_non_comm_graph(n_atm: int, operations: list, map_dict: dict):
    adj = []
    for k in range(n_atm):
        n = range(len(operations))
        for i in n:
            for j in n:
                if i > j:
                    adj.append([
                        map_dict[operations[i] + str(k)],
                        map_dict[operations[j] + str(k)]
                    ])
    return adj


def generate_alphabet(n_atm: int, operations: list):
    alphabet = []
    alphabet_inter = []
    map_dict: Dict[str, str] = {}

    for i in range(n_atm):
        for op in operations:
            alphabet_inter.append(op + str(i))
    for i in range(len(alphabet_inter)):
        map_dict[alphabet_inter[i]] = chr(ord("A") + i)
    for i in alphabet_inter:
        alphabet.append(map_dict[i])
    return alphabet, map_dict


def main():
    n_atm = 10
    operations = ["a", "c", "d", "r", "s", "w"]

    alphabet, map_dict = generate_alphabet(n_atm, operations)

    # Non-commutative graph
    non_comm_graph = generate_non_comm_graph(n_atm, operations, map_dict)

    with open(ATM_OPERATIONS_PATH, "r") as file:
        sequences = file.readlines()[:]
        lengths = []
        for sequence in sequences:
            length_tmp = 0
            for i in alphabet:
                length_tmp += sequence.count(i)
            lengths.append(length_tmp)

        plot_sequences_complexities(lengths, sequences, non_comm_graph)


if __name__ == '__main__':
    main()
