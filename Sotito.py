import datetime

class Persona():
	def __init__(self, lugar):
		self.llegada = datetime.datetime.today()
		self.pos_inicial = lugar
		self.pos = lugar
		self.ida = ""

class Fila():
	def __init__(self, cuantos_antes_de_llegar=0):
		self.total = cuantos_antes_de_llegar
		self.hora_inicio = datetime.datetime.today()
		self.perso_iniciales = cuantos_antes_de_llegar
		self.personas = []
		self.se_fueron = []

	def agregar_persona(self):
		A = Persona(self.total)
		self.personas.append(A)
		self.total += 1

	def mover_fila(self):
		se_fue = self.personas.pop(0)
		se_fue.ida = datetime.datetime.today()
		self.se_fueron.append(se_fue)
		for perso in self.personas:
			perso.pos -= 1


f1 = int(input("¿Cuantas personas en fila UNO hay ahora?\n --> "))
f2 = int(input("¿Cuantas personas en fila DOS hay ahora?\n --> "))

fila1 = Fila(f1)
fila2 = Fila(f2)

while True:
	print(""" MENU
	[1] LlEGÓ alguien fila UNO
	[2] LLEGÓ alguien fila DOS
	[3] MUEVE fila UNO
	[4] MUEVE fila DOS

	[5] SALIR""")
	deci = int(input("--> "))
	if deci == 1:
		fila1.agregar_persona()
	elif deci == 2:
		fila2.agregar_persona()
	elif deci == 3:
		fila1.mover_fila()
	elif deci == 4:
		fila2.mover_fila()
	else:
		with open("Fila_1.txt", "w") as data:
			data.write("Inicio a las {} con {} personas\n".format(
				fila2.hora_inicio, fila1.perso_iniciales))
			data.write("\nSe Fueron:\n")
			for elem in fila1.se_fueron:
				tex = "N-{} llego a las {} se fue a las {}\n".format(
					elem.pos_inicial, elem.llegada, elem.ida)
				data.write(tex)
			data.write("\nQuedaron:\n")
			for ele in fila1.personas:
				text = "N-{} llego a las {}\n".format(
					ele.pos_inicial, ele.llegada)
				data.write(text)

		with open("Fila_2.txt", "w") as data:
			data.write("Inicio a las {} con {} personas\n".format(
				fila2.hora_inicio, fila2.perso_iniciales))
			data.write("\nSe Fueron:\n")
			for elem in fila2.se_fueron:
				tex = "N-{} llego a las {} se fue a las {}\n".format(
					elem.pos_inicial, elem.llegada, elem.ida)
				data.write(tex)
			data.write("\nQuedaron:\n")
			for ele in fila2.personas:
				text = "N-{} llego a las {}\n".format(
					ele.pos_inicial, ele.llegada, ele.ida)
				data.write(text)
		break