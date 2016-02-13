import re
from collections import defaultdict
import pprint

def generate_map_from_replacement_rules(rules):
    expression_map =  defaultdict(list)
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
                result.append(target_molecule[:location] + reduction + target_molecule[location+len(m):])
    return len(set(result))


def get_min_num_steps(rules_str, target_molecule, source_molecule):
    expression_map, reverse_rule_expression = generate_map_from_replacement_rules(rules_str.split('\n'))
    all_molecules = sorted(reverse_rule_expression.keys(), key=lambda x: -len(x))
    current_count = 0
    target_tree = {'target': target_molecule, 'source': '', 'prev': None, 'count': 0}
    current_node = target_tree
    while target_molecule != source_molecule:
        not_found = True
        for molecule in all_molecules:
            if not_found and \
                target_molecule.find(molecule) >= 0 and \
                    current_node.get('source', None) != molecule:
                print molecule
                target_molecule = target_molecule.replace(molecule, reverse_rule_expression[molecule][0], 1)
                current_node['source'] = molecule
                current_node['next'] = {'target': target_molecule, 'count': current_node.get('count', 0) + 1}
                prev_node = current_node
                current_node = current_node['next']
                current_node['prev'] = prev_node
                not_found = False
                current_count = current_node['count']
                continue
        if not_found:
            target_molecule = current_node['target']
            current_node = current_node['prev']

    pprint.pprint(current_node)
    return current_count



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

z = \
"""e => H
e => O
H => HO
H => OH
O => HH"""

target_molecule = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'
target_molecule_1 = 'HOHOHO'
#print get_num_distinct_molecules(t, target_molecule)
print get_min_num_steps(t, target_molecule, 'e')