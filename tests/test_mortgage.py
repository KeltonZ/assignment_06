"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):

    def test_invalid_loan_amount(self):
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
        # Arrange

        loan = 500
        rate = "FIXED_3"
        frequency = "MONTHLY"
        validator = 5

        expected = Mortgage
        
        # Act
        result = Mortgage

        # Assert
        self.assertEqual(result, expected)
