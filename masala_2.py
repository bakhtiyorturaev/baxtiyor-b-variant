from faker import Faker
import random

fake = Faker()


def ism_generatsiya():
    while True:
        ism = fake.first_name() + " " + fake.last_name()
        if len(ism) > 7 and ism[-1].lower() in ['a', 'e', 'i', 'o', 'u']:
            return ism


def yosh_generatsiya():
    return random.randint(1, 100)


def yoshi_tub_yoki_toq(son):
    if son == 1:
        return "tub"
    return "toq"


def test1_generatsiya(file_name):
    with open(file_name, "w") as file:
        for i in range(1, 21):
            ism = ism_generatsiya()
            yosh = yosh_generatsiya()
            yosh_xususiyati = yoshi_tub_yoki_toq(yosh % 2)
            file.write(f"{i}. {ism:<20} {yosh} {yosh_xususiyati}\n")


def test2_generatsiya(file_name):
    with open(file_name, "w") as file:
        for i in range(1, 11):  # 10 qatorda ma'lumot yoziladi
            ism = ism_generatsiya()
            yosh = yosh_generatsiya()
            yosh_xususiyati = yoshi_tub_yoki_toq(yosh % 2)
            file.write(f"{ism:<20} {yosh} {yosh_xususiyati}\n")



test1_generatsiya("test1.txt")
test2_generatsiya("test2.txt")
