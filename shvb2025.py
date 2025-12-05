#1
#a = str(input())
#b = str(input())
#n = ""
#for i in range(len(a)):
 #   if a[i]=="1":
  #      if b[i]=="1":
  #          n += "0"
  #      else:
  #          n+="1"
  #  else:
 #       if b[i]=="1":
  #          n += "0"
 #       else:
 #           n+="1"
#n = n[::-1]
#while n[0]=="0":
#    n=n[1:]
#print(n)

#2
#def dv(a, b):
#    z = 0
#    q = bin(a)[2:]+bin(b)[2:]
#    for i in range(len(q)-2):
#        if q[i]=="1" and q[i+1]=="1":
#            z = 1
#            break
#        if q[i]=="0" and q[i+1]=="0"and q[i+2]=="0":
#            z = 1
#            break
#    if q[-2]=="1" and q[-1]=="1":
#        z = 1
#    return z
#n = int(input())
#x = 0
#L = [i for i in range(1, n+1)]
#for i in range(len(L)-1):
#    for j in range(i+1, len(L)):
#        if dv(L[i], L[j])==1 and dv(L[j], L[i])==1:
#            x+=1
#print(x)

#3
mins = 0
maxs = 0
sleep = input()
upping = input()
a = int(sleep[0])*10*60+int(sleep[1])*60+int(sleep[3])*10+int(sleep[4])
b = int(upping[0])*10*60+int(upping[1])*60+int(upping[3])*10+int(upping[4])
c = int(upping[6])*10*60+int(upping[7])*60+int(upping[9])*10+int(upping[10])
if int(sleep[0])>0:
    mins = b + 1440 - a
    maxs = c + 1440 - a
else:
    mins = b - a
    maxs = c - a
print(b, c, mins, maxs)

