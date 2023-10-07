def main():
   print(shorten(input("Input: ")))


def shorten(word):
    newWord = ""
    i = 0
    while i < word.__len__():
        #removed check for uppercase vowels
        if word[i:i+1] != "a" and word[i:i+1] != "e" and word[i:i+1] != "i" and word[i:i+1] != "o" and word[i:i+1] != "u":
            newWord+= word[i:i+1]
        i+=1
    return(newWord)


if __name__ == "__main__":
    main()