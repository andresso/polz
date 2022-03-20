from polz_utils.utils_class import Util
from polz_utils.hash_table_class import HashTable


class POLZ:
    def __init__(self):
        self.util = Util()

    def encode(self, sequence, non_comm_graph):
        encoded_dic = []  # D
        projection_table = HashTable()  # Q

        last_index = 0  # \rho
        ind = 0
        inc = 1
        polz_complexity = 0

        while True:
            if ind + inc > len(sequence):
                break

            sub_word = sequence[ind: ind + inc]
            proj_sub_word = self.util.word_projections(sub_word, non_comm_graph)
            proj_join = "".join(proj_sub_word)  # \pi_i
            type_sub_word = "".join(sorted(sub_word))   # t_i

            key = proj_join + "-" + type_sub_word

            # If it is a new phrase
            if projection_table.find(key) is None:
                # Increase polz complexity by 1
                polz_complexity += 1

                # Add to encoded dictionary
                sigma_i = sub_word[-1]
                encoded_tuple = (last_index, sigma_i)
                encoded_dic.append(encoded_tuple)

                # Add to projections hash table
                projection_table.insert(key, polz_complexity)
                last_index = 0  # \rho

                ind += inc
                inc = 1
            else:
                # Update index
                last_index = projection_table.find(key)
                inc += 1
        return polz_complexity, encoded_dic

    @staticmethod
    def decode(encoded_dict):
        seq_eq = ""
        decoding_list = [""]

        for rho_i, sigma_i in encoded_dict:
            s_i = decoding_list[rho_i] + sigma_i
            decoding_list.append(s_i)
            seq_eq += s_i

        return seq_eq, decoding_list[1:]
