"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage_doc.mortgage import Mortgage, __init__
from mortgage_doc.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    
    #def setUp(self):                                               # wrote this to potentially solve an issue, but was found to not be necessary, keeping just in case
        #self.mortgage = Mortgage(500, "FIXED_3", "MONTHLY", 5) 

    
    #Accessor tests:
    #loan amount
    #rate
    #frequency
    #amortization

    def test_loan_amount_accessor(self):
        """
        Tests and confirms the functionality of the loan amount accessor

        Mortgage needs all 4 attributes declared to function

        loan: 
            has to be equal to Mortgage in order assign loan_amount attribute a value to the loan variable, 
            which is then compared to the expected result of 500.00
        """
        #Arrange
        loan = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        #Act & Assert
        self.assertEqual(loan.loan_amount, 500.00)

    def test_rate_accessor(self):
        """
        Tests and confirms the functionality of the rate accessor

        Mortgage needs all 4 attributes declared to function

        rates:
            has to be equal to Mortgage in order assign rate attribute a value to the rates variable, 
            which is then compared to the expected result of MortgageRate.FIXED_#
        """
        
        #Arrange
        rates = Mortgage(500, "FIXED_3", "MONTHLY", 5)

        #Act & Assert
        self.assertEqual(rates.rate, MortgageRate.FIXED_3)
    
    def test_frequency_accessor(self):
        """
        Tests and confirms the functionality of the frequency accessor

        Mortgage needs all 4 attributes declared to function

        frequencies:
            has to be equal to Mortgage in order assign frequency attribute a value to the frequencies variable, 
            which is then compared to the expected result of PaymentFrequency.#Valid_Member
        """
        #Arrange
        frequencies = Mortgage(500, "FIXED_3", "MONTHLY", 5)

        #Act & Assert
        self.assertEqual(frequencies.frequency, PaymentFrequency.MONTHLY)
    
    def test_amortization_accessor(self):
        """
        Tests and confirms the functionality of the amortization accessor

        Mortgage needs all 4 attributes declared to function

        validator:
            has to be equal to Mortgage in order assign amortization attribute a value to the validator variable, 
            which is then compared to the expected result of 5 which is a valid Key-value
        """

        #Arrange
        validator = Mortgage(500, "FIXED_3", "MONTHLY", 5)

        #Act & Assert
        self.assertEqual(validator.amortization, 5)


    #Input tests
    #Invalid loan amount
    #Invalid rate
    #Invalid frequency
    #Invalid amortization
    #Valid attribute inputs

    def test_invalid_loan_amount(self):
        """
        Tests to confirm that ValueError is raised when an value that is lesser or equal to 
        zero is given to the loan_amount attribute of the Mortgage class

        Args:
            loan:
                represents the invalid value for loan_amount attribute
            rate:
                represents the value for rates attribute
            frequency:
                represents the value for frequency attribute
            validator:
                represents the value for amortization attribute
        """
        # Arrange
        loan = -500
        rate = "FIXED_3"
        frequency = "MONTHLY"
        validator = 5

        expected = "Loan Amount must be positive."
    
        # Act & Assert

        with self.assertRaises(ValueError) as context:
            Mortgage(loan, rate, frequency, validator)
        self.assertEqual(str(context.exception), (expected))

    def test_invalid_rate(self):
        """
        Tests to confirm that ValueError is raised when an value that is not in the MortgageRate class 
        is given to the rate attribute of the Mortgage class

        Args:
            loan:
                represents the value for loan_amount attribute
            rate:
                represents the invalid value for rates attribute
            frequency:
                represents the value for frequency attribute
            validator:
                represents the value for amortization attribute
        """
        # Arrange
        
        loan = 500
        rate = "FIXED_2"
        frequency = "MONTHLY"
        validator = 5

        expected = "Rate provided is invalid."

        # Act and Assert

        with self.assertRaises(ValueError) as context:
            Mortgage(loan, rate, frequency, validator)
        self.assertEqual(str(context.exception), (expected))
    
    def test_invalid_frequency(self):
        """
        Tests to confirm that ValueError is raised when an value that is not in the PaymentFrequency class 
        is given to the frequency attribute of the Mortgage class

        Args:
            loan:
                represents the value for loan_amount attribute
            rate:
                represents the  value for rates attribute
            frequency:
                represents the invalid value for frequency attribute
            validator:
                represents the value for amortization attribute
        """
        # Arrange 
        
        loan = 500
        rate = "FIXED_3"
        frequency = "BI_MONTHLY"
        validator = 5

        expected = "Frequency provided is invalid."

        # Act & Assert

        with self.assertRaises(ValueError) as context:
            Mortgage(loan, rate, frequency, validator)
        self.assertEqual(str(context.exception), (expected))

    def test_invalid_amortization(self):
        """
        Tests to confirm that ValueError is raised when an value that is not in the VALID_AMORTIZATION set 
        is given to the amortization attribute of the Mortgage class

        Args:
            loan:
                represents the value for loan_amount attribute
            rate:
                represents the  value for rates attribute
            frequency:
                represents the value for frequency attribute
            validator:
                represents the invalid value for amortization attribute
        """
        # Arrange

        loan = 500
        rate = "FIXED_3"
        frequency = "MONTHLY"
        validator = 6

        expected = "Amortization provided is invalid."

        # Act & Assert

        with self.assertRaises(ValueError) as context:
            Mortgage(loan, rate, frequency, validator)
        self.assertEqual(str(context.exception), (expected))

    def test_valid_attributes(self):
        """
        Tests to confirm that valid inputs are accepted for the Mortgage class

        Args:
            loan:
                represents the value for loan_amount attribute
            rate:
                represents the  value for rates attribute
            frequency:
                represents the value for frequency attribute
            amortization:
                represents the value for amortization attribute
        """
        # Arrange

        loan_amount = 500.0
        rate = "FIXED_3"
        frequency = "MONTHLY"
        amortization = 5
        
        # Act
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
    

        # Assert
        self.assertEqual(loan_amount, mortgage.loan_amount)
        self.assertEqual(MortgageRate.FIXED_3, mortgage.rate)
        self.assertEqual(PaymentFrequency.MONTHLY, mortgage.frequency)
        self.assertEqual(amortization, mortgage.amortization)

    
    #Mutators tests
    #loan amount negative
    #loan amount equals zero
    #loan amount valid change
    #rate valid change
    #rate invalid change
    #frequency valid 
    #frequency invalid change
    #amortization valid change
    #amortization invalid change

    def test_loan_amount_mutator_negative_amount(self):
        """
        tests to confirm the functionality of the loan_amount mutator, and that a negative value,
        would raise a valueError. 
        """
        #Arrange
        mortgage = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        expected = "Loan Amount must be positive."

        #Act & Assert
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -500
        self.assertEqual(expected, str(context.exception))


    def test_loan_amount_mutator_amount_equals_zero(self):
        """
        tests to confirm the functionality of the loan_amount mutator, and that a value equal to zero,
        would raise a valueError. 
        """
        #Arrange
        mortgage = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        expected = "Loan Amount must be positive."

        #Act & Assert
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0
        self.assertEqual(expected, str(context.exception))
    
    def test_loan_amount_mutator_valid_amount(self):
        """
        tests to confirm the functionality of the loan_amount mutator, and that the new value is properly applied
        """
        #Arrange
        mortgage = Mortgage(1000, "FIXED_3", "MONTHLY", 5)
        expected = 500.00

        #Act
        mortgage.loan_amount = 500

        #Assert
        self.assertEqual(expected, mortgage.loan_amount)

    def test_rate_mutator_valid(self):
        """
        tests to confirm the functionality of the rate mutator, and that the new value is properly applied
        """
        #Arrange
        valid_rate = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        expected = MortgageRate.FIXED_5

        #Act
        valid_rate.rate = "FIXED_5"

        #Assert
        self.assertEqual(expected, valid_rate.rate)
    
    def test_rate_mutator_valueError(self):
        """
        tests to confirm the functionality of the rate mutator and that a valueError is raised when
        an invalid value is applied
        """
        #Arrange
        invalid_rate = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        expected = "Rate provided is invalid."

        #Act & Assert
        with self.assertRaises(ValueError) as context:
            invalid_rate.rate = "FIXED_2"
        self.assertEqual(expected, str(context.exception))

    def test_frequency_mutator_valid(self):
        """
        tests to confirm the functionality of the frequency mutator, and that the new value is properly applied
        """
        #Arrange
        valid_frequency = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        expected = PaymentFrequency.BI_WEEKLY

        #Act
        valid_frequency.frequency = "BI_WEEKLY"

        #Assert
        self.assertEqual(expected, valid_frequency.frequency)
    
    def test_frequency_mutator_valueError(self):
        """
        tests to confirm the frequency of the rate mutator and that a valueError is raised when
        an invalid value is applied
        """
        #Arrange
        invalid_frequency = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        expected = "Frequency provided is invalid."

        #Act & Assert 
        with self.assertRaises(ValueError) as context:
            invalid_frequency.frequency = "TRI_WEEKLY"
        self.assertEqual(expected, str(context.exception))

    def test_amortization_mutator_valid(self):
        """
        tests to confirm the amortization of the loan_amount mutator, and that the new value is properly applied
        """
        #Arrange
        valid_amort = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        expected = 20

        #Act
        valid_amort.amortization = 20

        self.assertEqual(expected, valid_amort.amortization)

    def test_amortization_mutator_valueError(self):
        """
        tests to confirm the amortization of the rate mutator and that a valueError is raised when
        an invalid value is applied
        """
        #Arrange
        invalid_amort = Mortgage(500, "FIXED_3", "MONTHLY", 5)
        expected = "Amortization provided is invalid."

        #Act & Assert
        with self.assertRaises(ValueError) as context:
            invalid_amort.amortization = 6
        self.assertEqual(expected, str(context.exception))