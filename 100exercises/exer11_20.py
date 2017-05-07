def exer11():
    input = raw_input('>').split(',')
    output = [x for x in input if int(x, 2) % 5 == 0]
    print ','.join(output)


def exer12():

    def is_even(n):
        while n:
            r = n % 10
            if r % 2:
                return False
            n = n / 10
        return True

    output = [str(x) for x in xrange(1000, 3001) if is_even(x)]
    print ','.join(output)



exer12()