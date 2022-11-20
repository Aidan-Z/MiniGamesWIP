import os
import sys


#user inputs

def number():
    num_range = list(range(1, 31))
    print("choose number between 1-30")
    print('========================================')


    user_num = int(input('num: ')) 
    if (user_num in num_range):
        print('ok')
    else:
        print('not within range')
        os.execl(sys.executable, sys.executable, *sys.argv)

    print('========================================')

    print("is user_num div by 5?")
    div_5 = input('Y/N: ').capitalize()
    if div_5 == 'Y' and user_num % 5 == 0: #if num div by 5 and user = true
        div_5_list = (30, 25, 20, 15, 10, 5) #list of potential numbers
        print(div_5_list)

        if user_num in div_5_list: 
            print('is number bellow 20?: ')
            bel_20 = input('Y/N: ').capitalize()
            if bel_20 == 'Y' and user_num < 20: #narrow down to number bellow 20 and div by 5
                print('ok_bel20')
                bel_20_list = (15, 10, 5)
                print(bel_20_list)
                print('is number multiple of 3?')
                mul_3 = input('Y/N: ').capitalize()
                if mul_3 == 'Y' and user_num % 3 == 0:
                    print('your number is 15')
                    print(user_num)
                    sys.exit
                else:
                    print('is your number divisible by 2?')
                    div_2 = input('Y/N: ').capitalize()
                    if div_2 == 'Y':
                        print('your number is 10')
                        print(user_num)
                        sys.exit
                    else:
                        print('your number is 5')
                        print(user_num)
                        sys.exit
            
            else:
                if user_num > 20 == False:
                    print('Wrong- try again')
                    os.execl(sys.executable, sys.executable, *sys.argv)
                else:
                    if user_num >= 20:
                        print('above 20')
                        abv_20_list = [30, 25, 20]
                        print(abv_20_list)
                        print('is number divisible by 2?')
                        div_2v2 = input('Y/N: ').capitalize()
                        if div_2v2 == 'Y':
                            print('is number divisible by 3?')
                            div_3v2 = input('Y/N: ').capitalize()
                            if div_3v2 == 'Y' and user_num % 3 == 0:
                                print('your numb is 30')
                                print(user_num)
                            else:
                                print('your number is 20')
                                print(user_num)
                        else:
                            print('your number is 25')
                            print(user_num)   
                            
        else:
            print('5')
    else: #remove numbers from origional range list
        for elements1 in num_range:
            if elements1 % 5 == 0:
                num_range.remove(elements1)
            new_num_range1 = num_range
        print(new_num_range1)
        print('NOT DIV BY 5')

    print('========================================')

    print('number divisible by 7?')
    div_7 = input('Y/N: ').capitalize()
    if div_7 == 'Y' and user_num % 7 == 0:
        div_7_list = (28, 21, 14, 7)
        print(div_7_list)
        if user_num in div_7_list:
            print('is your number odd?')
            odd_7 = input('Y/N: ').capitalize()
            if odd_7 == 'Y' and user_num % 2 != 0:
                odd_7_list = (21, 7)
                print(odd_7_list)
                print('is number multiple of 3?')
                mul_3v7 = input('Y/N: ').capitalize()
                if mul_3v7 == 'Y':
                    print('your number is 21')
                    print(user_num)
                    sys.exit
                else:
                    if mul_3v7 == 'N':
                        print('your number is 7')
                        print(user_num)
                        sys.exit
            else:
                print('is your number bellow 20?')
                bel_20v2 = input('Y/N: ').capitalize()
                if bel_20v2 == 'Y':
                    print('your number is 14')
                    print(user_num)
                    sys.exit
                else:
                    print('your number is 28')
                    print(user_num)

    else:
        for elements2 in num_range:
            if elements2 % 7 == 0:
                num_range.remove(elements2)
            new_num_range2 = num_range
        print(new_num_range2)
        print('NOT DIV BY 7 or 5')

    print('========================================')












number()



