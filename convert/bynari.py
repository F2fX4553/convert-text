# Python3 code to demonstrate working of
# Converting String to binary
# Using join() + ord() + format()

# initializing string

def binr():	
    test_str = str(input("enter yor text : " ))
    res = ''.join(format(ord(i), '08b') for i in test_str)
    print("The string after binary conversion : " + str(res))
    binr()
binr()
    ###################################################################


