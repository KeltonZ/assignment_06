"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Kelton Zinn
Date: April 16th, 2025
"""

from mortgage_doc.mortgage import Mortgage


"""
Will read file_path file items in order of amount, rate, amortization, frequency. 
It should be noted that the Mortgage accepts arguements in order  of amount (loan), rate, frequency, amortization,
so you will be required to order it as such, since the file items are out of order. 
"""

file_path = "data\\pixell_river_mortgages.txt"

try:
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
   
        for data in input:
            items = data.split(",")
            
            try:
                amount = float(items[0])
                rate = items[1]
                amortization = int(items[2]) #originally written as amortization = int(items[2]), however the order of coding that was asking has frequency in this spot
                frequency = items[3] # above comment applies to this as well
                mortgage_obj = Mortgage(amount, rate, frequency, amortization) #arranged the order to match the way it was written in code previously?
                
                print(mortgage_obj)
                
            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")
except FileNotFoundError:
    print("Unable to find file with given path" f"{file_path}")    