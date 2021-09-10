##################################
#     CSC 113-2L(Morning)        #
#      Mehedi H Shohag           #
#                                #
#     Midterm (11/18/2020)       #
##################################

###########################   Question 1   ############################
print('\nQuestion 1 Solution')


def babylonian_sqrt(N, k, initial):
    count = 0
    guess = initial
    iteration = []
    while True:
        error = guess ** 2 - N
        count += 1
        if abs(error) <= k:
            break
        guess = (guess + N / guess) / 2.0
        iteration.append(guess)
    print('S:', N)
    print('Initial guess : ', initial)
    print('Square-root ~ ', guess)
    print(count, 'iterations')

    if count < 100:
        file = open('log.txt', 'w')
        file.write('S:' + str(N) + '\n')
        file.write('Initial guess : ' + str(initial) + '\n')
        file.write('Square-root ~ ' + str(guess) + '\n')
        file.write(str(count) + ' iterations' + '\n')
        for i in range(len(iteration)):
            file.write('Iteration ' + str(i + 1) + ' : ' + str(iteration[i]) + '\n')
    file.close()


if __name__ == '__main__':
    number = abs(float(input("N: ")))
    initial = abs(float(input("Initial guess: ")))
    error = abs(float(input("k: ")))
    babylonian_sqrt(number, error, initial)


###########################   Question 2   ############################
print('\nQuestion 2 Solution')

def move_line(file,k):
    text=open(file,'r')
    output=open('Mehedi_shifted.txt','w')
    data=text.readlines()
    for i in range(len(data)):
        if(i>k):
            output.write(data[i])
        else:pass
    n=0
    output.write('\n')
    while(n<k):
        output.write(data[n])
        n+=1
    output.close()

if __name__=='__main__':
    line=int(input('Please enter the k value : '))
    move_line('Mehedi.txt',line)
    print('Line has successfully shifted and written to the Mehedi_shifted.txt file')


###########################   Question 3   ############################
print('\nQuestion 3 Solution')

def check_char_exist(string,char):
    return 'Char exist' if char.lower() in string.lower() else 'Char doesn\'t exist'

if __name__=='__main__':
    st=input('Please enter a String :')
    ch=input('Please enter a character :')
    print(check_char_exist(st,ch))

###########################   Question 4   ############################
print('\nQuestion 4 Solution')

def f1():
    try:
        a=eval(input('please enter something'))
        b=eval(input('please enter something'))
        c=a+b
        return c
    except NameError:
        print('Please enter a number or multiple numbers with expression(e.g 4+7) ')
    except SyntaxError:
        print('Please enter numbers with complete expression')
if __name__ == '__main__':
    print(f1())
    print('The code above will generate a sum of two user input which returns in c.\n'+
         'But based on the user input it can produce two types of exception.\n'+
         'If the user inputs some variable such as a,b or something like that,\n'+
         'It will creates a NameError because that variable is not defined previously in order to evaluate.\n'+
         'And the second error is if the user inputs some number with expression but unfinished expression,\n'+
         '(e.g 4+8-)then it will create a SyntaxError.')

###########################   Question 5   ############################
print('\nQuestion 5 Solution')

from random import randint

counter = 0
win = 0
lose = 0

loose_streak = 0
loose_streak_max = 0

while counter <= 10000:
    randNum = randint(1, 2)
    if randNum == 1:
        win += 1
        loose_streak = 0
    else:
        lose += 1
        loose_streak += 1

    if loose_streak > loose_streak_max:
        loose_streak_max = loose_streak
    counter += 1
if __name__ == '__main__':
    print('Win: ', win, '\nLose: ', lose, '\nLS: ', loose_streak_max)

###########################   Question 6   ############################
print('\nQuestion 6 Solution')

def prime_number(num1, num2):
    prime = []
    sum=0
    for i in range(num1+1, num2):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                prime.append(i)

    for k in range(len(prime)):
        print(prime[k])
        sum+=prime[k]
    print('Sum of all prime = ',sum)

if __name__ == '__main__':
    a, b = [int(x) for x in input("Enter two value followed by space : ").split()]
    prime_number(a, b)

###########################   Question 7   ############################
print('\nQuestion 7 Solution')


def perfect_square(a, b):
    c = 1
    while c * c < a:
        c += 1
    while c * c <= b:
        print(c * c)
        c += 1


if __name__ == '__main__':
    a = int(input('Enter a :'))
    b = int(input('Enter b :'))
    perfect_square(a, b)


###########################   Question 8   ############################
print('\nQuestion 8 Solution')

def check_string_exist(string,file):
    data=open(file,'r').read()
    return 'String exist' if string.lower() in data.lower() else 'String doesn\'t exist'

if __name__=='__main__':
    st=input('Please enter a String :')
    print(check_string_exist(st,'Mehedi.txt'))

###########################   Question 9   ############################
print('\nQuestion 9 Solution')

if __name__=='__main__':
    for i in range(11):
        print('*'*i)

###########################   Question 10   ############################
print('\nQuestion 10 Solution')


def lcm(a, b):
    gcd = 0
    if a == 0:
        gcd = b
    else:
        gcd = lcm(b % a, a)
    return gcd


if __name__ == '__main__':
    try:
        file = input('Please enter the file name (Enter Mehedi_10.txt): ')
        num = open(file, 'r')
        for l in num:
            a, b = (l.split(' '))
        gcd = lcm(int(a), int(b))
        print('The least common multiple : ', (int(a) * int(b)) / gcd)
    except FileNotFoundError:
        print('File doesn\'t exist')

###########################   Question 11   ############################
print('\nQuestion 11 Solution')


def Parabola(a, b, c):
    vertix_x = format(-b / (2 * a), '.2f')
    vertix_y = format((4 * a * c) - ((b ** 2) / (4 * a)), '.2f')
    focus_x = format(-b / (2 * a), '.2f')
    focus_y = format(((4 * a * c) - ((b ** 2) + 1) / (4 * a)), '.2f')
    directrix = format((c - ((b ** 2) + 1) * 4 * a), '.2f')

    print('Vertix = (', vertix_x, ',', vertix_y, ')\n' +
          'Focus = (', focus_x, ',', focus_y, ')\n' +
          'Directrix = ', directrix)


if __name__ == '__main__':
    try:
        a, b, c = [float(x) for x in input("Enter three values followed by space : ").split()]
        Parabola(a, b, c)
    except ZeroDivisionError:
        print('First entered number can not be zero.')

###########################   Question 12   ############################
print('\nQuestion 12 Solution')


def absn(number):
    return abs(number)


if __name__ == '__main__':
    num = 1
    while (num != 0):
        try:
            num = float(input('Please enter a number : '))
            if num == 0:
                raise print('Zero entered. Program terminated.')
                exit
            elif num < 0 or num > 0:
                print(absn(num))
        except:
            print('Invalid input')

###########################   Question 13   ############################
print('\nQuestion 13 Solution')


def common(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    str3 = str2.difference(str1)
    for i in str3:
        print(i, end='')


if __name__ == '__main__':
    a = input('Please enter a string')
    b = input('Please enter another string')
    common(a, b)

###########################   Question 14   ############################
print('\nQuestion 14 Solution')


def alphabet_order(string):
    n = len(string)
    vowel = set('aeiou')
    stringSet = set(string)
    string_vowel = []
    if stringSet.issuperset(vowel):
        for i in string:
            if i in 'aeiou':
                string_vowel.append(i)
        for j in range(1, len(string_vowel)):
            if (string_vowel[j] < string_vowel[j - 1]):
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    user = input('Please enter a word : ')
    if (alphabet_order(user)):
        print('Vowels are in Order')
    else:
        print('Vowels are not in Order')

###########################   Question 15   ############################
print('\nQuestion 15 Solution')

def count_word(file):
    count=0
    with open(file) as f:
        line=f.read()
    words=line.split()
    for i in range(len(words)):
        if len(words[i])>5:
            count+=1
        else:
            continue
    print('There are',count,'words which has more then 5 character')
if __name__=='__main__':
    count_word('Mehedi.txt')

