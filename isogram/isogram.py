def is_isogram(string):

    ## first way I thought it:    
##    tmp = ""
##    for char in string.lower():
##        if char in tmp and char.isalpha():
##            return False
##        tmp += char
##
##    return True

    ## more elegant way:
    string = string.lower().replace(" ", "").replace("-", "")
    
    return [char for char in string if string.count(char) < 2] == list(string)
    
