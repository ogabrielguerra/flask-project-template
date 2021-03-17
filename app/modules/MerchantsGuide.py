import re


class MerchantsGuide:

    def __init__(self):
        self.units = {
            "prok": "V",
            "glob": "I",
            "pish": "X",
            "tegj": "L"
        }

        self.credits = {
            "Silver": 17,
            "Gold": 14450,
            "Iron": 195.5
        }

        self.romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def converter(self, str_query):
        print("QUERY: " + str_query)

        terms = str_query.split(" ")
        roman_string = ""
        multiplier = ""

        # Empty query not allowed
        if str_query == "":
            print("LOG: Empty query")
            return False

        # Check dialect
        if self.is_valid_dialect(str_query) is False:
            print("LOG: Invalid query " + str_query)
            return False

        # Process units that are not Credits(Silver, Gold or Iron)
        for term in terms:
            if self.is_valid_unit(term):
                # Adds a char to string
                roman_string += self.units.get(term.strip())
            elif self.is_valid_multiplier(term):
                # Allows only one multiplier
                if multiplier == "":
                    multiplier = term

        if self.is_valid_roman(roman_string) is False:
            print("Invalid Roman")
            return False

        # Calc value of roman string
        roman_value = self.get_roman_value(roman_string)
        result = roman_value * self.credits.get(multiplier) if multiplier != "" else roman_value

        return result

    # Checks if str is a valid Roman
    def is_valid_roman(self, str):
        if str == "":
            print("empty string")
            return False

        pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
        res = re.search(pattern, str)

        if res is None or res == "":
            print("Invalid Roman")
            return False

        return True

    # Checks if is a valid unit
    def is_valid_unit(self, test):
        if test in self.units and test != "":
            return True

        return False

    # Checks if is a valid multiplier
    def is_valid_multiplier(self, test):
        if test in self.credits and test != "":
            return True
        else:
            print("Not a valid multiplier " + test)
            return False

    # Returns the single value of a char in Romans
    def get_char_value(self, char):
        return self.romans.get(char)

    # Defines the proper operation (sum / subtraction)
    def sum_or_subtract(self, c, last):
        if self.get_char_value(c) <= last:
            return last
        else:
            return last * -1

    # Calcs a Roman number's value
    def get_roman_value(self, numeral):
        i = 1
        last = 0
        roman_value = 0

        if len(numeral) > 1:
            for c in numeral:
                # is the first iteration?
                if i == 1:
                    last = self.get_char_value(c)

                elif i > 1 and i != len(numeral):
                    roman_value += self.sum_or_subtract(c, last)
                    last = self.get_char_value(c)

                # is the last?
                elif i == len(numeral):
                    roman_value += self.sum_or_subtract(c, last)
                    roman_value += self.get_char_value(c)

                i += 1

        else:
            roman_value = self.romans.get(numeral)

        print("Roman value: " + str(roman_value))
        return roman_value

    # Checks if is a valid query
    def is_valid_dialect(self, str_term):
        terms = str_term.split(" ")

        # Check if term exists in units
        for term in terms:
            if self.is_valid_unit(term) is False and self.is_valid_multiplier(term) is False:
                return False

        return True

    def url_to_query(self, query):

        query = query.split(",")
        prepQuery = ""

        if len(query) == 1:
            prepQuery = ''.join(query).strip()

        else:
            for term in query:
                prepQuery += term + " "

        prepQuery = prepQuery.strip()

        return prepQuery
