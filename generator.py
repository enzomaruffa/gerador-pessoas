#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
import hashlib
import copy
from random import randint
from random import choice

possible_names = ['Carolina', 'Guilherme', 'Daniel', 'Luna', 'Natalie', 'Elaini', 'Eduarda', 'Isabella', 'Júlia', 'André', 'Thiago', 'Sandra', 'Edson', 'Ossian', 'Laura', 'Dante', 'Fernando', 'Antonio', 'Denise', 'Eloisa', 'Eduardo', 'Sílvio', 'Pedro', 'José', 'Jorge', 'Alfredo', 'Amadeus', 'Marcos', 'Enzo', 'Mariana', 'Aline', 'Marcus', 'Silvana', 'Ada', 'Renan', 'Roberto', 'Caio', 'Maria', 'Livia', 'Emerson', 'Luiz', 'Luis', 'Alan']
possible_surnames = ['Andrade', 'Krum', 'Kawasaki', 'Gallice', 'Pedri', 'Harres', 'Queiroz', 'Rodrigues', 'Vicente', 'Kniss', 'Yamada', 'Cremonezi', 'Schumacher', 'Campos', 'Kovalski', 'Strozzi', 'Iboshi', 'Handa', 'Megumi', 'Shinohata', 'Padovani', 'Olini', 'Martins', 'Pereira', 'Moreira', 'Lopes', 'Souza', 'Sousa', 'Gomes', 'Ameixa', 'Pera', 'Maruffa', 'Krajuska', 'Dudeque', 'Starosta', 'Franco', 'Dencker', 'Gil', 'Barreto', 'Kruger', 'Calopsita', 'Meneghel']
possible_emails = ['gmail.com', 'outlook.com', 'bol.com.br', 'outlook.com']

possible_street_types = ['Av.', 'Rua']
possible_street_prefixes = ['Marechal', 'Presidente', 'Coronel']
possible_street_separator = [' de ', ' da ', ' ', ' ', ' ']
possible_states = ['Amapá', 'Paraná', 'Amazonas', 'Rio Grande do Sul', 'Santa Catarina', 'São Paulo', 'Rio de Janeiro', 'Espírito Santo', 'Alagoas', 'Sergipe', 'Bahia', 'Mato Grosso', 'Mato Grosso do Sul', 'Pará', 'Minas Gerais']
possible_cities = ['Curitiba', 'Manaus', 'Porto Alegre', 'Florianópolis', 'São Paulo', 'Rio de Janeiro', 'Vitória', 'Maceió', 'Aracaju', 'Salvador', 'Cuiabá', 'Campo Grande', 'Belém', 'Belo Horizonte', 'Palotina', 'Divinópolis', 'Nova Serrana', 'Monte Alegre do Sul', 'Santa Maria', 'Porto Seguro', 'Campo Largo', 'Curitibanos', 'Itapoá']
possible_ddds = [67, 66, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41]

visaPrefixList = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']]

mastercardPrefixList = [
        ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

class Person:

	def __init__(self):
		self.name, self.surname = self.generate_random_name()

		self.email = self.generate_random_email()
		self.password = self.generate_random_password()

		self.cpf = self.generate_random_cpf()
		self.street, self.number, self.complement, self.city, self.cep = self.generate_random_address()
		self.telephone = self.generate_random_phone(True)
		self.cellphone = self.generate_random_phone(False)
		self.cardNickname, self.pan, self.expDate, self.cvv = self.generate_random_card()

	def generate_random_name(self):
		name = random.choice(possible_names)
		surname = random.choice(possible_surnames)

		return name, surname

	def generate_random_email(self):
		email = self.name.lower() + "." + self.surname.lower() + "@" + random.choice(possible_emails)
		return email

	def generate_random_password(self):
		h = hashlib.md5()
		h.update((self.name + self.surname))
		return (h.hexdigest())[0:6]

	def generate_random_cpf(self):
		cpf = ""
		for i in range(0, 11):
			digit = random.randrange(0, 9)
			cpf += str(digit)
		return cpf

	def generate_random_phone(self, telephone=True):
	    if telephone:
	        typePhone = ' '
	    else:
	        typePhone = ' 9'
	    number = '+55 {0}{1}'.format(random.choice(possible_ddds), typePhone)
	    number += str(randint(1,9))
	    for n in range(7):
	        number += str(randint(0,9))
	    return number

	def generate_random_address(self):
		def generate_random_street():
			prefix = random.choice(possible_street_prefixes)
			
			i = random.randint(1, 100)
			# Gera rua legal
			if i <= 85:
				first_name = random.choice(possible_names)
				separator = random.choice(possible_street_separator)
				second_name =  random.choice(possible_surnames)
				last_name =  random.choice(possible_surnames)
				street = prefix + ' ' + first_name + separator + second_name + ' ' + last_name

			# Gera rua de estado
			else:
				state_name = random.choice(possible_states)
				street = prefix + ' ' + state_name

			return street

		street = generate_random_street()
		number = str(random.randint(1, 2000))

		i = random.randint(1, 100)
		if i <= 50:
			complement = 'Casa'
		else:
			complement = 'Ap. ' + str(random.randint(1, 200))

		city = random.choice(possible_cities)

		cep = ""
		for i in range(0, 9):
			digit = random.randrange(0, 9)
			cep += str(digit)

		return street, number, complement, city, cep

	def generate_random_card(self):
		def completed_number(prefix, length):
		    """
		    'prefix' is the start of the CC number as a string, any number of digits.
		    'length' is the length of the CC number to generate. Typically 13 or 16
		    """
		    ccnumber = prefix
		    # generate digits
		    while len(ccnumber) < (length - 1):
		        digit = str(random.choice(range(0, 10)))
		        ccnumber.append(digit)

		    # Calculate sum
		    sum = 0
		    pos = 0

		    reversedCCnumber = []
		    reversedCCnumber.extend(ccnumber)
		    reversedCCnumber.reverse()

		    while pos < length - 1:
		        odd = int(reversedCCnumber[pos]) * 2
		        if odd > 9:
		            odd -= 9
		        sum += odd

		        if pos != (length - 2):
		            sum += int(reversedCCnumber[pos + 1])
		        pos += 2

		    # Calculate check digit
		    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
		    ccnumber.append(str(checkdigit))
		    return ''.join(ccnumber)

		def credit_card_number(prefixList, length):
			ccnumber = copy.copy(random.choice(prefixList))
			return (completed_number(ccnumber, length))

		visa16 = credit_card_number(visaPrefixList, 16)[:-2]
		#cardNickname = self.name.upper() + ' ' + self.surname.upper()
		cardNickname = "VISA teste"
		
		month = str(random.randint(0, 12))
		if int(month) < 10:
			month = "0" + month

		expDate = month + str(2) + str(random.randint(1, 9))

		cvv = str(random.randint(0, 999))
		if int(cvv) < 10:
			cvv = "0" + cvv
		if int(cvv) < 100:
			cvv = "0" + cvv

		return cardNickname, visa16, expDate, cvv

people_list = []

for i in range(0, 10000):
	person = Person()
	numbers = [person.pan for person in people_list]
	while person.number in numbers:
		person = Person()
	people_list.append(person)

file = open('pessoas.csv', 'w+')
file.write('email,senha,nome,sobrenome,cep,endereco,numero,complemento,cidade, telefone fixo, celular, apelido cartao,pan,dataexp,cvv,cpf\n')

for person in people_list:
	file.write(person.email + ',' + person.password + ',' + person.name + ',' + person.surname + ',' + person.cep + ',' + person.street + ',' + person.number + ',' + person.complement + ',' + person.city + ',' + person.telephone + ',' + person.cellphone + ',' + person.cardNickname + ',' + person.pan + ',' + person.expDate + ',' + person.cvv + ',' + person.cpf + '\n')
	print(person.name + ' ' + person.surname + ' / ' + person.email + ' / ' + person.password + ' / ' + person.cpf + ' / ' + person.street + ', ' + person.number + ', ' + person.complement + '. ' + person.city + ', '  + person.telephone + ', '  + person.cellphone + ', ' + person.cep + ' / ' + person.cardNickname + ', ' + person.pan + ', ' + person.expDate + ', ' + person.cvv)

file.close()
