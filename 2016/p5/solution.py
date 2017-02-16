import md5


def generate_password_a(i_str, limit):
    password = []
    index = 0
    while True:
        if len(password) == limit:
            break
        s = '%s%s' % (i_str, index)
        digest = md5.md5(s).hexdigest()
        if digest[:5] == "00000":
            password.append(digest[5])
        index += 1
    return "".join(password)


def generate_password_b(i_str, limit):
    password = ['0'] * limit
    password_found = [False] * limit
    index = 0
    while True:
        if len(filter(lambda _: _, password_found)) == limit:
            break
        s = '%s%s' % (i_str, index)
        digest = md5.md5(s).hexdigest()
        if digest[:5] == "00000":
            p, c = digest[5], digest[6]
            if (48 <= ord(p) < 48 + limit) and not password_found[int(p)]:
                password[int(p)] = c
                password_found[int(p)] = True
        index += 1
    return "".join(password)


# a
print generate_password_a("ffykfhsq", 8)
# b
print generate_password_b("ffykfhsq", 8)
