import itertools


def get_next_look_and_say(iString, count=1):
    if count <= 0:
        return iString
    else:
        return get_next_look_and_say(
                ''.join([str(len(list(v))) + str(k) for k, v in itertools.groupby(list(iString))]), count - 1)


print len(get_next_look_and_say('1321131112', 40))
print len(get_next_look_and_say('1321131112', 50))
