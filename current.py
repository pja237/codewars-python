#!/usr/bin/python

def get_item(n,k):
	if k<0 or k>n:
		return 0
	if n==0:
		return 1
	else:
		return get_item(n-1,k-1)+get_item(n-1,k)


def sierpinski(n):
	triangle=''
	for i in xrange(2**n):
		row=[]
		for j in xrange(i+1):
			row+=[get_item(i,j)]
		print ' '.join(map(lambda i: 'L' if i%2!=0 else ' ', row))
		triangle+='\n' if triangle else ''
		triangle+=' '.join(map(lambda i: 'L' if i%2!=0 else ' ', row))
	print "THE END"
	return triangle

from math import factorial

def sierpinski_nonrec(n):
	triangle=''
        for i in xrange(2**n):
		row=[]
		#row=map(lambda k: factorial(i)/(factorial(k)*factorial(i-k)), xrange(i/2+1) )
		row=map(lambda k: 'L' if (factorial(i)/(factorial(k)*factorial(i-k)))%2!=0 else ' ', xrange(i/2+1) )
		if i!=0: row+=row[::-1] if i%2==1 else row[::-1][1:]
		#print ' '.join(row)
		triangle+='\n' if triangle else ''
		triangle+=' '.join(row)
		#print ' '.join(map(lambda i: 'L' if i%2!=0 else ' ', row))
		#triangle+='\n' if triangle else ''
		#triangle+=' '.join(map(lambda i: 'L' if i%2!=0 else ' ', row))
		#print row
        print "THE END"
        return triangle

def sierpinski_bin(n):
        triangle=''
	row=1
        for i in xrange(2**n):
		print ' '.join(bin(row)[2:]).replace('1', 'L').replace('0', ' ')
		triangle+=' '.join(bin(row)[2:]).replace('1', 'L').replace('0', ' ')
		triangle+='\n' if n!=0 and i!=2**n-1 else ''
		row=row^(row<<1)
        return triangle


level1 = '''
L
L L
'''.strip()

print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
print "START RUN"

#tri=sierpinski(5)
print "rec returned triangle"
#print tri
print "EOT"


#tri=sierpinski_nonrec(3)
print "nonrec returned triangle"
#print tri
print "EOT"

tri=sierpinski_bin(5)
print "nonrec returned triangle"
#print tri
print "EOT"

