import random
class Student:
    def __init__(self, name, intelligence, grade, happines):
        self.name = name
        self.health = 100
        self.intelligence = intelligence
        self.energy = 100
        self.grade = grade
        self.happiness = happines
        self.character = ''

    def learn(self):
        self.health -= 25
        self.intelligence +=2
        self.energy -= 10
        self.grade += 0.1
        self.happiness -= 50
        print(f'{self.name}, Отсидел 4 пары, что-то сделал, что-то написал. Его средний балл стал {self.grade}')

    def chill(self):
        self.health += 20
        self.energy += 30
        print(f'{self.name} на чиле, на расслабоне')

    def have_fun(self):
        self.health -= 15
        self.intelligence -= 1
        self.energy -= 20
        self.grade -= 0.1
        self.happiness += 20
        print(f'{self.name} Построил церковь в майнкрафт.'
              f'Он стал немного тупее и, следовательно, счастливее')

    def slip(self):
        self.health += 25
        self.energy += 25
        self.happiness += 10
        print(f' для {self.name} сон это святое')


def main():
    k13 = []
    k14 = []
    student1 = Student("Igor", random.randint(1, 10), random.randint(0, 5), random.randint(20, 100))
    student2 = Student("Ilya", random.randint(1, 10), random.randint(0, 5), random.randint(20, 100))
    student3 = Student("Anton", random.randint(1, 10), random.randint(0, 5), random.randint(20, 100))
    student4 = Student("Maks", random.randint(1, 10), random.randint(0, 5), random.randint(20, 100))
    student5 = Student("Vladimer", random.randint(1, 10), random.randint(0, 5), random.randint(20, 100))
    student6 = Student("Tofig", random.randint(1, 10), random.randint(0, 5), random.randint(20, 100))
    k13.append(student1)
    k13.append(student2)
    k13.append(student3)
    k14.append(student4)
    k14.append(student5)
    k14.append(student6)

    for m in range(random.randint(5, 15)):
        for i in range(3):
            k = random.randint(1, 4)
            a = k13[i]
            if k == 1:
                a.learn()
            elif k == 2:
                a.slip()
            elif k == 3:
                a.have_fun()
            elif k == 4:
                a.slip()

        for i in range(3):
            k = random.choice(1, 4)
            a = k14[i]
            if k == 1:
                a.learn()
            elif k == 2:
                a.chill()
            elif k == 3:
                a.have_fun()
            elif k == 4:
                a.slip()

    max_bal_k14 = 0
    max_bal_k13 = 0
    k13_sred_bal = 0
    k14_sred_bal = 0
    otchislen = []
    for i in range(3):
        k13_sred_bal += k13[i].grade
        k14_sred_bal += k14[i].grade
        if k13[i].grade <= 2.5:
            otchislen.append(k13[i].name)
        if max_bal_k13 < k13[i].grade:
            max_bal_k13 = k13[i].grade
            name_k13 = k13[i].name
        if k14[i].grade <= 2.5:
            otchislen.append(k14[i].name)
        if max_bal_k14 < k14[i].grade:
            max_bal_k14 = k14[i].grade
            name_k14 = k14[i].name
    k13_sred_bal = k13_sred_bal / 3
    k14_sred_bal = k14_sred_bal / 3

    for i in range(11):
        print()
    print(f'Иготи года:')
    print(f'Средний бал в группе к13 = {k13_sred_bal}')
    print(f'Средний бал в группе к14 = {k13_sred_bal}')
    print(f'Студент с самым большим баллом в группе k13: {name_k13}')
    print(f'Студент с самым большим баллом в группе k14: {name_k14}')
    print(f'Списки на отчисление: {otchislen} ')


main()
