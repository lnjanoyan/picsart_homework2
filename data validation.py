import validators


def email():
    if val.count('@') == 1:
        main = val.split('@')[0]
        domain = val.split('@')[1]
        dom_half = domain.split('.')
        if domain.count('.') == 1 and len(domain) >= 3 and len(main) >= 1 \
                and dom_half[0].isalpha() and dom_half[1].isalpha():
            for i in '`!#$%^&*()=:;][{}?/':
                if i in main:
                    break
            else:
                print('Valid email')
            return
        else:
            print('Invalid email')
            return
    print('Invalid email')


def website(val):
    if '://' not in val:
        val = 'http://' + val
    valid = validators.url(val)
    if valid:
        print("Valid URL")
    else:
        print("Invalid URL")


def card():
    num = val.replace(' ', '')
    if len(num) == 16 and num.isdigit():
        print("Valid credit card number")
    else:
        print('Invalid credit card number')


def date():
    repl = val.replace('.', ' ').replace(',', ' ').replace('/', ' ')
    ls = []
    try:
        for i in range(len(repl.split())):
            ls.append(int(repl.split()[i]))
    except ValueError:
        print('Non number value found!!!')
    else:
        print(ls)
        if len(ls) == 3:
            if (ls[2] > 0 and len(str(ls[2])) <= 4 and ls[1] in [1, 3, 5, 7, 8, 10, 12] and 1 <= ls[0] <= 31) or (
                    ls[2] > 0 and len(str(ls[2])) <= 4 and ls[1] in [4, 6, 9, 11] and 1 <= ls[0] <= 30) or (
                    ls[2] > 0 and len(str(ls[2])) <= 4 and ls[1] == 2 and 1 <= ls[0] <= 28):
                print('Valid date')
            else:
                print('Invalid date')
        else:
            print('Please type only one of this forms: 01.12.2023 or 01/12/2023 or 01,12,2023 or 01 12 2023')


def number():
    if val.isdigit() and int(val) >= 0:
        print('Valid Number')
    else:
        print('Invalid Number')


def phone():
    ph_num = val.replace(' ', '')
    if (ph_num.startswith('+374') and len(ph_num) == 12 and ph_num[1:].isdigit()) or (
            ph_num.startswith('0') and len(ph_num) == 9 and ph_num.isdigit()):
        print('Valid phone number')
    else:
        print('Invalid phone number')


while True:
    print(
        '\nHere are 6 types of data checking, please choose one of the options: \n1 - Email\n2 - Website URL\n3 - '
        'Date\n4 - Number\n5 - Credit Card Number\n6 - Mobile Phone Number\n7 - For ending program\n ')
    choice = input("Your option: ")
    val = input('Enter your value for checking: ')
    if choice == '1':
        email()
    elif choice == '2':
        website(val)
    elif choice == '3':
        date()
    elif choice == '4':
        number()
    elif choice == '5':
        card()
    elif choice == '6':
        phone()
    elif choice == '7':
        print('Program ended!')
        break
    else:
        print('Please type only one of these numbers. ')
