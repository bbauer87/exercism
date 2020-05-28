def find_anagrams(word, candidates):

    result = []
    
    for x in candidates:
        if word.lower() == x.lower(): continue

        result.append(x) if sorted(word.lower()) == sorted(x.lower()) else 0

    return result
