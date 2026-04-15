import sys


def main():
    """
    Function to print arguments and number of them
    """
    print("=== Command Quest ===")
    argv = sys.argv
    argc = len(argv)

    if argc == 1:
        print("No arguments provided!")

    print(f"Program name: {argv[0]}")

    if argc > 1:
        print(f"Arguments received: {argc - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {argv[i]}")
            i += 1

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
