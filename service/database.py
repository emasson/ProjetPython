import sqlite3
class Database:
	def __init__(self, path):
		self.conn = sqlite3.connect(path)
		self.path = path

	def createNew(self, name, classe):
		c = self.conn.cursor()
		c.execute("DROP TABLE IF EXISTS " + name)
		c.execute(classe.SQLcreate())

	def insert(self, items):
		c = self.conn.cursor()
		for item in items:
			c.execute(item.SQLinsert())

	def commit(self):
		self.conn.commit()

	def selectAll(self, name):
		c = self.conn.cursor()
		for row in c.execute("SELECT * FROM " + name):
			print(row)

	def close(self):

		"""
		Closes the connexion to the database
		"""
		self.conn.close()

	def read_Activite(self):
		c = self.conn.cursor()
		activite = [[]]
		for i in c.execute("SELECT * FROM activite"):
			activite.append([i[0], i[1], i[2], i[3], i[4]])
		return activite

	def read_Installation(self):
		c = self.conn.cursor()
		installation = [[]]
		for i in c.execute("SELECT * FROM installation"):
			installation.append([i[0], i[1], i[2]])
		return installation

	def read_Equipement(self):
		c = self.conn.cursor()
		equipement = [[]]
		for i in c.execute("SELECT * FROM equipement"):
			equipement.append([i[0], i[1], i[2]])
		return equipement