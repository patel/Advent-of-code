def decompress_line(ip_str, part_b=False):
    current_index = 0
    cnt = 0
    if ip_str.find('(') < 0:
        return ip_str
    while True:
        if current_index >= len(ip_str):
            break
        if ip_str[current_index] == '(':
            closing_marker_index = ip_str[current_index:].find(')')
            marker = ip_str[current_index + 1:current_index + closing_marker_index]
            num_chars, num_times = map(int, marker.split('x'))
            sequence = ip_str[
                       current_index + closing_marker_index + 1:current_index + closing_marker_index + 1 + num_chars]
            if part_b and sequence.find('(') >= 0:
                cnt += decompress_line(sequence, part_b) * num_times
            else:
                cnt += len(sequence * num_times)
            current_index += closing_marker_index + 1 + num_chars
        else:
            cnt += len(ip_str[current_index])
            current_index += 1
    return cnt


ip_str = open('input.txt', 'r').read()

#a
print (decompress_line(ip_str))
#b
print (decompress_line(ip_str, part_b=True))
