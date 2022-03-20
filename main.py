from polz.polz_class import POLZ


def main():
    polz = POLZ()
    # Non-commutativity graph
    adj = [
        ["n", "s"],
        ["e", "w"],
    ]

    sequence = "nsenwnweewns" # n, s, e, w, nw, ee, wns - Complexity 7
    complexity, encoded_dict = polz.encode(sequence, adj)
    print(f"Sequence: {sequence}")
    print(f"Complexity: {complexity}")
    print(f"Encoded dictionary: {encoded_dict}")

    sequence_eq, _ = polz.decode(encoded_dict)
    print(f"Decompressed sequence: {sequence_eq}")


if __name__ == '__main__':
    main()
