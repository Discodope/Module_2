numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_primes = [] #Создаем пустые списки для внесения чисел

for i in numbers:
    is_prime = True # принимаем простые числа за True
    if i <= 1: # сразу откидываем единицу потому что оно не простое и не не простое
        is_prime = False
    else:
        for j in range(2, int(i ** 0.5) + 1): # возводим каждое число, начиная с двойки, в степень 0.5 и прибавляем к нему 1, присваиваем int(остаток не интересен)
            if i % j == 0: # если делится без
                is_prime = False
                break

    if is_prime:
        prime.append(i)
    else:
        not_primes.append(i)

print('primes:', prime)
print('not_primes:', not_primes)


