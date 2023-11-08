#!/usr/bin/python3
# 100-my_calculator.py

if __name__ == "__main__":
    # This script handles basic arithmetic operations.
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        # Check if the correct number of arguments is provided.
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Define the available operators.
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        # Check if the operator is valid.
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Parse the input arguments.
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Perform the requested operation and display the result.
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
