def count_primes(n):
    # Хэрэв n нь 2-оос бага байвал 0-ыг буцаана
    if n < 2:
        return 0

    # Бүх тоонуудыг prime гэж үзэж эхэлнэ
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0 болон 1 нь prime биш

    # n-ын квадрат язгуур хүртэлх бүх тоонуудыг шалгана
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            # Хэрэв prime байвал түүний бүх үржвэрүүдийг prime биш гэж тэмдэглэнэ
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # prime массивын үнэн утгуудыг нийлбэрлэн prime тоонуудын тоог буцаана
    return sum(primes)

# Жишээ:
n = 18
print(count_primes(n))  # Гаралт: 7
# 2. Prime Number Calculation (Анхны тоо олох):
# (Time Complexity): O(n log log n), Сieve of Eratosthenes алгоритм ашигласан.
# (Space Complexity): O(n), учир нь prime массивыг ашиглаж байгаа.