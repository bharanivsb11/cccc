a="10220101"
n=len(a)
p=0
q=0
for i in range(0,n):
	if(a[i]=='1'or a[i]=='0'):
		p=p+1
	if(a[i]!='1' or a[i]!='0'):
		q=q+1	
if(n==p):
	print("yes")
else:	
	print("no")
