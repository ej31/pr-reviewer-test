# Test file for debugging review #335

def calculate_sum(a, b):
    # Missing type hints
    result = a + b
    return result

def process_data(data):
    # No input validation
    for item in data:
        print(item)
    return data

# Unused import simulation
import os
import sys

if __name__ == "__main__":
    print(calculate_sum(1, 2))
