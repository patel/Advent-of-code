import hashlib


def get_md5(secret_key, num_zeros):
    i = 0
    while True:
        m = hashlib.md5(secret_key + str(i))
        if m.hexdigest()[:num_zeros] == '0' * num_zeros:
            return i
        i += 1


# part 1
print get_md5('bgvyzdsv', 5)

# part 2
print get_md5('bgvyzdsv', 6)
