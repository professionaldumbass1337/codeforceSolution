def main():
    n = input()
    if n == n[::-1]:
        print("This is a Palindrome ; "+n+n[::-1])
    else:
        print("This is NOT a Palindrome")

if __name__=='__main__':
    main()