def my_div(a):
  maxd=int (1);
  for i in range(a-1,1,-1):
    if (a%i==0):
      if (maxd<i):
        maxd=i

  if (maxd==1):
    return a
  else :
    return maxd

a=int(input());
print(my_div(a));
