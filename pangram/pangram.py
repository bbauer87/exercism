def is_pangram(sentence):

    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    compare = []
    
    for x in sentence.lower():
        if x == " ":
            continue
        if x not in compare:
            compare.append(x)

    compare.sort()
    if letters != compare:
        return "Not a pangram."
    else:
        return "That's a pangram!"
