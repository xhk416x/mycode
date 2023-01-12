import argparse

def main():
    print(f"I would like {args.d} to drink!")

if __name__ == "__main__":

    # parser will read command line arguments and pass it to python
    parser= argparse.ArgumentParser(description="Allow users to choose a drink")

    # teach parser what arguments to expect
    parser.add_argument("-d", type=str, default="coffee", help="Choice of drink")

    # parser assembles all arguments into one object
    args= parser.parse_args()

    main()
