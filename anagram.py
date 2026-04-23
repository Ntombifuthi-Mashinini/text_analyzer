def is_anagram(s1, s2):
    clean = lambda s: sorted(s.lower().replace(" ", ""))
    return clean(s1) == clean(s2)
print(is_anagram("listen", "silent"))
