def anagrams(S): # S is a set of strings
    d = {} # maps s to list of words with signature s
    for word in S: # group words according to the signature
        s = ''.join(sorted(word)) # calculate the signature
        if s in d:
            d[s].append(word) # append a word to an existing signature
        else:
            d[s] = [word] # add a new signature and its first word
    return [d[s] for s in d if len(d[s]) > 1]
def main():
    s=str(input("enter a string: "))
    print(anagrams(s))
if __name__=="__main__":
    main()
