import sys


def fibonacci(n,mem):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    else:
        if n in mem:
            return mem[n]
        else:
            mem[n] = fibonacci(n-1, mem)+fibonacci(n-2, mem)
        return mem[n]


sys.setrecursionlimit(5000)
number_strings = []
while True:
    number_string = input()
    if len(number_string) == 0:
        break
    else:
        number_strings.append(number_string)

for number in number_strings:
    try:
        fibonacci_num = fibonacci(int(number), {})
        print(f"Die Ficonacci Zahl für {number} ist: {str(fibonacci_num)}")
    except(Exception):
        print("Bitte gib valide Zahlen ein!")

