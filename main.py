import ast
import chomp

def main():
    import sys
    s = sys.stdin.read()
    net = chomp.compile(s)
    print(net)


if __name__ == '__main__':
    main()
