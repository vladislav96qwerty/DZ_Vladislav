from __future__ import print_function


class GroupLimitException(Exception):
    def __init__(self, message="Максимальна кількість студентів у групі - 10"):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"
        )


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old, Record Book: {self.record_book}"

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupLimitException()
        if student not in self.group:
            self.group.append(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        group_info = (
            f"Group: {self.number}, Students: {len(self.group)}/{self.MAX_STUDENTS}"
        )
        return (
            f"{group_info}\n{all_students}"
            if self.group
            else f"{group_info}\n(No students)"
        )


if __name__ == "__main__":
    gr = Group("PD1")

    students_data = [
        ("Male", 29, "Влад", "Петренко", "AN142"),
        ("Female", 26, "Олена", "Коваленко", "AN145"),
        ("Male", 28, "Ігор", "Шевченко", "AN150"),
        ("Female", 27, "Марія", "Іваненко", "AN151"),
        ("Male", 30, "Олександр", "Сидоренко", "AN152"),
        ("Female", 25, "Наталія", "Павленко", "AN153"),
        ("Male", 29, "Дмитро", "Гончаренко", "AN154"),
        ("Female", 26, "Катерина", "Бондаренко", "AN155"),
        ("Male", 28, "Андрій", "Ткаченко", "AN156"),
        ("Female", 27, "Тетяна", "Кравченко", "AN157"),
        ("Male", 24, "Сергій", "Олійник", "AN158"),
    ]

    print("Тестування додавання студентів до групи:")
    print("=" * 50)

    for i, (gender, age, first_name, last_name, record_book) in enumerate(
        students_data, 1
    ):
        try:
            student = Student(gender, age, first_name, last_name, record_book)
            gr.add_student(student)
            print(f"✅ Студент {i} доданий: {first_name} {last_name}")
        except GroupLimitException as e:
            print(
                f"❌ Помилка при додаванні студента {i} ({first_name} {last_name}): {e}"
            )

    print("\n" + "=" * 50)
    print("Поточний стан групи:")
    print(gr)

    print("\n" + "=" * 50)
    print("Додаткові тести:")

    try:
        extra_student = Student("Male", 22, "Екстра", "Студент", "AN999")
        gr.add_student(extra_student)
    except GroupLimitException as e:
        print(f"❌ Не вдалося додати  студента: {e}")

    print("\nТестування видалення та додавання нового студента:")
    gr.delete_student("Петренко")
    print(
        f"Студент Петренко видалений. В групі залишилось: {len(gr.group)}/{Group.MAX_STUDENTS}"
    )

    try:
        new_student = Student("Female", 21, "Нова", "Студентка", "AN200")
        gr.add_student(new_student)
        print(
            f"✅ Нова студентка додана. В групі тепер: {len(gr.group)}/{Group.MAX_STUDENTS}"
        )
    except GroupLimitException as e:
        print(f"❌ Не вдалося додати нову студентку: {e}")
