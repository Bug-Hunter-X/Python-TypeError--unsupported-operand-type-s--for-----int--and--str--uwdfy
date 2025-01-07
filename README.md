# Python TypeError: unsupported operand type(s) for /: 'int' and 'str'
This repository contains a simple Python program demonstrating a common yet easily overlooked TypeError.  The error arises when attempting to perform division involving incompatible data types (specifically, an integer and a string).  The solution showcases proper exception handling to gracefully manage such situations.

## Bug Description
The primary issue lies in the lack of robust type checking.  The function doesn't explicitly validate input types, leading to a runtime error when an integer is divided by a string. 

## Solution
The solution incorporates a `try-except` block to catch the `TypeError` and provide informative error messages, preventing program crashes.