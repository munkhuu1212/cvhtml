def coin_change(zoos, hemjee):
    # Тооцоолсон үр дүнг хадгална
    memory = {}

    def dp(uldsen):
        # Үндсэн нөхцөлүүд
        if uldsen == 0:
            return 0  # Хэрэв үлдэгдэл 0 байвал ямар ч мөнгөн дэвсгэрт хэрэггүй
        if uldsen < 0:
            return float('inf')  # Үлдэгдэл сөрөг бол боломжгүй утга

        # Хэрэв өмнө тооцоолсон бол санах ойгоос үр дүнг буцаана
        if uldsen in memory:
            return memory[uldsen]

        # Бүх мөнгөн дэвсгэртийг шалгаж, хамгийн багыг нь сонгоно
        min_zoos = float('inf')
        for coin in zoos:
            ur_dun = dp(uldsen - coin)  # Үлдэгдэлээс дэвсгэртийг хасна
            if ur_dun != float('inf'):
                min_zoos = min(min_zoos, ur_dun + 1)  
                # Хамгийн бага утгыг сонгоно

        # Санах ойд үр дүнг хадгална
        memory[uldsen] = min_zoos
        return min_zoos

    # Гол функцээр дамжуулан нийт үр дүнг тооцоолно
    ur_dun = dp(hemjee)

    # Хэрэв үр дүн хязгааргүй байвал боломжгүй утга гэж үзнэ
    return ur_dun if ur_dun != float('inf') else -1
# Жишээ
zoos = [1, 2, 5]
hemjee = 11
print(coin_change(zoos, hemjee))  # Гаргалт: 3