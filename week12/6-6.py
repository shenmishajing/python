def acronym(phrase):
    res = ''
    phrase = phrase.split()
    for p in phrase:
        res += p[0].upper()
    return res


phrase = input()
print(acronym(phrase))
