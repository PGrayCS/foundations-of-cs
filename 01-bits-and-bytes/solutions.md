# Bits and Bytes Solutions

## Exercise 1: Binary Representation
1. 13 = **1101**
2. 27 = **11011**
3. 64 = **1000000**
4. 100 = **1100100**
5. 255 = **11111111**

## Exercise 2: Decimal Conversion
1. 1011 = **11**
2. 11010 = **26**
3. 101010 = **42**
4. 11111111 = **255**
5. 10000000 = **128**

## Exercise 3: Bitwise Operations
Given `a = 25` (binary: 11001) and `b = 19` (binary: 10011):

1. `a & b` = 25 & 19 = **17** (binary: 10001)
2. `a | b` = 25 | 19 = **27** (binary: 11011)
3. `a ^ b` = 25 ^ 19 = **10** (binary: 1010)
4. `~a` = ~25 = **-26** (two's complement)
5. `a << 2` = 25 << 2 = **100** (binary: 1100100)
6. `b >> 1` = 19 >> 1 = **9** (binary: 1001)

## Exercise 4: Bit Manipulation

```python
def check_bit(number, position):
    """Check if the nth bit is set."""
    return bool(number & (1 << position))

def set_bit(number, position):
    """Set the nth bit."""
    return number | (1 << position)

def clear_bit(number, position):
    """Clear the nth bit."""
    return number & ~(1 << position)

def toggle_bit(number, position):
    """Toggle the nth bit."""
    return number ^ (1 << position)

def count_set_bits(number):
    """Count the number of set bits."""
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count
    
    # Alternative using Brian Kernighan's algorithm:
    # count = 0
    # while number:
    #     number &= number - 1  # Clears the lowest set bit
    #     count += 1
    # return count
```

## Exercise 5: Practical Applications

### 1. Power of 2 Check
```python
def is_power_of_two(n):
    """Check if a number is a power of 2."""
    return n > 0 and (n & (n - 1)) == 0
```

### 2. Swap Without Temp
```python
def swap_xor(a, b):
    """Swap two numbers using XOR."""
    if a != b:  # Avoid swapping same memory location
        a = a ^ b
        b = a ^ b
        a = a ^ b
    return a, b
```

### 3. ASCII to Binary
```python
def string_to_binary(text):
    """Convert string to binary representation."""
    for char in text:
        ascii_val = ord(char)
        binary = format(ascii_val, '08b')
        print(f"'{char}' = ASCII {ascii_val} = {binary}")
```

### 4. Color Values
```python
def extract_rgb(color_24bit):
    """Extract RGB components from 24-bit color."""
    red = (color_24bit >> 16) & 0xFF
    green = (color_24bit >> 8) & 0xFF
    blue = color_24bit & 0xFF
    return red, green, blue

def combine_rgb(red, green, blue):
    """Combine RGB values into 24-bit color."""
    return (red << 16) | (green << 8) | blue
```

## Exercise 6: Byte Operations

1. **8 bits** are in a byte
2. Value ranges:
   - 1 byte (unsigned): **0 to 255** (2^8 - 1)
   - 2 bytes (unsigned): **0 to 65,535** (2^16 - 1)
   - 4 bytes (unsigned): **0 to 4,294,967,295** (2^32 - 1)
3. -5 in 8-bit two's complement: **11111011**
   - Step 1: 5 in binary = 00000101
   - Step 2: Invert bits = 11111010
   - Step 3: Add 1 = 11111011

## Exercise 7: Memory Calculations

1. Memory needed:
   - 1000 boolean values: **1000 bits = 125 bytes** (minimum, though often stored as 1000 bytes)
   - 50 ASCII characters: **50 bytes**
   - 100 32-bit integers: **400 bytes** (100 × 4 bytes)

2. 1 GB for 32-bit integers:
   - 1 GB = 1,073,741,824 bytes
   - Each integer = 4 bytes
   - Total integers: **268,435,456 integers**

## Bonus Challenge: Bit Packing

```python
def pack_person_data(age, gender, department_id):
    """Pack person data into 16-bit integer.
    
    Layout: [unused:1][age:7][gender:1][department_id:4][unused:3]
    """
    if not (0 <= age <= 127):
        raise ValueError("Age must be 0-127")
    if not (0 <= gender <= 1):
        raise ValueError("Gender must be 0 or 1")
    if not (0 <= department_id <= 15):
        raise ValueError("Department ID must be 0-15")
    
    # Pack: age in bits 8-14, gender in bit 7, dept_id in bits 3-6
    packed = (age << 8) | (gender << 7) | (department_id << 3)
    return packed

def unpack_person_data(packed):
    """Unpack person data from 16-bit integer."""
    age = (packed >> 8) & 0x7F        # Extract bits 8-14 (7 bits)
    gender = (packed >> 7) & 0x01      # Extract bit 7 (1 bit)
    department_id = (packed >> 3) & 0x0F  # Extract bits 3-6 (4 bits)
    
    return age, gender, department_id

# Test cases
def test_bit_packing():
    test_cases = [
        (25, 1, 5),   # Age 25, Female, Dept 5
        (127, 0, 15), # Age 127, Male, Dept 15
        (0, 1, 0),    # Age 0, Female, Dept 0
    ]
    
    for age, gender, dept in test_cases:
        packed = pack_person_data(age, gender, dept)
        unpacked = unpack_person_data(packed)
        print(f"Original: ({age}, {gender}, {dept})")
        print(f"Packed: {packed} (binary: {bin(packed)})")
        print(f"Unpacked: {unpacked}")
        print(f"Match: {(age, gender, dept) == unpacked}")
        print()
```
