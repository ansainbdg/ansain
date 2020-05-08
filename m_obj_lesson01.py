import math


def manager(base, position):
    ins = round((base+position)*0.17, -1)
    income = (base+position-ins)*0.9
    return income


def general(base, overtime):
    money = math.floor(base*(1+overtime*1.25/160)/10)*10
    ins = round(money*0.15, -1)
    income = (money-ins)*0.9
    return income


def part(unit, time):
    income = unit*time*0.9
    return income


if __name__ == "__main__":
    terao_income = manager(350000, 80000)
    wakabayashi_income = manager(375000, 40000)
    hamaguchi_income = manager(360000, 40000)
    terada_income = general(320000, 30)
    hirota_income = general(295000, 20)
    kannuma_income = general(220000, 35)
    adachi_income = general(310000, 20)
    kikuchi_income = part(1200, 90)
    yamagishi_income = part(800, 150)
    mochiduki_income = part(1100, 90)

    print(f' 寺尾さんの振込額は{terao_income}')
    print(f' 若林さんの振込額は{wakabayashi_income}')
    print(f' 浜口さんの振込額は{hamaguchi_income}')
    print(f' 寺田さんの振込額は{terada_income}')
    print(f' 広田さんの振込額は{hirota_income}')
    print(f' 菅沼さんの振込額は{kannuma_income}')
    print(f' 安達さんの振込額は{adachi_income}')
    print(f' 菊池さんの振込額は{kikuchi_income}')
    print(f' 山岸さんの振込額は{yamagishi_income}')
    print(f' 望月さんの振込額は{mochiduki_income}')