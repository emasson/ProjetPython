	#!/usr/bin/env python3
	# -*- coding: utf-8 -*-
import json
import codecs
	
class Activite: 
	def __init__(self, EquipementId, ComInsee, ActCode, ActLib, ComLib):
		self.EquipementId = EquipementId
		self.ComInsee = ComInsee
		self.ActCode = ActCode
		self.ActLib = ActLib
		self.ComLib = ComLib

	def __repr__(self):
		return "{} - {} - {} - {} - {}".format(self.EquipementId, self.ComInsee, self.ActCode, self.ActLib, self.ComLib)

	def get_EquipmentId(self):
		return self.EquipementId

	def get_ComInsee(self):
		return self.ComInsee

	def get_ActCode(self):
		return self.ActCode

	def get_ComInsee(self):
		return self.ActLib

	def get_ActCode(self):
		return self.ComLib

	def SQLcreate(self):
		return "CREATE TABLE activite (EquipementId integer, ComInsee integer, ActCode integer, ActLib varchar, ComLib varchar)"

	def SQLinsert(self):
		if self.ActCode == None:
			self.ActCode = 0
		if self.ActLib == None:
			self.ActLib = ""
		if self.ComLib == None:
			self.ComLib = ""
		return "INSERT INTO activite VALUES({}, {}, {}, {}, {})".format(self.EquipementId, self.ComInsee, self.ActCode, "\""+self.ActLib+"\"", "\""+self.ComLib+"\"")

def parse_json_activite(json_file):
	activites = []
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)
	for item in data["data"]:
		activites.append(Activite(item["EquipementId"], item["ComInsee"], item["ActCode"], item["ActLib"], item["ComLib"]))
	return activites