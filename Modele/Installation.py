#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import codecs

class Installation :

	def __init__ (self, InsNumeroInstall, ComLib, ComInsee):
		self.InsNumeroInstall = InsNumeroInstall
		self.ComLib = ComLib
		self.ComInsee = ComInsee

	def __repr__ (self):
		"{} - {} - {}".format(self.InsNumeroInstall, self.ComLib, self.ComInsee)

	def __str__(self): 
		return self.InsNumeroInstall+" | "+self.ComLib+" | "+self.ComInsee

	def getInsNumeroInstall(self):
		return (self.InsNumeroInstall)

	def getComLib(self):
		return (self.ComLib)

	def getComInsee(self):
		return (self.ComInsee)

	def SQLcreate(self):
		return "CREATE TABLE installation (InsNumeroInstall integer, ComLib varchar, ComInsee integer)"

	def SQLinsert(self):
		return "INSERT INTO installation VALUES({}, {}, {})".format(self.InsNumeroInstall, "\""+self.ComLib+"\"", self.ComInsee)


def parse_json_installation(json_file):
	installations = []
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)
	for item in data["data"]:
		installations.append(Installation(item["InsNumeroInstall"], item["ComLib"], item["ComInsee"]))
	return installations

