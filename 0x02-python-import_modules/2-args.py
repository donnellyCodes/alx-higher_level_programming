#!/usr/bin/python3
# sys is used to access list of command line arguments passed to it
if __name__ == "__main__":
    import sys
    # to determine number of arguments
    argc = len(sys.argv) - 1
    if argc == 0:
        print("O arguments.")
    elif argc == 1:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{argc} arguments:")
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")
