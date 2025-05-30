#!/usr/bin/env python3
"""
Bitwise Operations Examples

This module demonstrates various bitwise operations in Python.
Bitwise operations work directly on the binary representation of numbers.
"""

def demonstrate_bitwise_operations():
    """Demonstrate basic bitwise operations with examples."""
    
    print("=== BITWISE OPERATIONS EXAMPLES ===\n")
    
    # Example numbers
    a = 12  # Binary: 1100
    b = 7   # Binary: 0111
    
    print(f"a = {a} (binary: {bin(a)})")
    print(f"b = {b} (binary: {bin(b)})\n")
    
    # AND operation (&)
    result_and = a & b
    print(f"a & b = {result_and} (binary: {bin(result_and)})")
    print("AND: 1100 & 0111 = 0100\n")
    
    # OR operation (|)
    result_or = a | b
    print(f"a | b = {result_or} (binary: {bin(result_or)})")
    print("OR:  1100 | 0111 = 1111\n")
    
    # XOR operation (^)
    result_xor = a ^ b
    print(f"a ^ b = {result_xor} (binary: {bin(result_xor)})")
    print("XOR: 1100 ^ 0111 = 1011\n")
    
    # NOT operation (~)
    result_not_a = ~a
    print(f"~a = {result_not_a} (binary: {bin(result_not_a)})")
    print("NOT: ~1100 = ...11110011 (two's complement)\n")
    
    # Left shift (<<)
    result_left_shift = a << 2
    print(f"a << 2 = {result_left_shift} (binary: {bin(result_left_shift)})")
    print("Left shift by 2: 1100 becomes 110000\n")
    
    # Right shift (>>)
    result_right_shift = a >> 2
    print(f"a >> 2 = {result_right_shift} (binary: {bin(result_right_shift)})")
    print("Right shift by 2: 1100 becomes 11\n")


def check_bit(number, position):
    """Check if a specific bit is set at the given position."""
    return bool(number & (1 << position))


def set_bit(number, position):
    """Set a bit at the given position."""
    return number | (1 << position)


def clear_bit(number, position):
    """Clear a bit at the given position."""
    return number & ~(1 << position)


def toggle_bit(number, position):
    """Toggle a bit at the given position."""
    return number ^ (1 << position)


def demonstrate_bit_manipulation():
    """Demonstrate bit manipulation functions."""
    
    print("=== BIT MANIPULATION EXAMPLES ===\n")
    
    number = 10  # Binary: 1010
    print(f"Starting number: {number} (binary: {bin(number)})\n")
    
    # Check bits
    for i in range(4):
        bit_set = check_bit(number, i)
        print(f"Bit at position {i}: {'1' if bit_set else '0'}")
    print()
    
    # Set bit at position 0
    number_set = set_bit(number, 0)
    print(f"After setting bit 0: {number_set} (binary: {bin(number_set)})")
    
    # Clear bit at position 1
    number_clear = clear_bit(number, 1)
    print(f"After clearing bit 1: {number_clear} (binary: {bin(number_clear)})")
    
    # Toggle bit at position 2
    number_toggle = toggle_bit(number, 2)
    print(f"After toggling bit 2: {number_toggle} (binary: {bin(number_toggle)})")


def convert_to_binary_string(number, width=8):
    """Convert a number to a binary string with specified width."""
    return format(number, f'0{width}b')


def demonstrate_binary_conversion():
    """Demonstrate binary conversion and representation."""
    
    print("=== BINARY CONVERSION EXAMPLES ===\n")
    
    numbers = [5, 15, 42, 128, 255]
    
    for num in numbers:
        binary_8bit = convert_to_binary_string(num, 8)
        print(f"{num:3d} = {binary_8bit} (8-bit binary)")
    
    print("\nBytes representation:")
    text = "Hi!"
    for char in text:
        ascii_val = ord(char)
        binary_rep = convert_to_binary_string(ascii_val, 8)
        print(f"'{char}' = ASCII {ascii_val} = {binary_rep}")


if __name__ == "__main__":
    demonstrate_bitwise_operations()
    print("\n" + "="*50 + "\n")
    demonstrate_bit_manipulation()
    print("\n" + "="*50 + "\n")
    demonstrate_binary_conversion()
