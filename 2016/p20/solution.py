def get_non_overlapping_intervals(ip_lines):
    intervals = sorted([map(int, ip_line.split('-')) for ip_line in ip_lines.split('\n')], key=lambda x: (x[0], x[1]))
    curr_lower, curr_higher = intervals[0]
    merged_intervals = []
    for interval in intervals:
        if (interval[0] - 1) <= curr_higher:
            curr_higher = max(curr_higher, interval[1])
        else:
            merged_intervals.append((curr_lower, curr_higher))
            curr_lower, curr_higher = interval

    merged_intervals.append((curr_lower, curr_higher))
    return merged_intervals


def get_lowest_unblocked_range(ip_lines):
    non_overlapping_intervals = get_non_overlapping_intervals(ip_lines)
    return non_overlapping_intervals[0][1] + 1


def get_all_valid_ips(ip_lines, max_ip):
    non_overlapping_intervals = [(0, 0)] + get_non_overlapping_intervals(ip_lines) + [(max_ip, max_ip)]
    return sum(map(lambda (a, b): max(0, b[0] - a[1] - 1),
                   [(non_overlapping_intervals[i], non_overlapping_intervals[i + 1])
                    for i in range(len(non_overlapping_intervals) - 1)]))


ip_str = open('input.txt', 'r').read()

# a
print get_lowest_unblocked_range(ip_str)

# b
print get_all_valid_ips(ip_str, 2**32-1)
