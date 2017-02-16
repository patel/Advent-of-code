def get_dragon_checksum(ip, disk_size):
    def _generate_checksum(data):
        if len(data) % 2 == 1:
            return data
        else:
            return _generate_checksum(''.join(
                map(lambda x: '1' if x[0] == x[1] else '0', [data[i * 2:i * 2 + 2] for i in range(len(data) / 2)])))

    res = ip
    i = 0
    while True:
        a = res
        b = ''.join(map(lambda x: {'0': '1', '1': '0'}[x], a[::-1]))
        res = a + '0' + b
        if len(res) >= disk_size:
            return _generate_checksum(res[0:disk_size])
        i += 1


print get_dragon_checksum('10001001100000001', 272)
print get_dragon_checksum('10001001100000001', 35651584)