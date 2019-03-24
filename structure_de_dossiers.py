import os
import json

def creer_dossiers(dossiers):
	for key, values in dossiers.items():
		for value in values:
			dossier='{0}/{1}/{2}'.format(base,key,value)
			#creer les dossiers et sous-dossiers
			os.makedirs(dossier)
			print('creation du dossier {0}'.format(dossier))

def ecrire_json(fichier_json,dictionnaire):
	with open(fichier_json,'w') as f:
		json.dump(dictionnaire,f,indent=4)


base= r'C:\Users\dadou\Desktop\Structure'
#pour etre certain le r suffit
base=base.replace('\\', '/')

fichier_json= r'C:\Users\dadou\Desktop\Structure\structure.json'
fichier_json=fichier_json.replace('\\', '/')

structure={
			'Musique': ['Rock', 'Jazz', 'Pop'],
			'Document': ['Factures', 'Travail', 'Maison'],
			'Images': ['Vacances', 'Famille'],
			'Videos': ['Chat', 'Musique'] 
			}

creer_dossiers(structure)
ecrire_json(fichier_json,structure)