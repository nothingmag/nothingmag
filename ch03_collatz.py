"""
File: collatz.py
Author: Maggie Wu
Date: 2024-09-09

Description:
"""
def collatz(number):
   output_num = 0
   if (number % 2 == 0):
      output_num = number / 2
   else:
      output_num = 3 * number + 1

   return output_num

print('Enter a number: ')
number = int(input())

bContinue = True
while (bContinue):
   output_num = collatz(number)
   print(output_num)

   if (output_num == 1):
      break
   else:
      number = int(input())

