import re
from collections import defaultdict

class Node:
    def __init__(self, source, count, parent):
        self.source = source
        self.parent = parent
        self.count = count
        self.children = {}

def generate_map_from_replacement_rules(rules):
    expression_map = defaultdict(list)
    reverse_rule_expression = defaultdict(list)
    rule_expression = re.compile('(.+) => (.+)')
    for rule in rules:
        rule_match = rule_expression.match(rule)
        (k, v) = rule_match.groups()
        expression_map[k].append(v)
        reverse_rule_expression[v].append(k)
    return expression_map, reverse_rule_expression


def get_num_distinct_molecules(rules_str, target_molecule):
    expression_map, reverse_rule_expression = generate_map_from_replacement_rules(rules_str.split('\n'))
    molecules_set = expression_map.keys()
    sorted_molecules_set = sorted(molecules_set, key=lambda x: -len(x))
    target_molecules_lookup = {}

    for molecule in sorted_molecules_set:
        target_molecules_lookup[molecule] = [match.start() for match in re.finditer(molecule, target_molecule)]

    result = []
    for m, locations in target_molecules_lookup.iteritems():
        for location in locations:
            for reduction in expression_map[m]:
                result.append(target_molecule[:location] + reduction + target_molecule[location + len(m):])
    return len(set(result))


def get_min_num_steps(rules_str, start_molecule, target_molecule):
    expression_map, reverse_rule_expression = generate_map_from_replacement_rules(rules_str.split('\n'))
    all_molecules = sorted(reverse_rule_expression.keys())
    all_molecules = sorted(all_molecules, key=lambda x: -len(x))
    skipped_list = set([]) # Skip list to avoid dead ends
    largest_reduction = len(all_molecules[0]) - len(reverse_rule_expression[all_molecules[0][0]])
    current_node = Node(start_molecule, 0, None)
    while current_node.source != target_molecule and current_node is not None:
        not_found = True
        for molecule in set(all_molecules) - set(current_node.children.keys()):
            if not_found and current_node.source.find(molecule) >= 0:
                for r_molecule in reverse_rule_expression[molecule]:
                    if not_found and not current_node.children.has_key(molecule + '|' + r_molecule):
                        current_node.children[molecule + '|' + r_molecule] = \
                            Node(current_node.source.replace(molecule, r_molecule, 1),
                                                              current_node.count + 1,
                                                              current_node)

                        if not current_node.source.replace(molecule, r_molecule, 1) in skipped_list:
                            current_node = current_node.children[molecule + '|' + r_molecule]
                            not_found = False
                        break
        if not_found:
            skipped_list.add(current_node.source)
            total_length = len(current_node.source)
            # We can backtrack the following number of steps with certainty to skip deadends
            for i in range(0, total_length/largest_reduction - 1):
                skipped_list.add(current_node.source)
                current_node = current_node.parent
            while current_node.source in skipped_list:
                current_node = current_node.parent

    return current_node.count


t = \
"""Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg"""


target_molecule = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'
print get_num_distinct_molecules(t, target_molecule)
print get_min_num_steps(t, target_molecule, 'e')
