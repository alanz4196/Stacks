import time
from Stack import Stack

def Hanoi_rec(n, s, a, d):
	print(n, s, a, d)
	# TODO replace pass with your base and recursive cases.
	if n>0:
		Hanoi_rec(n-1, s,d,a)
		d.push(s.pop())
		Hanoi_rec(n-1,a,s,d)
	else:
		d.push(s.pop())
	print(n, s, a, d)
	print()

def Hanoi(n):
	source = Stack()
	dest = Stack()
	aux = Stack()
	i = n-1
	while i >= 0:
		source.push(i)
		i = i - 1
	Hanoi_rec(n-1, source, aux, dest)

if __name__ == '__main__':
	numarr = [ ]
	timearr = [ ]
	for i in range(1,15):
		start = time.clock()
		Hanoi(i)
		end = time.clock()
		numarr.append(i)
		timearr.append(end - start)
		
	print(numarr, "\n", timearr)
	#print('computed Hanoi(' + str(n) + ') in ' + str(end - start) + ' seconds.')
