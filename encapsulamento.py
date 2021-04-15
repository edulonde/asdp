#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:49:57 2021

@author: yusuf_edouard
"""

class Pessoa:

	def __init__(self):
		self.__nome = None

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, nome):
		self.__nome = nome

p = Pessoa()
p.nome = 'José Eduardo'
print(p.nome)