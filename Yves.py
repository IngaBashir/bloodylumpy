def max(a,b):
	if a>b:
		return(a)
	else:
		return(b)
	

def max3(a,b,c):
	z=max(a,b)
	y=max(z,c)
	return(y)


def max4(a,b,c,d):
	y=max3(a,b,c)
	z=max(y,d)
	return(z)

	


print(max4(1,9.4,11,4))	







