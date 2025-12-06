from __future__ import print_function


class Human(object):
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "%s %s, %s, %d years old" % (
            self.first_name,
            self.last_name,
            self.gender,
            self.age,
        )


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super(Student, self).__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return "%s %s, %s, %d years old, Record Book: %s" % (
            self.first_name,
            self.last_name,
            self.gender,
            self.age,
            self.record_book,
        )

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class Group(object):
    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
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
        return "Number:%s\n%s" % (self.number, all_students)


st1 = Student("Male", 29, "Влад", "Петренко", "AN142")
st2 = Student("Female", 26, "Олена", "Коваленко", "AN145")
st3 = Student("Male", 28, "Ігор", "Шевченко", "AN150")

gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)

print("Вивід групи:\n", gr)
assert str(gr.find_student("Петренко")) == str(st1), "Test1"
assert gr.find_student("Петренко2") is None, "Test2"
assert isinstance(gr.find_student("Петренко"), Student) is True
gr.delete_student("Коваленко")
print("\nПісля видалення Коваленко:\n", gr)
gr.delete_student("Коваленко")
