from examples.examples_utils import get_command_sequence,plot_sequences_complexities


def main():
    # Unconstrained commutation
    non_comm_graph = []

    max_length = int(1e5)
    lengths = list(range(10, max_length, max_length // 11))
    alphabet = ["n", "s", "w", "e"]
    sequences = get_command_sequence(lengths, alphabet)
    plot_sequences_complexities(lengths, sequences, non_comm_graph)


if __name__ == '__main__':
    main()
