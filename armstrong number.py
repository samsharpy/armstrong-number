#craeated 27/08/2019
#author: samuvel
a=int(input('enter the number:')) #getting the input fro user 
b=0 #intialzing 0 to variable
c=a
while(c>0):#checking wheather c is greater then 0
    digit=c%10
    b+=(digit**3)
    c//=10# cheking whether its is armstrong number
if(a==b):
    print("its armstrong number")
else:
    print("its not")#if statement to give output
