#1
def easy(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

num = int(input('Введите число: '))

if easy(num):
    print('Простое число.')
else:
    print('Не простое число.')
#2
def sorted(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

nums = input('Введите числа, разделенные пробелом: ')
num_sorted = [int(num) for num in nums.split()]
sorted(num_sorted)

print(num_sorted)
#3
def find(nums):
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum

sort = input('Введите числа через проблел: ')
nums = list(map(int, sort.split()))

print(find(nums))

#4
def func(nums):
    if nums == 1 or nums == 2:
        return 1
    else:
        return func(nums - 1) + func(nums - 2)


num = int(input('Введите число: '))
print('Число Фибоначчи: ', func(num))
#5
def line(lines):
    table = {}
    max = 0
    repeat = ''

    for string in lines:
        if string in table:
            table[string] += 1
        else:
            table[string] = 1

        if table[string] > max:
            max = table[string]
            repeat = string

        return repeat

num = []
person = input('Введите элемент: ')
while person != "0":
    num.append(person)
    person = input('Введите элемент: ')

find = line(num)
print('Наиболее часто встречающаяся строка: ', find)