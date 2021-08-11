# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")

def fun_applycaesarcipher(msg, shift):
	res = ''
	for ch in msg:
		if ch.isupper():
			o = ord(ch)
			s = o + shift
			if s < 65:
				newO = 91 - (65-(s))
			elif o + shift > 90:
				newO = 64 + ((s)-90)
			else:
				newO = s
			res = res + chr(newO)
		elif ch.islower():
			o = ord(ch)
			s = o + shift
			if s < 97:
				newO = 123 - (97-(s))
			elif o + shift > 122:
				newO = 96 + ((s)-122)
			else:
				newO = s
			res = res + chr(newO)
		else:
			res = res + ch
	return res
# print(fun_applycaesarcipher('abcxyz', -2))




