def get_prime(i):
    facts = list()
    div = 2
    while(div <= i):
        if (i % div) == 0:
            facts.append(divisor)
            i = i/div
        else:
            div += 1
    return facts