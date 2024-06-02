class Solution:
    def romanToDecimal(self, S): 
        # code here
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in S:
            # Get the value of the current Roman numeral
            value = roman_values[char]
            
            # If the current value is greater than the previous value, subtract twice the previous value
            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            
            # Update the previous value
            prev_value = value
        
        return total