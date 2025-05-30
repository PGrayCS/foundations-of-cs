# Bits and Bytes Exercises

## Exercise 1: Binary Representation
Convert the following decimal numbers to binary:
1. 13
2. 27
3. 64
4. 100
5. 255

## Exercise 2: Decimal Conversion
Convert the following binary numbers to decimal:
1. 1011
2. 11010
3. 101010
4. 11111111
5. 10000000

## Exercise 3: Bitwise Operations
Given `a = 25` and `b = 19`, calculate:
1. `a & b` (AND)
2. `a | b` (OR)
3. `a ^ b` (XOR)
4. `~a` (NOT a)
5. `a << 2` (left shift a by 2)
6. `b >> 1` (right shift b by 1)

## Exercise 4: Bit Manipulation
Write functions to:
1. Check if the nth bit of a number is set
2. Set the nth bit of a number
3. Clear the nth bit of a number
4. Toggle the nth bit of a number
5. Count the number of set bits in a number

## Exercise 5: Practical Applications
1. **Power of 2 Check**: Write a function that determines if a number is a power of 2 using bitwise operations.

2. **Swap Without Temp**: Write a function that swaps two numbers without using a temporary variable (hint: use XOR).

3. **ASCII to Binary**: Write a program that takes a string and displays each character's ASCII value and its 8-bit binary representation.

4. **Color Values**: RGB colors are often represented as 24-bit values (8 bits each for red, green, blue). Write functions to:
   - Extract the red, green, and blue components from a 24-bit color value
   - Combine separate R, G, B values into a single 24-bit color value

## Exercise 6: Byte Operations
1. How many bits are in a byte?
2. What is the range of values that can be stored in:
   - 1 byte (unsigned)
   - 2 bytes (unsigned)
   - 4 bytes (unsigned)
3. How would you represent the number -5 in 8-bit two's complement?

## Exercise 7: Memory Calculations
1. How much memory is needed to store:
   - 1000 boolean values
   - A string of 50 characters (ASCII)
   - An array of 100 integers (32-bit each)
2. If you have 1 GB of RAM, approximately how many 32-bit integers can you store?

## Bonus Challenge: Bit Packing
Design a system to pack multiple small values into a single integer:
- Store a person's age (0-127), gender (0-1), and department ID (0-15) in a single 16-bit integer
- Write functions to pack and unpack these values
- Demonstrate your solution with test cases
