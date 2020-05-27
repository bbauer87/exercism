class PhoneNumber:
    def __init__(self, number):
        tmp = ""
        for x in number:
            if x.isalpha():
                raise ValueError("Invalid number as it have letters on it")
            if x.isdigit():
                tmp += x
                
        if len(tmp) < 10 or len(tmp) > 11:
            raise ValueError("Incomplete or invalid number")
        
        if len(tmp) == 11:
            if tmp[0] != "1":
                raise ValueError("Invalid country code")
            else:
                tmp = tmp[1:]

        if len(tmp) == 10 and (tmp[0] not in list("23456789") or tmp[3] not in list("23456789")):
            raise ValueError("Invalid area or exchange code")    
        
        self.number = tmp
        self.area_code = self.number[:3]

    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"
        
