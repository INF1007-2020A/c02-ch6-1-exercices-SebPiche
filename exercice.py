#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	# result = []
	# for elem in numbers:
	# 	result.append(max(elem))
	# return result
	return [max(elem) for elem in numbers]

def join_integers(numbers):
	# result = ""
	# for elem in numbers:
	# 	result += str(elem)
	# return int(result)
	return int("".join([str(elem) for elem in numbers]))

# FONCTIONE Eratosthène
def generate_prime_numbers(limit):
	#premiers = liste vide
	premiers = []
	#nombres = liste des entiers de 2 a limite
	nombres = [i for i in range(2, limit+1)]
	#TANT QUE nombres est non vide FAIRE
	while len(nombres) != 0:
		#Ajouter a premiers le premier entier de nombbres
		premiers.append(nombres[0])
		#nombre = liste des entiers de nombre non multiple premier
		nombres = [elem for elem in nombres if elem % nombres[0] != 0]
		# nombre_2 = []
		# for elem in nombres:
		# 	if elem % nombres[0] != 0:
		# 		nombres_2.append(elem)
		# nombres = nombres_2
	#RESULTAT PREMIER
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	return [
		string + str(i)
		for i in range(1, num_combinations + 1)
			if excluded_multiples is None or i % excluded_multiples != 0
				for string in strings
	]
	# result = []
	# for i in range(1, num_combinations + 1):
	# 	if excluded_multiples is None or i % excluded_multiples != 0:
	# 		for elem in strings:
	# 			result.append(elem + str(i))
	# return result

	# for i in range(1, num_combinations + 1):
	# 	result += [elem + str(i) if excluded_multiples is None or i % excluded_multiples != 0 for elem in strings]
	# return result
if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("-")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("--")
	print(generate_prime_numbers(17))
	print("---")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
