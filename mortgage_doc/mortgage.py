"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage_doc.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """
    Defines the attributes of Mortgage class using __init__, as well as
    accessors and mutators.
    """
    def __init__(self, loan_amount: float, rate: str, frequency: str, amortization: int):
        """
        Args:
            loan_amount: float,
                used to represent the money value that a mortgage broker might loan to a client.
                Must be value greater than zero or raises ValueError
            rate: str,
               Validates value against MortgageRates by using the MortgageRate class Enum in pixell_lookup,py 
            frequency: str,
                Validates value against PaymentFrequency class Enum in pixell_lookup,py
            amortization: int,
                validates value against the VALID_AMORTIZATION set in pixell_lookup,py
            
        """
        
        self.__loan_amount = loan_amount
        self.__amortization = amortization

        if self.__loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")

        try:
            self.__rate = MortgageRate[str(rate)]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
       
        try:
            self.__frequency = PaymentFrequency[str(frequency)]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        
        if self.__amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
    
      
        
            

    @property
    def loan_amount(self):
        """Gets the loan amount 
        
        Returns:
            float: The loan amount
        """
        
        return self.__loan_amount
    
    @loan_amount.setter
    def loan_amount(self, loan_amount: float) -> None:
        """
        sets the loan amount for the mortgage

        Args:
            loan (float): A value greater than zero must be used to represent the loan amount
        
            Raises: 
                ValueError: Raised when the value is equal to or lesser than zero as: 
                "Loan Amount must be positive."
        
        """
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        else:
            self.__loan_amount = loan_amount
        
    
    @property
    def rate(self):
        """
        Gets the rate 
        
        Returns:
            float: MortgageRate value 
        """
        return self.__rate
    
    @rate.setter
    def rate(self, rate: str) -> MortgageRate:
        """
        Modifies the value of rate

        validates new value against MortgageRate class
        """    
        try:
            rate = MortgageRate[str(rate)]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        self.__rate = rate

    @property
    def frequency(self):
        """
        Gets the frequency 
        
        Returns:
            int: PaymentFrequency value 
        """

        return self.__frequency
    

    @frequency.setter
    def frequency(self, frequency: str) -> PaymentFrequency:
        """
        Modifies the value of frequency

        validates new value against PaymentFrequency class
        """    
        try:
            frequency = PaymentFrequency[str(frequency)]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")

        self.__frequency = frequency

    @property
    def amortization(self):
        """
        Gets the amortization
        
        Returns:
            int: VALID_AMORTIZATION key-value 
        """
        return self.__amortization
    
    @amortization.setter
    def amortization(self, amortization: int):
        """
        Modifies the value of amortization

        validates the new value against VALID_AMORTIZATION key-values
        """
        
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        
        self.__amortization = amortization


