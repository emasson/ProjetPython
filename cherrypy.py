	#!/usr/bin/env python3
	# -*- coding: utf-8 -*- 
import cherrypy
import Modele.Installation
import Modele.Equipement
import Modele.Activite
import service.database as bd

class WebManager(object): 

	@cherrypy.expose

	def index(self): 
		""" Exposes the service at localhost:8080 """
		return ''' <html><body> 
		<h1> Installations sportives des Pays de la loire </h1> 
		<input type="button" name="Installations" value="Fiche installations" onclick="self.location.href='display_Installations'">
		<input type="button" name="Activites" value="Fiche activites" onclick="self.location.href='display_Activites'"> 
		<input type="button" name="Installations" value="Fiche equipements" onclick="self.location.href='display_Equipements'">
		</body></html> ''' 

	@cherrypy.expose 

	def display_Installations(self):
		""" Exposes the service at localhost:8080/display_Installations """
		html="" 
		database = bd.Database('service/M4105C.db')
		inst = database.read_Installation()

		html += '''
		<h2>Information des installations</h2>

		<table> <tr>

		<th>NumeroInstall</th>

		<th>ComLib</th>

		<th>ComInsee</th> 
		</tr>\n'''

		for i in inst:
			if (i!=[]):
				html += '''<tr>\n
			  	<td>''' + str(i[0]) + '''</td>
			  	<td>''' + i[1] + '''</td>
			  	<td>''' + str(i[2]) + '''</td>
			  	</tr>''' 
		html += '''</table>''' 
		return html 

	@cherrypy.expose 
	
	def display_Activites(self):
		""" Exposes the service at localhost:8080/display_Activites """
		html = ""
		database = bd.Database('service/M4105C.db') 
		act = database.read_Activite() 

		html += '''
	 	<h2>Information des activites</h2>

	 	<table> <tr> 
	 	<th>EquipementId</th>

	 	<th>ComInsee</th>

	 	<th>ActCode</th> 

		<th>ActLib</th>

		<th>ComLib</th> 

		</tr>\n'''

		for i in act:
			if (i!=[]):
				html += '''<tr>\n
			  	<td>''' + str(i[0]) + '''</td>
			  	<td>''' + str(i[1]) + '''</td>
			  	<td>''' + str(i[2]) + '''</td>
			  	<td>''' + i[3] + '''</td>
			  	<td>''' + i[4] + '''</td>

			  	</tr>''' 
		html += '''</table>''' 
		return html

	@cherrypy.expose 

	def display_Equipements(self):
		""" Exposes the service at localhost:8080/display_Equipements """
		html="" 
		database = bd.Database('service/M4105C.db')
		eqs = database.read_Equipement()

		html += '''
		<h2>Information des installations</h2>

		<table> <tr>

		<th>NumeroInstall</th>

		<th>ComLib</th>

		<th>ComInsee</th> 
		</tr>\n'''

		for i in eqs:
			if (i!=[]):
				html += '''<tr>\n
			  	<td>''' + str(i[0]) + '''</td>
			  	<td>''' + str(i[1]) + '''</td>
			  	<td>''' + str(i[2]) + '''</td>
			  	</tr>''' 
		html += '''</table>''' 
		return html 

cherrypy.quickstart(WebManager())