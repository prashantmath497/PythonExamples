#define methods


def sum(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

n1=int(input("Enter the 1 number"))
n2=int(input("Enter 2 number"))
opr=input("Enter operator")
if(opr=="+"):
  print("Number of args are two",sum(n1,n2))
elif(opr=="-"):
  print("Number of args are two",sub(n1,n2))
elif(opr=="*"):
  print("Number of args are two",mul(n1,n2))
elif(opr=="/"):
  print("Number of args are two",div(n1,n2))


  
  
