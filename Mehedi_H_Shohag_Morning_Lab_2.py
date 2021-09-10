##################################
#     CSC 113-2L(Morning)        #
#      Mehedi H Shohag           #
#                     
#     Lab 2 (11/10/2020)         #
##################################

############################   Question 1   ###################

def PerfectNumber(n):
    summation = 0
    for i in range(1, n):
        if n % i == 0:
            summation += i
    return summation == n


def userInput():
    while True:
        num = int(input("Enter a number or enter 0 to quit the program\n"))
        if num == 0:
            print('Program Terminated')
            break
        elif num < 0:
            raise ValueError('You can not input negative number.')
        else:
            print(PerfectNumber(num))


if __name__ == '__main__':

    try:
        userInput()

    except ValueError as e:
        print(e)




############################   Question 2   ###################

def prime_number(num1, num2):
    prime = []
    for i in range(num1, num2 + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                prime.append(i)

    for k in range(len(prime)):
        print(prime[k])
        with open('Prime.txt', 'w') as file:
            file.write(str(prime))


if __name__ == '__main__':
    a, b = [int(x) for x in input("Enter two value: ").split()]
    prime_number(a, b)




############################   Question 3   ###################
def triangleCheck(x1, y1, x2, y2, x3, y3):
    s = (x1 * (y2 - y3) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))
    if (s == 0):
        print("Will not Create triangle")
    else:
        print("Will create triangle")


if __name__ == '__main__':
    while True:
        try:
            a, b, c, d, e, f = [int(x) for x in input("Enter 3 points(six numbers following by space) : ").split()]
            if (a, b, c, d, e, f >= 0 or a, b, c, d, e, f <= 0):
                triangleCheck(a, b, c, d, e, f)
            else:
                raise ValueError('Invalid Input')
            user = input('Do u want to check one more round?(y/n)')
            if user == 'y':
                continue
            else:
                break
        except ValueError as e:
            print(e)


############################   Question 4   ###################
def trimmingLine(input_file):
    with open(input_file, encoding='utf-8') as f:
        with open("quotes2.txt", "w", encoding='utf-8') as f1:
            for line in f:
                if len(line.strip()) != 0:
                    print(line.strip(), file=f1)


if __name__ == '__main__':
    trimmingLine('quotes.txt')




############################   Question 5   ###################
def primeLine(input_file):
    cntnt = open(input_file, 'r+')
    content = cntnt.read()
    lines = content.split('\n')
    new_lines = []
    for i in lines:
        if (len(i)) != 0:
            new_lines.append(i)
    num_lines = len(new_lines)
    prime = False
    if n > 1:
        for i in range(2, num_lines):
            if num_lines % i == 0:
                prime = True
                break
    cntnt.seek(0)
    cntnt.truncate()
    if prime == False:
        for i in lines:
            cntnt.write(i)
    else:
        for i in lines:
            cntnt.write(i + '\t')
    cntnt.close()


if __name__ == '__main__':
    primeLine('quotes.txt')




############################   Question 6   ###################
def Greetings(A, k):
    a = len(A)
    for i in range(a):
        if a >= k:
            print(A[:a])
        a -= 1


if __name__ == '__main__':
    user = input('Please enter a word: ')
    n = int(input('Enter a number : '))
    Greetings(user, n)
