import math  

def negjiin_urtug(n):
    niit_zardal = 0  # Нийт зардлыг 0-ээр эхлүүлнэ
    for i in range(1, n + 1):  # 1-ээс n хүртэлх бүх тоонууд дээр давталт хийнэ
        if math.log2(i).is_integer():  # i-гийн логарифм 2-оор хуваагддаг эсэхийг шалгана
            niit_zardal += i  # Хэрвээ 2-оор хуваагддаг бол тухайн тоог нийт зардалд нэмнэ
        else:
            niit_zardal += 1  # Хэрвээ 2-оор хуваагдахгүй бол 1 нэмнэ
    return niit_zardal / n  # Нийт зардлыг n-ээр хувааж, дундаж нэгжийн өртгийг буцаана

n = 16  
unit_cost = negjiin_urtug(n)  
print(f"{n} үйлдлийн дундаж нэгжийн өртөг нь {unit_cost:.2f}")  