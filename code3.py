

def com_str(a,b): #Function to do the job :P
	if len(a)<len(b):
		return a+b+a
	else:
		return b+a+b

a=raw_input("Enter string A")
b=raw_input("Enter string B")
print(com_str(a,b))
