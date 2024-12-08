def assign_bikes(students, bikes):
    # Оюутан, дугуй хоорондын зайг хадгалсан жагсаалтыг үүсгэнэ
    distances = []
    for i, student in enumerate(students):
        for j, bike in enumerate(bikes):
            dist = abs(student[0] - bike[0]) + abs(student[1] - bike[1])
            distances.append((dist, i, j))

    # Зай, дараа нь оюутан, дараа нь дугуйг тоогоор нь эрэмбэлнэ
    distances.sort()

    # Оюутан болон дугуйг сонгож байгаа эсэхийг тэмдэглэнэ
    assigned_students = [-1] * len(students)
    used_bikes = [False] * len(bikes)

    # Эрэмбэлсэн зайг ашиглан хамгийн ойр байгааг оюутанд даатгана
    for dist, student, bike in distances:
        if assigned_students[student] == -1 and not used_bikes[bike]:
            assigned_students[student] = bike
            used_bikes[bike] = True

    return assigned_students

# Жишээ:
students = [(0, 0), (1, 1)]
bikes = [(0, 1), (4, 3), (2, 1)]
print(assign_bikes(students, bikes))  # Гаралт: [0, 2]
# 3. Students and Bikes Problem (Оюутан ба дугуйн асуудал):
# (Time Complexity): O(n * m log(n * m)), энд n нь оюутны тоо, m нь дугуйн тоо.
# (Space Complexity): O(n * m), учир нь оюутан ба дугуйн хоорондын зайг хадгалах массив ашиглаж байгаа.