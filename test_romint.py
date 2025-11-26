# Run with: pytest -v
import pytest
from romantointerger import roman_to_int, int_to_roman

# -----------------------------
# BASIC ROMAN NUMERALS
# -----------------------------
def test_basic_numerals():
    assert roman_to_int("I") == 1
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10
    assert roman_to_int("L") == 50
    assert roman_to_int("C") == 100
    assert roman_to_int("D") == 500
    assert roman_to_int("M") == 1000

# -----------------------------
# REPETITION OF NUMERALS
# -----------------------------
def test_repetition():
    assert roman_to_int("II") == 2
    assert roman_to_int("XX") == 20

# -----------------------------
# MANY LETTERS IN ORDER
# -----------------------------
def test_many_letters_in_order():
    assert roman_to_int("VI") == 6
    assert roman_to_int("XV") == 15

# -----------------------------
# SUBTRACTIVE NOTATION
# -----------------------------
def test_subtractive():
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("XL") == 40
    assert roman_to_int("CM") == 900
    assert roman_to_int("XIV") == 14

# -----------------------------
# INVALID CHARACTERS
# -----------------------------
def test_invalid_characters():
    assert roman_to_int("Z") == "Error: Invalid character 'Z'"
    assert roman_to_int("XIZ") == "Error: Invalid character 'Z'"

# -----------------------------
# INVALID REPETITION
# -----------------------------
def test_invalid_repetition():
    assert roman_to_int("IIII") == "Error: Invalid repetition of a numeral more than 3 times"
    assert roman_to_int("VV") == "Error: Invalid repetition of 'V', 'L', or 'D'"
    assert roman_to_int("") == "Error: Input is empty"

# -----------------------------
# INTEGER → ROMAN: VALID
# -----------------------------
def test_int_to_roman_valid():
    assert int_to_roman(1) == "I"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(14) == "XIV"
    assert int_to_roman(44) == "XLIV"
    assert int_to_roman(3999) == "MMMCMXCIX"

# -----------------------------
# INTEGER → ROMAN: INVALID
# -----------------------------
def test_int_to_roman_invalid():
    assert int_to_roman(0) == "Error: Enter an integer between 1 and 3999"
    assert int_to_roman(4000) == "Error: Enter an integer between 1 and 3999"
    assert int_to_roman(-2) == "Error: Enter an integer between 1 and 3999"
    assert int_to_roman("ABC") == "Error: Enter an integer between 1 and 3999"

# -----------------------------
# PRINT FRIENDLY MESSAGE IF ALL TESTS PASS
# -----------------------------
if __name__ == "__main__":
    # Run pytest programmatically
    result = pytest.main(["-v", __file__])
    if result == 0:
        print("\n✅ All tests passed successfully!")
