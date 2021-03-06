"""
Date: 19th April 2022 Tuesday
Name: kavuri venkatesh reddy
File Desc: DATA TYPES integer(int),float(float),string(str),boolean(bool)
"""
'''type() > this method will help us to know what datatype it is.'''

''' Integer Data Type (int)
---> Integer value is representrd by 'int' class
---> It contains psitive or negative whole numbers (with out function or decimals
---> In python there is no limit to how long an integer value can be 
EX : 0,1,2,3,-1,-2,-3......

---> FORMATE SPECIFER for int (%d or %i) '''

# print(type(6))
# print(type(2))
# print(type(0))
# print(type(-7))

# a=6
# print(a)
# print('%d' %a)
# print('%i' %a)

#-------------------------------------

"""" Float Data Type(float)
---> Float value is representrd by 'float' class
---> It is specifed in Decimal values
---> It contains Positive  and Negative Decimal values
EX : 0.1,9.2,.1,-2.3,-3.9

---> FORMATE SPECIFER for float is (%f) """

# print(type(0.0))
# print(type(2.3))
# print(type(-6.7))
# print(type(.3))

# b=4.7 
# print(b)
# print('%f' %b) 
# print('%.1f' %b)
# print('%.2f' %b)
# print('%.3f' %b)
# print('%3f' %b)
# print('%8f' %b)
# print('%9f' %b)
# print('%12f' %b)

"""" STRING Data Type(str)
---> string value is representrd by 'str' class
---> string are 'arrays' of bytes represented by unicode charactors
---> anything encloed between single quotes or double quotes or 
three times single quotes or three times double quoteskept inside the print statement or 
assigned to a variable is called as string. """

# print(type('hi')) 
# print(type('8')) 
# print(type('4.7')) 

# a='hi' ; b="bye" ; c='''chai'''; d="""die"""
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))
# print(d,type(d))

# print('%s'%b)
# print('%s'%a)
# print('%s'%c)

""" BOOLEAN DATA TYPE (bool0
--->boolean value is representrd by 'bool' class
---> Data Type withoneof the two built in value True or False
---> Depending the Boolean will give the Answers in (True or False)
---> NOTE : True or False with captial 'T' and 'F' are valid boolean other wise python will throw an arror """
# print(type(True))
# print(type(False))
# print(6<7) # True
# print(4>7) # False
# print(7==7) # True
# print(7!=7) # False

# print('hey'.isidentifier())
# print('_hey'.isidentifier())
# print('5hey'.isidentifier())

print(type(1))        #'int'
print(type(-2))       #'int'
print(type(0.1))      #'float'
print(type(-0.2))     #'float'
print(type('python')) #'str'
print(type("python")) #'str'
print(type('''python''')) #'str'
print(type("""python""")) #'str'
print(type(3<5))      #'bool'
print(type(5<3))      #'bool'
print(type(True))     #'bool'
print(type(False))    #'bool'
