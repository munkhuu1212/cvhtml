class AmortizedStack:
    def __init__(self, k):  
        # Стек хадгалах жагсаалт
        self.stack = []
        # "backup" үйлдлийг хийх зай буюу k утга
        self.k = k
        # Хэдэн удаа "backup" хийснийг хадгалах тоолуур
        self.backups = 0

    def push(self, value):  
        # Стек рүү шинэ утга нэмэх
        self.stack.append(value)
        # Хэрэв стек дэх элементүүдийн тоо k-ийн үржвэр байвал "backup" хийнэ
        if len(self.stack) % self.k == 0:
            self.backup()

    def pop(self):  
        # Стекээс хамгийн сүүлийн утгыг хасаж буцаах
        if self.stack:
            return self.stack.pop()
        # Хэрэв стек хоосон байвал None буцаана
        return None

    def backup(self):  
        # Нөөцлөлт хийгдсэн тоог 1-р нэмэгдүүлэх
        self.backups += 1  

    def total_cost(self):  
        # Нийт зардал: стек дэх элементүүдийн тоо + "backup" тоо
        return len(self.stack) + self.backups

# Жишээ 
k = 5  # Нөөцлөлтийн зай
operations = 20  # Нийт үйлдлийн тоо
stack = AmortizedStack(k)  # Шинэ стек үүсгэх

# 1-ээс 20 хүртэлх утгууд дээр push, pop үйлдэл хийх
for i in range(1, operations + 1):
    stack.push(i)  # push үйлдэл
    if i % 3 == 0:  
        stack.pop()

# Нийт үйлдлийн дараах зардлыг хэвлэх
print(f"{operations} үйл ажиллагааны дараах нийт зардал: {stack.total_cost()}")
# Үйлдэл бүрийн дундаж зардлыг хэвлэх
print(f"Үйл ажиллагааны хорогдуулсан зардал: {stack.total_cost() / operations:.2f}")