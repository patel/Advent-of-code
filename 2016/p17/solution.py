import md5


class Node():
    def __init__(self, val, parent=None, children=None):
        self.val = val
        self.children = [] if not children else children
        self.parent = parent

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)


def get_path_to_target(original_passcode, size, longest=False):
    def get_added_child(node, point):
        children = node.children
        existing_child = filter(lambda child: child.val[0] == point[0] and child.val[1] == point[1], children)
        if existing_child:
            return None
        else:
            new_child = Node(point, node)
            node.add_child(new_child)
            return new_child

    def _is_open_space(c):
        return c in list('bcdef')

    current_step = Node((0, 0))
    potential_nodes = [(current_step, original_passcode)]
    all_solutions = []

    while True:
        if not potential_nodes:
            return all_solutions.pop()
        current_step, passcode = potential_nodes.pop(0)
        digest = md5.new(passcode).hexdigest()[0:4]
        current_path = {
            'U': _is_open_space(digest[0]),
            'D': _is_open_space(digest[1]),
            'L': _is_open_space(digest[2]),
            'R': _is_open_space(digest[3])
        }
        if (current_step.val[0] == size - 1) and (current_step.val[1] == size - 1):
            target_path = passcode[len(original_passcode):]
            if longest:
                all_solutions.append(target_path)
                continue
            else:
                return target_path

        valid_current_paths = map(lambda (k, v): k, filter(lambda (k, v): v, current_path.iteritems()))

        while True:
            added_child = None
            path_under_consideration = valid_current_paths.pop() if len(valid_current_paths) else None
            if not path_under_consideration:
                break
            if path_under_consideration == 'U' and current_step.val[1] - 1 >= 0:
                added_child = get_added_child(current_step, (current_step.val[0], current_step.val[1] - 1))
            if path_under_consideration == 'D' and current_step.val[1] + 1 < size:
                added_child = get_added_child(current_step, (current_step.val[0], current_step.val[1] + 1))
            if path_under_consideration == 'L' and current_step.val[0] - 1 >= 0:
                added_child = get_added_child(current_step, (current_step.val[0] - 1, current_step.val[1]))
            if path_under_consideration == 'R' and current_step.val[0] + 1 < size:
                added_child = get_added_child(current_step, (current_step.val[0] + 1, current_step.val[1]))

            if added_child:
                potential_nodes.append((added_child, passcode + path_under_consideration))
            else:
                potential_nodes = filter(lambda (x, y): y != passcode + path_under_consideration, potential_nodes)


# a
print get_path_to_target('edjrjqaa', 4)
# b
print len(get_path_to_target('edjrjqaa', 4, longest=True))
