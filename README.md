Roman <-> Integer Converter

Overview

This project is a Python-based Roman numeral and integer converter.
It allows users to:

Convert Roman numerals to integers.

Convert integers to Roman numerals (1–3999).

The project also includes automated test cases to ensure accuracy.

Features

Bidirectional conversion: Roman → Integer and Integer → Roman.

Input validation:

Detects invalid characters in Roman numerals.

Checks invalid repetitions of numerals (e.g., IIII or VV).

Ensures integers are within the valid range (1–3999).

Interactive mode: Users can switch between conversion modes or exit gracefully.

Automated tests: Use pytest to verify all conversions and edge cases.

Friendly error messages guide the user when input is invalid.

Installation

Clone the repository:

git clone https://github.com/your-username/roman-integer-converter.git


Navigate to the project folder:

cd roman-integer-converter


Install dependencies (only pytest is required for testing):

pip install pytest

Usage
Interactive Mode

Run the main script:

python romtoint.py


Choose conversion mode:

1 → Roman to Integer

2 → Integer to Roman

Enter your value.

Type exit anytime to quit or switch modes.

Automated Testing

Run all test cases using pytest:

pytest -v


If all tests pass, you will see:

✅ All tests passed successfully!

Examples
Roman → Integer
roman_to_int("XIV")  # Output: 14
roman_to_int("CM")   # Output: 900

Integer → Roman
int_to_roman(44)     # Output: XLIV
int_to_roman(3999)   # Output: MMMCMXCIX

Invalid Input
roman_to_int("IIII")   # Output: Error: Invalid repetition of a numeral more than 3 times
int_to_roman(4000)     # Output: Error: Enter an integer between 1 and 3999
