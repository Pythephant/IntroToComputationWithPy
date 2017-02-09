def isPalindrome(s):
	def toChars(s):
		''' input string s to lower case'''
		return s.lower()
	
	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			return s[0]==s[-1] and isPal(s[1:-1])

	return isPal(toChars(s))


if __name__ == '__main__':
	print isPalindrome('jason')
	print isPalindrome('aabaa')
