import re


def is_tls(s):
    def is_abba(s):
        return any([filter(lambda x: x == x[::-1] and x[0] != x[1], [s[i:i + 4] for i in range(len(s) - 3)])])

    matches = re.findall("(?P<f>\w+)[\[(?P<h>\w+)\](?P<s>\w+)]?", s)
    sequences, hypernets = [matches[i * 2] for i in range(len(matches) / 2 + 1)], \
                           [matches[i * 2 + 1] for i in range(len(matches) / 2)]
    return all([any(map(lambda x: is_abba(x), sequences)), all(map(lambda x: not is_abba(x), hypernets))])


def is_ssl(s):
    def get_abas(s):
        return filter(lambda x: x == x[::-1] and x[0] != x[1], [s[j:j + 3] for j in range(len(s) - 2)])

    def get_babs(s):
        return map(lambda y: '%s%s%s' % (y[1], y[0], y[1]), get_abas(s))

    matches = re.findall("(?P<f>\w+)[\[(?P<h>\w+)\](?P<s>\w+)]?", s)
    potential_babs_lists = [get_babs(s) for s in [matches[i * 2] for i in range(len(matches) / 2 + 1)]]
    potential_babs = [el for sublist in potential_babs_lists for el in sublist]
    available_babs_lists = [get_abas(s) for s in [matches[i * 2 + 1] for i in range(len(matches) / 2)]]
    available_babs = [el for sublist in available_babs_lists for el in sublist]
    return any(map(lambda x: x in available_babs, potential_babs))


def get_number_of_tls_ip(ip_str):
    return sum(filter(lambda x: x, [is_tls(s) for s in ip_str.split('\n')]))


def get_number_of_ssl_ip(ip_str):
    return sum(filter(lambda x: x, [is_ssl(s) for s in ip_str.split('\n')]))


ip_str = open('input.txt', 'r').read()

# a
print get_number_of_tls_ip(ip_str)
# b
print get_number_of_ssl_ip(ip_str)
