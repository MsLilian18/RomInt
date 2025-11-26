import re

# Roman to Integer Function

def roman_to_int(s):
    if not s or s.strip() == "":
        return "Error: Input is empty"

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    valid_subtractive = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}

    total = 0
    i = 0

    for char in s:
        if char not in roman:
            return f"Error: Invalid character '{char}'"

    if re.search(r'(I{4}|X{4}|C{4}|M{4})', s):
        return "Error: Invalid repetition of a numeral more than 3 times"
    if "VV" in s or "LL" in s or "DD" in s:
        return "Error: Invalid repetition of 'V', 'L', or 'D'"

    while i < len(s):
        if i == len(s) - 1:
            total += roman[s[i]]
            break

        current = roman[s[i]]
        nxt = roman[s[i + 1]]

        if current < nxt:
            if s[i] not in valid_subtractive or s[i + 1] not in valid_subtractive[s[i]]:
                return f"Error: Invalid subtractive pair '{s[i]}{s[i + 1]}'"
            total += nxt - current
            i += 2
        else:
            total += current
            i += 1

    return total



# Integer to Roman Function

def int_to_roman(num):
    if not isinstance(num, int) or num <= 0 or num > 3999:
        return "Error: Enter an integer between 1 and 3999"

    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = ""
    for val, symbol in val_map:
        while num >= val:
            result += symbol
            num -= val
    return result


# AUTOMATED TEST CASES


# Roman -> Integer Tests
assert roman_to_int("I") == 1
assert roman_to_int("V") == 5
assert roman_to_int("X") == 10
assert roman_to_int("L") == 50
assert roman_to_int("C") == 100
assert roman_to_int("D") == 500
assert roman_to_int("M") == 1000

assert roman_to_int("XI") == 11
assert roman_to_int("IV") == 4
assert roman_to_int("XIV") == 14
assert roman_to_int("II") == 2

assert roman_to_int("Z") == "Error: Invalid character 'Z'"
assert roman_to_int("XIZ") == "Error: Invalid character 'Z'"
assert roman_to_int("VV") == "Error: Invalid repetition of 'V', 'L', or 'D'"
assert roman_to_int("") == "Error: Input is empty"
assert roman_to_int("IIII") == "Error: Invalid repetition of a numeral more than 3 times"

# Integer -> Roman Tests
assert int_to_roman(1) == "I"
assert int_to_roman(4) == "IV"
assert int_to_roman(9) == "IX"
assert int_to_roman(14) == "XIV"
assert int_to_roman(44) == "XLIV"
assert int_to_roman(3999) == "MMMCMXCIX"

assert int_to_roman(0) == "Error: Enter an integer between 1 and 3999"
assert int_to_roman(4000) == "Error: Enter an integer between 1 and 3999"
assert int_to_roman(-5) == "Error: Enter an integer between 1 and 3999"
assert int_to_roman("X") == "Error: Enter an integer between 1 and 3999"

print("All automated test cases passed! ✅\n")


# Yes/No Prompt Helper

def yes_no_prompt(message):
    while True:
        choice = input(message + " (y/n): ").strip().lower()
        if choice in ["y", "n"]:
            return choice
        else:
            print("Please enter 'y' or 'n'.")



# Interactive Mode

if __name__ == "__main__":
    print("🧮 Roman ↔ Integer Converter")
    print("Choose a mode once. Type 'exit' anytime to quit.\n")

    mode = input("Choose conversion (1: Roman to Int, 2: Int to Roman): ").strip()
    if mode.lower() == "exit":
        if yes_no_prompt("Do you really want to exit?") == "y":
            print("Goodbye! 👋")
            exit()

    while True:
        if mode == "1":  # Roman → Integer
            user_input = input("\nEnter a Roman numeral: ").strip().upper()
            if user_input.lower() == "exit":
                if yes_no_prompt("Do you really want to exit?") == "y":
                    switch = yes_no_prompt("Do you want to switch to Integer → Roman mode?")
                    if switch == "y":
                        mode = "2"
                        continue
                    else:
                        print("Goodbye! 👋")
                        break
                else:
                    continue
            print(f"Result: {roman_to_int(user_input)}")

        elif mode == "2":  # Integer → Roman
            user_input = input("\nEnter an integer (1-3999): ").strip()
            if user_input.lower() == "exit":
                if yes_no_prompt("Do you really want to exit?") == "y":
                    switch = yes_no_prompt("Do you want to switch to Roman → Integer mode?")
                    if switch == "y":
                        mode = "1"
                        continue
                    else:
                        print("Goodbye! 👋")
                        break
                else:
                    continue
            if not user_input.isdigit():
                print("Error: Please enter a valid integer")
                continue
            print(f"Result: {int_to_roman(int(user_input))}")

        else:
            print("Invalid mode. Restart the program and choose 1 or 2.")
            break
