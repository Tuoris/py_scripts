from sys import stdout, exit
from time import sleep


def scrolling_text(text, repeats=1, space=0, delay=0.1):
    data = text + ' ' * space
    l = len(data)
    cycles = l * repeats + 1
    for shift in range(cycles):
        stdout.write(data[shift % l:] + data[:shift % l] + '\r')
        sleep(delay)
    print()


def main():
    print("Enter your string")
    text = input(">>> ").strip() + ' '
    print("Enter additional information or 'Enter' to use defaults")
    print("In format: number of repeats, additional space, delay in ms")
    add_info = input(">>> ").split()

    try:
        add_info = [int(i) for i in add_info]
    except ValueError:
        print("Input is invalid.")
        exit(0)

    if len(add_info) == 3:
        scrolling_text(text, int(add_info[0]),
                       int(add_info[1]), int(add_info[2]) / 100)
    else:
        scrolling_text(text)
    pass

if __name__ == '__main__':
    main()
