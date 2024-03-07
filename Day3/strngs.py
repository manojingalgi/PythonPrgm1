# # str1="my name is"
# # str2 = "Manoj"
# # #print(str1+str2)
# # str1=  str1+" Manu"
# # print(str1)
# #
# # str3= "I'm Successful"
# # print(str3+" in 2024")
# # print(str3*5)
#
#
# #slicing
# str= "welcome"
# # print(str[1:3]) #el
# # print(str[:5]) #welco here starting index is 0 by default
# # print(str[2:]) #lcome
#
# print(str[1:-1]) #elcom last 1 char is removed
# print(str[1:-2]) #elco last 2 char is removed
#
#
# #ord() & chr()
# print(ord("A")) #65 returns ascii value of char
# print(chr(65)) #A return char of ascii value

# #max() min() len()
# print(max("abc"))
# print(min("abc"))
# print(len("abc"))
# #in and not in operator

# #converting string
# s= "String in PYTHON"
# s1 = s.capitalize()
# print(s1)
#
# s2= s.title()
# print(s2)
#
# s3= s.lower()
# print(s3)
#
# s4=s.upper()
# print(s4)
#
# s5= s.swapcase()
# print(s5)
#
# s6= s.replace("in","on")
# print(s6)
#
# #VVVVIMP
# #reverse string
# s="welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print("reversed string is : ",rev_str )

#method 2
s= "welcome"
rev=s[::-1]
print(rev)