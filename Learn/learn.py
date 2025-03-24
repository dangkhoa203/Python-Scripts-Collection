# ####Calculator####

# a=input("Enter first number : ")
# b=input("Enter second number : ")
# plus=lambda a,b:int(a)+int(b)
# minus=lambda a,b:int(a)-int(b)
# Mul=lambda a,b:int(a)*int(b)
# Sub=lambda a,b:float(a)/float(b)
# ch=int(input("Choice = "))
# 
# if(ch==1):
#     print(plus(a,b))
# elif(ch==2):
#     print(minus(a,b))
# elif(ch==3):
#     print(Mul(a,b))
# elif(ch==4):
#     print(Sub(a,b))




# #### LIST ####
# arr=[1,2,3,4,5,6,7,8,9]
# arr1=[4,6,2,1,8,5,9]
# # print(arr[::-1])
# # arr1.sort()
# # print(arr1)
# name=['n','v','d','y']
# print(name.index('d'))
# name.insert(2,'o')
# name.sort()
# name.extend(arr)
# name.append(10)
# print(name)
# name.remove('v')
# print(name)
# name.pop()
# print(name)
# name.clear()
# print(name)

# i=0
# maxt=[('a','b','c'),('c','a','b'),('b','c','a')]
# for row in maxt:
#     j=0
#     for column in maxt:
#         print(maxt[i][j])
#         j+=1
        
#     i+=1   

# def isnegodd(a):
#     if a%2!=0 and a<0:
#         return True
#     else:
#         return False
# print(isnegodd(-1))

# loc={
#     "a":["S","D","T"],
#     "b":["W","Q","R"],
#     "c":["U","P","N"]}

# print(loc["a"])
# print(loc.get("d","Not right"))


maxt=[('a','b','c'),('c','a','b'),('b','c','a')]
for row in maxt:
    for clo in row:
        print(clo)
        
if 'd' in maxt:
    print("true")
else:
    print("False")