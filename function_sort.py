import operator

class Pessoa:

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def obterNome(self):
		return self.nome

	def obterIdade(self):
		return self.idade

p1 = Pessoa('Marcos', 28)
p2 = Pessoa('Pedro', 20)
p3 = Pessoa('Carol', 30)
p4 = Pessoa('Yankee', 25)

pessoas = [p1, p2, p3, p4]
pessoas.sort(key=operator.attrgetter('idade'),)

for pessoa in pessoas:
	print('Nome: %s, idade: %d' % (pessoa.obterNome(), pessoa.obterIdade()))
