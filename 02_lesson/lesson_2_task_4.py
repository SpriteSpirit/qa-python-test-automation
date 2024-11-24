def fizz_buzz(n):
    """
    Выводит числа от 1 до n, заменяя числа, кратные 3, на "Fizz", числа, кратные 5, на "Buzz",
    а числа, кратные 3 и 5, на "FizzBuzz".
    :param n: Верхний предел диапазона.
    """

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


fizz_buzz(17)
