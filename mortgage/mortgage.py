"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION


class Mortgage():

    def __init__(self, loan: float, rate: str, frequency: str, Amortization: int):
        
        
        if loan <= 0:
            raise ValueError("Loan Amount must be positive.")
        
        try:
            self.rate = MortgageRate[str(rate)]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        try:
            self.frequency = PaymentFrequency[str(frequency)]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        
        if  Amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")  
        

