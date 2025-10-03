# FILE NAME - convert_C_to_F_02.py

# NAME: Justin Weaver  
# DATE: 10/2/25
# BRIEF DESCRIPTION:   C_F_converter2



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
print('===== Temperature Converter =====')
print()
print('  1. Convert from Celsius to Fahrenheit')
print('  2. Convert from Fahrenheit to Celsius')
print()
convert = input('Please choose from the above menu: ')
temp = float(input('Enter a temperature to convert: '))
print()
if (convert=='1'):
  
    fahrenheit = (temp * 9/5) + 32
    print  (f'{temp:.1f} degrees Celsius is {fahrenheit:.1f} degrees Fahrenheit.')
else:

    celsius = (temp - 32 ) * 5/9
    print  (f'{temp:.1f} degrees Fahrenheit is {celsius:.1f} degrees Celsius.')









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
Again the code itself wasn't horrible to do. I built it out line for lne and that part was pretty straight forward.
But I ran this like 10 times trying to get it too pass and it kept failing. At first I thought it was bc i missed a blank line here or there and I did.
But what ultimatley made it keep failing was the 2 spaces before the 1 and 2 options and I had one space. Its always these little things that trip me up.
I write a perfect code that does exactly what its suppose to but always fails due to some missed space or something small and ultimatley inconsequential to the actually code running or working. 






'''
