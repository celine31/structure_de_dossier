import os
import json

def print_hierarchie(fichier_json):
	with open(fichier_json,'r') as f:
		structure=json.load(f)
	print('Les dossiers existent deja')
	print('voici la liste de dossiers : ')
	for key, values in structure.items():
		print ('. {0}'.format(key))
		for value in values:
			print('--- {0}'.format(value))
		
		print('='*25)

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

if os.path.isfile(fichier_json):
	print_hierarchie(fichier_json)
else:
	creer_dossiers(structure)
	ecrire_json(fichier_json,structure)
