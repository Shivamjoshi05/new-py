def palin(word):
    original = word.lower()
    reversed = original[::-1]
    print("reversed word: ",reversed)
    if original == reversed:
        print("It a Palindrome")
        return True
    else :
        print("it's a palindrome")
        return False


print(palin("leavel"))