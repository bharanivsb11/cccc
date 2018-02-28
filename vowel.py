ch="btabb"
n=len(ch)
p=0
for i in range(0,n):
  if(ch[i]=='a' or ch[i]=='e' or ch[i]=='i' or ch[i]=='o' or ch[i]=='u'):
    p=p+1 
if(p>=1):
  print"yes"
else:
  print"no"
