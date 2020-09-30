import os, random, time
from sys import platform
def clear():
	if platform == "linux" or platform == "linux2":
		cl = "clear"
	else:
		cl = "cls"
	return os.system(cl)
clear()

person = True
game = False
match = False
person_name = input("Введите своё имя : ")
person_id = random.randint(0, 999999)
person_money = 100

stavka = None # начальная ставка выбирается игроком
win_1_or_2 = None # ставка игрока на П1 или П2

win_or_lose = ["победила", "проиграла", "возвращается"]
win_or_lose1_2 = None

settings_menu = None
settings_stavka = None

koef_list = []

while person == True:
	clear()

	print(27 * "=")
	print(f"Имя : {person_name} / id={person_id}")
	print(f"Деньги : {round(person_money,2)}")
	print(27 * "=")
	print("Выберите действие :")
	print("[1] = Ставки")
	print("[2] = Выход")
	settings_menu = int(input(">>> "))

	if settings_menu == 1:
		game = True
		while game == True:
			score1 = random.randint(0, 4)
			score2 = random.randint(0, 4)

			global_time = random.randint(0,89)
			two = round(random.uniform(2,3), 2)

			koef1 = (score2 + (score1 + score2)) / two
			koef_list.append(koef1)
			koef2 = (score1 + (score1 + score2)) / two
			koef_list.append(koef2)

			if score2 == score1:
				random_koef = random.randint(0,1)
				if random_koef == 0:
					koef1 = koef1 + round(random.uniform(0,1), 1)
				else:
					koef2 = koef2 + round(random.uniform(0,1), 1)

			clear()
			print(27 * "=")

			print("Ставка на футбол.")
			print(f"Ваша ставка : {stavka}")
			print(f"Время : прошло {global_time} мин.")
			print(f"Счёт ({score1}:{score2})")

			print(27 * "=")

			print(f"П1: {round(koef1, 2)} / П2: {round(koef2, 2)}")
			print("[1] = Поставить на П1")
			print("[2] = Поставить на П2")
			print("[3] = Изменить ставку")
			print("[4] = Выйти")
			settings_stavka = int(input(">>> "))

			if settings_stavka == 1 or settings_stavka == 2:
				if stavka <= 0 or stavka == None:
					while stavka <= 0:	
						print("Ваша ставка не принята.")
						print("Введите ставку")
						stavka = int(input(">>> "))

				win_1_or_2 = settings_stavka

				match = True # начало игры
				while match == True:
					clear()

					random_score1 = random.randint(0, 50)
					random_score2 = random.randint(0, 50)

					global_time = global_time + 1

					if random_score1 == random_score2:
						while random_score1 == random_score2:
							random_score1 = random.randint(0, 50)
							random_score2 = random.randint(0, 50)

					random_score = random.randint(0, 50)
					if random_score == random_score1:
						score1 += 1
					if random_score == random_score2:
						score2 += 1
					if global_time == 90:
						match = False
						if score1 > score2 and win_1_or_2 == 1:
							win_or_lose1_2 = 0
						if score1 < score2 and win_1_or_2 == 2:
							win_or_lose1_2 = 0
						if score1 > score2 and win_1_or_2 == 2:
							win_or_lose1_2 = 1
						if score1 < score2 and win_1_or_2 == 1:
							win_or_lose1_2 = 1
						if score1 == score2:
							win_or_lose1_2 = 2


						print("Матч окончен.")
						print(f"Ваша ставка на {stavka}$ {win_or_lose[win_or_lose1_2]}")
						if win_or_lose1_2 == 0:
							sum_stavka = stavka * koef_list[win_1_or_2 - 1]
							print(f"Вы выиграли : {round(sum_stavka,2)}")
							person_money = person_money + sum_stavka
						if win_or_lose1_2 == 1:
							print(f"Вы проиграли : {round(stavka)}")
							person_money = person_money - stavka
						if win_or_lose1_2 == 3:
							print("Ваша ставка возвращается")
						time.sleep(5)
						match = False

					print(f"Время : прошло {global_time} мин.")
					print(f"Счёт ({score1}:{score2})")
					time.sleep(0.4)


			if settings_stavka == 3:
				clear()
				print("Введите ставку")
				stavka = int(input(">>> "))

			if settings_stavka == 4:
				clear()
				game = False
	if person_money <= 0:
		clear()
		print("Деньги закончились")
		person = False

	if settings_menu == 2:
		clear()
		print("Пока!")
		person = False