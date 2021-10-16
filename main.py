import ast
import chomp

def main():
    import sys
    s = sys.stdin.read()
    tree = ast.parse(s)
    print(chomp.compile(tree))


if __name__ == '__main__':
    main()
