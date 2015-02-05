import json

class Equipement :

	def __init__ (self, ComInsee,ComLib,InsNumeroInstall,EquipementId,EquNom):
		self.ComInsee = ComInsee
		self.ComLib = ComLib
		self.InsNumeroInstall = InsNumeroInstall
		self.EquipementId = EquipementId
		self.EquNom = EquNom

	def __repr__ (self):
		"{} - {} - {} - {} - {}". format(self.ComInsee, self.ComLib, self.InsNumeroInstall, self.EquipementId, self.EquNom)


	def getComInsee(self):
		return str(ComInsee)

	def getComInsee(self):
		return str(ComLib)

	def getComInsee(self):
		return str(InsNumeroInstall)

	def getComInsee(self):
		return str(EquipementId)

	def getComInsee(self):
		return str(EquNom)

	def set_ComInsee (self,t):
		self.ComInsee = t

	def set_ComLib (self,t):
		self.ComLib = t

	def set_InsNumeroInstall (self,t):
		self.InsNumeroInstall = t

	def set_EquipementId (self,t): 
		self.EquipementId = t
		
	def set_EquNom (self,t):
		self.EquNom = t
	