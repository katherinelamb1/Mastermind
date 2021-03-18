# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:15:06 2021

@author: Katherine Lamb
"""

# The computer "thinks" a number with 4 different digits. You guess which digits
# For every digit that matched both in value, and in location the computer gives
# you a *. For every digit that matches in value, but not in space the computer 
# gives you a +. Try to guess the given number in as few guesses as possible.


# TO DO: research if i can congifure this in a way that screen readers will read over it
print( "#     #\n"
     + "##   ##   ##    ####  ##### ###### #####  #    # # #    # #####\n"
     + "# # # #  #  #  #        #   #      #    # ##  ## # ##   # #    #\n"
     + "#  #  # #    #  ####    #   #####  #    # # ## # # # #  # #    #\n"
     + "#     # ######      #   #   #      #####  #    # # #  # # #    #\n"
     + "#     # #    # #    #   #   #      #   #  #    # # #   ## #    #\n"
     + "#     # #    #  ####    #   ###### #    # #    # # #    # #####\n\n\n")

print("System generating key. . .\n")
import random
secret_code = []

for x in range(4):
    secret_code.append(random.randint(0,9))

print("Can you crack the code comprised of four random digits from 0 - 9?")
print(" *   a digit in the guess is in the correct position")
print(" +   a digit in the guess is in the code, in a different position")

# # %%
# latest_list = []
# attempts = 0
# while (latest_list != secret_code and attempts < 10):
        
#     # TO DO: look for built in python user input error checking
#     latest_guess = input("Your guess:")
#     latest_list = list( map( int, list(latest_guess.split()) ) )
    
#     # TO DO: compare the guess to the code,
#     #        output hint

    
#     attempts += 1
    
# # if user succeeds, congradulate them
# # otherwise womp womp
