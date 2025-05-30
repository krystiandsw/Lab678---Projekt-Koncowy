import argparse

def main():
    parser = argparse.ArgumentParser(description='Convert files between .json, .xml, and .yaml formats')
    parser.add_argument('source', help='Source file path')
    parser.add_argument('target', help='Target file path')
    args = parser.parse_args()

    print(f"Source file: {args.source}")
    print(f"Target file: {args.target}")

if __name__ == "__main__":
    main()