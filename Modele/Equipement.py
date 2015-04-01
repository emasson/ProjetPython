	#!/usr/bin/env python3
	# -*- coding: utf-8 -*-
import json
import codecs
	
class Equipement:
	def __init__(self, InsNumeroInstall, EquipementId, ComInsee):
		self.InsNumeroInstall = InsNumeroInstall
		self.EquipementId = EquipementId
		self.ComInsee = ComInsee

	def __repr__(self):
		return "{} - {} - {}".format(self.InsNumeroInstall, self.EquipementId, self.ComInsee)

	def get_InsNumeroInstall(self):
		return self.InsNumeroInstall

	def get_EquipementId(self):
		return self.EquipementId

	def get_ComInsee(self):
		return self.ComInsee

	def SQLcreate(self):
		return "CREATE TABLE Equipement (InsNumeroInstall integer, EquipementId integer, ComInsee integer)"

	def SQLinsert(self):
		return "INSERT INTO Equipement VALUES({}, {}, {})".format(self.InsNumeroInstall, self.EquipementId, self.ComInsee)

def parse_json_equipment(json_file):
	equipements = []

	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)

	for item in data["data"]:
		equipements.append(Equipement(item["InsNumeroInstall"], item["EquipementId"], item["ComInsee"]))
	return equipements