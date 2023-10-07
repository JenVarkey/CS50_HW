def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.__len__() < 2 or s.__len__() > 6:
        return False
    if not(s[0:2].isalpha()):
        return True
    if s.isalpha():
        return True
    else:
       numChain = False
       for x in range(s.__len__()):
           if not(s[x:x+1].isalpha() or s[x:x+1].isnumeric()):
            return False
           if numChain and s[x:x+1].isalpha():
               return False
           if s[x:x+1].isnumeric() and s[x-1:x].isalpha():
               if s[x:x+1] == "0":
                   return False
               numChain = True
    return True
if __name__ == "__main__":
    main()