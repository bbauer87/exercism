from random import randint

def is_valid(isbn):

    result = False
    isbn = validation(isbn)

    if isbn:
        if (isbn[0] * 10 + isbn[1] * 9 + isbn[2] * 8 + isbn[3] * 7 + isbn[4] * 6 + isbn[5] * 5 + \
                isbn[6] * 4 + isbn[7] * 3 + isbn[8] * 2 + isbn[9] * 1) % 11 == 0:
            
            result = True
            print("ISBN-13 from the ISBN-10 original:", isbn_13_generator(isbn, "10 to 13"))

    return result

def validation(isbn, operation = "normal"):
    
    isbn = isbn.replace("-", "")

    if operation == "normal" or (operation != "normal" and isbn):
        
        if operation == "normal":        
            if len(isbn) != 10:
                return False

        if isbn[-1].isalpha() and isbn[-1].upper() != "X":
            return False
        
        for x in isbn:
            if x.isalpha() and x.upper() != "X":
                return False

        for x in isbn[:-1]:
            if x.upper() == "X":
                return False
        
        if isbn[-1].upper() == "X":
            isbn = list(map(int, isbn[:-1]))
            isbn.append(10)
        else:
            isbn = list(map(int, isbn))

    else:
        isbn = []           

    return isbn

def isbn_13_generator(isbn, isbn_type, has_X = False):

    if isbn_type == "10 to 13": val = 3
    else:                       val = 13 - len(isbn)
    
    while True:
        
        for inserting in range(val):
            isbn.insert(0, randint(0,9))
            
        if (isbn[0] * 13 + isbn[1] * 12 + isbn[2] * 11 + \
            isbn[3] * 10 + isbn[4] * 9 + isbn[5] * 8 + isbn[6] * 7 + isbn[7] * 6 + isbn[8] * 5 + \
            isbn[9] * 4 + isbn[10] * 3 + isbn[11] * 2 + isbn[12] * 1) % 11 == 0:
            
            tmp = f"{isbn[0]}-"
            
            for x in isbn[1:4]:
                tmp += str(x)
                
            tmp += "-"
            
            for x in isbn[4:12]:
                tmp += str(x)

            if has_X == True:    tmp += "-X"
            else:                tmp += f"-{isbn[-1]}"
            
            return tmp
        
        else:            
            for deleting in range(val):
                del isbn[0]

def generator(partial = ""):

    if partial:  string = f"ISBN-13 from the partial ISBN {partial}:"
    else:        string = "ISBN-13 fully generated:"
    
    has_X = False
    if partial and partial[-1].upper() == "X": has_X = True
    
    if len(partial.replace("-", "")) >= 13:        raise ValueError("Partial ISBN already have 13 or more digits")

    isbn = validation(partial, "generator")      

    if isbn or isbn == []:  print(string, isbn_13_generator(isbn, "new", has_X))
    else:                   raise ValueError("Partial ISBN must be composed only by numbers or 'X' as check character, separated or not by dashes")



    

    

    
        
        
    
