import itertools
import md5
from collections import Counter, defaultdict


def get_valid_sequences(digest):
    return ((filter(lambda x: x[0] == x[1] and x[0] == x[2], [digest[i:i + 3] for i in range(len(digest) - 2)])),
            filter(lambda x: x[0] == x[1] and x[0] == x[2] and x[0] == x[3] and x[0] == x[4],
                   [digest[i:i + 5] for i in range(len(digest) - 4)]))


def get_index_of_key_number(salt, key_number, hash_count=1):
    index = 0
    sequence_lookup = defaultdict(dict)
    key_indexes = set([])
    potential_indexes = {}
    found_target_index = False
    while True:
        current_digest = "%s%s" % (salt, index)
        for i in range(0, hash_count):
            current_digest = md5.new(current_digest).hexdigest()
        three_valid_sequences, five_valid_sequences = get_valid_sequences(current_digest)
        if found_target_index and not len(potential_indexes.keys()):
            return sorted(key_indexes)[key_number - 1]
        for valid_sequence in five_valid_sequences:
            if sequence_lookup.get(valid_sequence[0:3]):
                key_indexes.update(sequence_lookup.get(valid_sequence[0:3]).keys())
        if not found_target_index:
            for valid_sequence in three_valid_sequences:
                sequence_lookup[valid_sequence][index] = current_digest
                potential_indexes[index] = valid_sequence
                break
        if index >= 1000:
            last_index = index - 1000
            ejected_valid_sequence = potential_indexes.pop(last_index, None)
            if ejected_valid_sequence:
                del sequence_lookup[ejected_valid_sequence][last_index]
        if len(key_indexes) >= key_number:
            found_target_index = True
        index += 1


print get_index_of_key_number('zpqevtbw', 64, 1)
print get_index_of_key_number('zpqevtbw', 64, 2017)
