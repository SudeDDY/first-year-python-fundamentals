# Data Processing & Statistics Tool

A Python script designed to parse, clean, and analyze raw text data from different sources.

## Features
1.  **Student Performance Analysis:**
    - Reads raw student data (names, houses, scores).
    - Cleans malformed lines and parses scores.
    - Calculates passing rates, averages, and identifies the top student.
    - Groups students by "House" (e.g., House Ignis, House Terra).

2.  **Inventory Management:**
    - Parses inventory items (name + weight).
    - Handles unit conversion and string cleaning (removing "kg", "*", "-").
    - Calculates total weight and identifies the heaviest item.

## Technologies Used
- String Manipulation (`strip`, `split`, `replace`)
- Data Structures (Lists, Tuples)
- Exception Handling (`try/except`)
- Formatted Output