#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Modele.Installation as inst
import Modele.Equipement as equ
import Modele.Activite as act
import service.database as db

installs = inst.parse_json_installation("fichierJson/Installation.json")
equs = equ.parse_json_equipment("fichierJson/Equipement.json")
acts = act.parse_json_activite("fichierJson/Activite.json")

database = db.Database("service/M4105C.db")
database.createNew("Installation", installs[0])
database.insert(installs)

#database.selectAll("installation")
database.createNew("Equipement", equs[0])
database.insert(equs)


#database.selectAll("equipement")
database.createNew("Activite", acts[0])
database.insert(acts)

database.commit()
database.close()