n=int(raw_input())
a=int(raw_input())
b=int(raw_input())
p=0
for i in range(a,b):
	if(n==i):
		p=p+1
if(p==1):
	print"yes"
else:
	print"no"
