from file_handling.iter_down import initialize_iter
from file_handling.wdog import initialize_watching

def main():
    option = int(input('[1] iter [2] watch\n'))
    if option == 1:
        initialize_iter()
    elif option == 2:
        initialize_watching()
    else:
        main()

if __name__ == '__main__':
    main()