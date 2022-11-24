import os
import sys



def number():
    num_range = list(range(1, 31))
    print('========================================')
    print("choose number between 1-30")
    print('========================================')


    user_num = int(input('num: ')) 
    if (user_num in num_range == False):
        print('Number not in range')
        os.execl(sys.executable, sys.executable, *sys.argv)

    print(' ')

    print("is your number divisible by 5?")
    print('------------------------------')
    div_5 = input('Y/N: ').capitalize()
    if div_5 == 'Y' and user_num % 5 == 0:
        print('Is your number bellow 20?')
        print('-------------------------')
        bel_20 = input('Y/N: ').capitalize()

        if bel_20 == 'Y' and user_num < 20:
            print('Is your number a multiple of 3?')
            print('-------------------------------')
            mul_3 = input('Y/N: ').capitalize()
            if mul_3 == 'Y' and user_num % 3 == 0:
                    print('Your number is 15')
                    print(user_num)
                    sys.exit
            else:
                print('Is your number divisible by 2?')
                print('------------------------------')
                div_2 = input('Y/N: ').capitalize()
                if div_2 == 'Y':
                    print('Your number is 10')
                    print(user_num)
                    sys.exit
                else:
                    print('Your number is 5')
                    print(user_num)
                    sys.exit
        else:
            if user_num > 20 == False:
                    print('Wrong - try again')
                    os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                if user_num >= 20:
                    print('Is your number divisible by 2?')
                    print('------------------------------')
                    div_2v2 = input('Y/N: ').capitalize()
                    if div_2v2 == 'Y':
                        print('Is your number divisible by 3?')
                        print('------------------------------')
                        div_3v2 = input('Y/N: ').capitalize()
                        if div_3v2 == 'Y' and user_num % 3 == 0:
                            print('Your number is 30')
                            print(user_num)
                        else:
                            print('Your number is 20')
                            print(user_num)
                    else:
                        print('Your number is 25')
                        print(user_num)   
    else: 
        for elements1 in num_range:
            if elements1 % 5 == 0:
                num_range.remove(elements1)
            new_num_range1 = num_range
        print(new_num_range1)
        print('||||||||||||||||||')
        print('NOT DIVISIBLE BY 5')
        print('||||||||||||||||||')

    print(' ')

    print('Is your number divisible by 7?')
    print('------------------------------')
    div_7 = input('Y/N: ').capitalize()
    if div_7 == 'Y' and user_num % 7 == 0:
        print('Is your number odd?')
        print('-------------------')
        odd_7 = input('Y/N: ').capitalize()
        if odd_7 == 'Y' and user_num % 2 != 0:
            print('Is your number a multiple of 3?')
            print('-------------------------------')
            mul_3v7 = input('Y/N: ').capitalize()
            if mul_3v7 == 'Y':
                print('Your number is 21')
                print(user_num)
                sys.exit
            else:
                if mul_3v7 == 'N':
                    print('Your number is 7')
                    print(user_num)
                    sys.exit
        else:
            print('Is your number bellow 20?')
            print('-------------------------')
            bel_20v2 = input('Y/N: ').capitalize()
            if bel_20v2 == 'Y':
                print('Your number is 14')
                print(user_num)
                sys.exit
            else:
                print('Your number is 28')
                print(user_num)
    else:
        for elements2 in num_range:
            if elements2 % 7 == 0:
                num_range.remove(elements2)
            new_num_range2 = num_range
        print(new_num_range2)
        print('||||||||||||||||||')
        print('NOT DIVISIBLE BY 7')
        print('||||||||||||||||||')

    print(' ')  

    print('Is your number divisible by 3?')
    print('------------------------------')
    div_3v3 = input('Y/N: ').capitalize()
    if div_3v3 == 'Y' and user_num % 3 == 0:
        print('Is your number odd?')
        print('-------------------')
        odd_3 = input('Y/N: ').capitalize()
        if odd_3 == 'Y' and user_num % 2 != 0: 
            print('Is your number above 5?')
            print('-----------------------')
            abv_5 = input('Y/N: ').capitalize()
            if abv_5 == 'Y':
                print('Your number is 9')
                print(user_num)
                sys.exit
            else:
                print('Your number is 3')
                print(user_num)
                sys.exit
        else:
            print('Is your below above 20?')
            print('-------------------------')
            bel_20v3 = input('Y/N: ').capitalize()
            if bel_20v3 == 'Y':
                print('Is your number divisible by 4?')
                print('------------------------------')
                div_4 = input('Y/N: ').capitalize()
                if div_4 == 'Y':
                    print('Your number is 12')
                    print(user_num)
                    sys.exit
                else:
                    print('Is your number above 10?')
                    abv_10 = input('Y/N: ').capitalize()
                    if abv_10 == 'Y':
                        print('Your number is 18')
                        print(user_num)
                        sys.exit
                    else:
                        print('Your number is 6')
                        print(user_num)
                        sys.exit
            else:
                print('Your number is 24')
                print(user_num)
                sys.exit
    else:
        for elements3 in num_range:
            if elements3 % 3 == 0:
                num_range.remove(elements3)
            new_num_range3 = num_range
        print(new_num_range3)
        print('||||||||||||||||||')
        print('NOT DIVISIBLE BY 3')
        print('||||||||||||||||||')





number()





