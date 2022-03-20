import os
import time

import matplotlib.pyplot as plt
import numpy as np
from lempel_ziv_complexity import lempel_ziv_complexity

from polz import POLZ
from polz_utils import Util


def plot_sequences_complexities(lengths: list, sequences: list, non_comm_graph: list) -> None:
    polz = POLZ()
    complexities_list = []
    times_list = []

    for sequence in sequences:
        # LZ78
        time_1 = time.time()
        lz78_complexity = lempel_ziv_complexity(sequence)
        time_2 = time.time()
        lz78_time = time_2 - time_1

        # POLZ
        time_1 = time.time()
        polz_complexity, _ = polz.encode(sequence, non_comm_graph)
        time_2 = time.time()
        polz_time = time_2 - time_1

        complexities_list.append([lz78_complexity, polz_complexity])
        times_list.append([lz78_time, polz_time])

    complexities = np.array(complexities_list)
    times = np.array(times_list)

    plot_complexities(lengths, complexities, times)


def generate_command_sequence(file, lengths, alphabet) -> None:
    util = Util()
    for length in lengths:
        sequence = util.generate_sequence(length, alphabet)
        file.write(sequence + "\n")

    print("Command file saved!")


def get_command_sequence(lengths: list, alphabet: list) -> list:
    robot_commands_path = "./robot_commands.txt"

    if os.path.exists(robot_commands_path):
        pass
    else:
        with open(robot_commands_path, 'a') as f:
            generate_command_sequence(f, lengths, alphabet)

    with open(robot_commands_path) as f:
        return f.readlines()


def plot_complexities(lengths, complexities_list, times_list):
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(lengths, complexities_list[:, 0], "-o", label="LZ78")
    plt.plot(lengths, complexities_list[:, 1], "-s", label="POLZ")
    plt.xlabel("Sequence length")
    plt.ylabel("Complexity")
    plt.grid()
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(lengths, times_list[:, 0], "-o", label="LZ78")
    plt.plot(lengths, times_list[:, 1], "-s", label="POLZ")
    plt.xlabel("Sequence length")
    plt.ylabel("Time (s)")
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()