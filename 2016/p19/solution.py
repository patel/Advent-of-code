import md5
from collections import defaultdict
from pprint import pprint


def get_elf_with_all_presents_a(num_elfs):
    elfs_with_presents = range(1, num_elfs + 1)
    while elfs_with_presents:
        if len(elfs_with_presents) == 1:
            return elfs_with_presents[0]
        is_odd_number_elfs = len(elfs_with_presents) % 2 == 1
        elfs_with_presents = [elfs_with_presents[i * 2] for i in range((len(elfs_with_presents) + 1) / 2)]
        if is_odd_number_elfs:
            elfs_with_presents.pop(0)


class Node:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None

    def set_neighbors(self, prev, next):
        self.prev = prev
        self.next = next


def get_elf_with_all_presents_b(num_elfs):
    elfs_with_presents = {i: Node(i + 1) for i in range(num_elfs)}
    for i in range(num_elfs):
        elfs_with_presents[i].set_neighbors(elfs_with_presents[(i + num_elfs - 1) % num_elfs],
                                             elfs_with_presents[(i + num_elfs + 1) % num_elfs])
    elfs_with_presents = elfs_with_presents.values()
    to_be_deleted_elf = elfs_with_presents[num_elfs / 2]
    while elfs_with_presents:
        if num_elfs == 1:
            return to_be_deleted_elf.num

        prev_to_be_deleted_elf = to_be_deleted_elf.prev
        next_to_be_deleted_elf = to_be_deleted_elf.next
        prev_to_be_deleted_elf.next = next_to_be_deleted_elf
        next_to_be_deleted_elf.prev = prev_to_be_deleted_elf
        if num_elfs % 2 == 1:
            to_be_deleted_elf = to_be_deleted_elf.next.next
        else:
            to_be_deleted_elf = to_be_deleted_elf.next
        num_elfs -= 1


print get_elf_with_all_presents_a(3017957)
print get_elf_with_all_presents_b(3017957)
