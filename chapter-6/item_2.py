def isPalindrome(str, i):
    if(i > len(str)/2):
       return True
    ans = False
    if((str[i] is str[len(str) - i - 1]) and isPalindrome(str, i + 1)):
      ans = True
    return ans

def main():
	str = input("Enter Input : ")
	print(f"'{str}' is palindrome" if isPalindrome(str,0) else  f"'{str}' is not palindrome")

if __name__ == '__main__':
	main()