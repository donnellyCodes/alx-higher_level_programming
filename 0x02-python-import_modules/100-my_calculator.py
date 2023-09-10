#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    # check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if len(sys.argv) == 4:
        # extract command line arguments
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
        # performing operaion based on operator
        if operator == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif operator == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif operator == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
