#copying list

x=[1,2,3,4,5]
y=x
#this well refer to same memory point on a location where x resides
y[1]='key'
print(y)

#this will create a new copy of y on a new location
y=x[:]
y=list(x)
