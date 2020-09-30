import os, random, time
from sys import platform
def clear():
	if platform == "linux" or platform == "linux2":
		cl = "clear"
	else:
		cl = "cls"
	return os.system(cl)
clear()

person = True # переменная для главного цикла вообще всей игры
game = False # переменная для цикла выбора команды победителя, смены ставки и тд, после ставки на одну из команд, активируется переменная match
match = False # переменная для цикла матча
person_name = input("Введите своё имя : ") # имя персонажа
person_id = random.randint(0, 999999) # id персонажа, не знаю зачем просто классно выглядит
person_money = 100 # деньги персонажа

stavka = None # начальная ставка, выбирается игроком
win_1_or_2 = None # ставка игрока на П1 или П2

win_or_lose = ["победила", "проиграла", "возвращается"] # вывод итогов матча в конце игры
win_or_lose1_2 = None # что то типо win_or_lose[win_or_lose1_2] чтобы показывать значение списка

settings_menu = None # игрок выбирает действие в главном меню
settings_stavka = None # игрок выбирает действие в окне матча

koef_list = [] # список коэффициентов

while person == True:
	clear()

	try:
		print(27 * "=")
		print(f"Имя : {person_name} | id={person_id}")
		print(f"Баланс : {round(person_money,2)}$")
		print(27 * "=")
		print("Выберите действие :")
		print("[1] = Ставки")
		print("[2] = Выход")
		settings_menu = int(input(">>> "))
	except:
		clear()
		print("Какая то ошибка")
		time.sleep(1)

	if settings_menu == 1:
		game = True
		while game == True:
			score1 = random.randint(0, 4) # рандомное число голов первой команды
			score2 = random.randint(0, 4) # рандомное число голов второй команды

			global_time = random.randint(0,59) # время которое прошло от начала матча
			two = round(random.uniform(2,3), 2) # переменная для деления коэффициента

			koef1 = (score2 + (score1 + score2)) / two # коэффициент на первую команду
			koef_list.append(koef1)
			koef2 = (score1 + (score1 + score2)) / two # коэффициент на вторую команду
			koef_list.append(koef2)

			if score2 == score1:
				random_koef = random.randint(0,1) # тут идет перевес коэффициентов рандомно на одну из команд в случае если счёт равный, дабы не было такого, что коэффициенты одинаковые получаются при одинаковом счёте
				if random_koef == 0:
					koef1 = koef1 + round(random.uniform(0,1), 1)
				else:
					koef2 = koef2 + round(random.uniform(0,1), 1)

			clear()
			print(27 * "=")

			print("Ставка на футбол.")
			print(f"Баланс : {person_money}$")
			print(f"Ваша ставка : {stavka}$")
			print(f"Время : прошло {global_time} мин.")
			print(f"Счёт ({score1}:{score2})")

			print(27 * "=")

			print(f"П1: {round(koef1, 2)} / П2: {round(koef2, 2)}")
			print("[1] = Поставить на П1")
			print("[2] = Поставить на П2")
			print("[3] = Изменить ставку")
			print("[4] = Выйти")
			try:
				settings_stavka = int(input(">>> "))
			except:
				clear()
				print("Какая то ошибка")
				time.sleep(1)

			if settings_stavka == 1 or settings_stavka == 2:
				if stavka <= 0 or stavka == None:
					while stavka <= 0 or stavka == None:
						print("Ваша ставка не принята.")
						print("Введите ставку")
						stavka = int(input(">>> "))

				win_1_or_2 = settings_stavka  # здесь типо выбор игрока П1 и П2 записывается в эту переменную, которая в итоге рассчитывается в конце матча

				match = True # начало игры / матча
				while match == True:
					clear()

					# выбираются 2 рандомных значения для каждой команды, в процессе матча каждый раз создаётся новое значение третьей переменной, и при совпадении третьей переменной с одной из этих, то одной из команд засчитывается гол
					random_score1 = random.randint(0, 50)
					random_score2 = random.randint(0, 50)

					global_time = global_time + 1

					if random_score1 == random_score2: # если вдруг они совпадают, то идет цикл, и он будет идти, пока значения не будут различаться
						while random_score1 == random_score2:
							random_score1 = random.randint(0, 50)
							random_score2 = random.randint(0, 50)

					random_score = random.randint(0, 50) # а вот и третья переменная которая выдает рандомные значения и сравнивается с теми двумя
					if random_score == random_score1:
						score1 += 1
					if random_score == random_score2:
						score2 += 1
					if global_time == 90: # конец матча и рассчёт вывода победы или поражения игроку, если счёт одинаковый, то идет возврат средств
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
							print(f"Вы выиграли : {round(sum_stavka,2)}$")
							person_money = person_money + sum_stavka
						if win_or_lose1_2 == 1:
							print(f"Вы проиграли : {round(stavka)}$")
							person_money = person_money - stavka
						if win_or_lose1_2 == 3:
							print("Ваша ставка возвращается")
						time.sleep(5)
						match = False

					print(f"Время : прошло {global_time} мин.")
					print(f"Счёт ({score1}:{score2})")
					time.sleep(0.2)


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