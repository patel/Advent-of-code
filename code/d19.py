import re
from collections import defaultdict

def generate_map_from_replacement_rules(rules):
    expression_map = defaultdict(list)
    rule_expression = re.compile('(.+) => (.+)')
    for rule in rules:
        rule_match = rule_expression.match(rule)
        (k, v) = rule_match.groups()
        expression_map[k].append(v)
    return expression_map

def get_num_distinct_molecules(rules_str, target_molecule):
    expression_map = generate_map_from_replacement_rules(rules_str.split('\n'))
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