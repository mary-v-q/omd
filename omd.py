def step1():
    print(
        'Утка-маляр 🦆 решила погулять по городу. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    places = ["парк", "музей", "театр"]
    print(
        'Утка-маляр взяла зонтик и пошла гулять по городу.\n'
        f'Она может пойти в следующие места: {", ".join(places)}.'
    )
    place = ""
    while place not in places:
        print(f'Выберите, куда пойти утке: {"/".join(places)}')
        place = input().strip().lower()
        if place not in places:
            print("Ошибка: выберите доступное место.")

    if place == "парк":
        print(
            f'Утка-маляр выбрала {place}, и смогла послушать пение птиц после того, как дождь закончился.\n'
            f'Потом она решила зайти за кофе в местное кафе.'
        )
    elif place == "музей":
        print(
            f'Утка-маляр выбрала {place}, и попала на открытие выставки.\n'
            f'Она познакомилась с уткой-художником, и они вместе пошли в ресторан.'
        )
    else:
        print(
            f'Утка-маляр выбрала {place}, и ей удалось взять автограф у известного режиссера.\n'
            f'После спектакля она поужинала в буфете.'
        )


def step2_no_umbrella():
    print("Утка промокла под дождем, у нее поднялась температура, и она полетела домой")


if __name__ == "__main__":
    step1()