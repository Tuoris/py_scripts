from sys import stdout, exit
from time import sleep


def scrolling_text(text, repeats=2, space=1, delay=0.1):
    data = text + ' ' * space
    l = len(data)
    cycles = l * repeats + 1
    for shift in range(cycles):
        stdout.write(data[shift % l:] + data[:shift % l] + '\r')
        sleep(delay)
    print()


def main():
    print("Enter text:")
    text = input("> ").strip()
    scrolling_text(text)

if __name__ == '__main__':
    main()
