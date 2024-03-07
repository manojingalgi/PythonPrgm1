#Conditional statement
#if, #else #if,#elif

 #example: if person is eligible to vote
 #age>=18
#
# age=20
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")
#

#example2
# if False:
#     print("true statement")
# else:
#     print("false statement")

#example3
# num=10
# if num%2==0:
#     print("given num is even")
# else:
#     print("givven num is odd")
#
#example4: if else in single line(ternary operator)
# num = 25
# print("even number") if num%2==0 else print("odd number")

# #Example5: if else - multiple statement
# a=5
# a=int(input("enter the value: "))
# {print("hello"),print("python")} if a>10 else {print("hi"),print("java")}

#week program
num=int(input("Enter your day: "))
if num==1:
    print("its is sunday")
elif num==2:
    print("its is monday")
elif num == 3:
    print("its is tuseday")
elif num == 4:
    print("its is wensday")
elif num == 5:
    print("its is thursday")
elif num == 6:
    print("its is friday")
elif num==7:
    print("its is saturday")
else:
    print("invalid week number")

