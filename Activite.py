class Activite : 

	def __init__(self, equipementId, equActiviteSalleSpe, equActivitePratique, equActivitePraticable, comLib, actCode, actNivLib, comInsee, actLib, equNbEquIdentique):
			self.equipementId = equipementId
			self.equActiviteSalleSpe = equActiviteSalleSpe
			self.equActivitePratique = equActivitePratique
			self.equActivitePraticable = equActivitePraticable
			self.comLib = comLib
			self.actCode = actCode
			self.actNivLib = actNivLib
			self.comInsee = comInsee
			self.actLib = actLib
			self.equNbEquIdentique = equNbEquIdentique

	def get_EquipementId (self):
		return str(self.equipementId)
	def get_EquActiviteSalleSpe (self):
		return str(self.equActiviteSalleSpe)
	def get_EquActivitePratique (self):
		return str(self.equActivitePratique)
	def get_EquActivitePraticable (self): 
		return str(self.equActivitePraticable)
	def get_ComLib (self):
		return str(self.comLib)
	def get_ActCode (self):
		return str(self.actCode)
	def get_ActNivLib (self):
		return str(self.actNivLib)
	def get_ComInsee (self):
		return str(self.comInsee)
	def get_ActLib (self):
		return str(self.actLib)
	def get_EquNbEquIdentique (self):
		return str(self.equNbEquIdentique)


	def set_EquipementId (self,t):
		self.equipementId = t
	def set_EquActiviteSalleSpe (self,t):
		self.equActiviteSalleSpe = t
	def set_EquActivitePratique (self,t):
		self.equActivitePratique = t
	def set_EquActivitePraticable (self,t): 
		self.equActivitePraticable = t
	def set_ComLib (self,t):
		self.comLib = t
	def set_ActCode (self,t):
		self.actCode = t
	def set_ActNivLib (self,t):
		self.actNivLib = t
	def set_ComInsee (self,t):
		self.comInsee = t
	def set_ActLib (self,t):
		self.actLib = t
	def set_EquNbEquIdentique (self,t):
		self.equNbEquIdentique = t