
## create directory
#importing module
import os
import numbers

## use brute force
def dirBruteForce(layer,dirPath,dirName):
	if layer > 0 :
		#call again to make layered dir
		for x in range(len(dirName)):
			dir = dirPath + dirName[x]
			dirBruteForce(layer - 1, dir,dirName)
	#call end of the dir
	elif layer == 0 :
		try:
			os.makedirs(dirPath)
			print(dirPath)
		except Exception as e:
			pass
		##copy dari template 
		for x in range(len(dirName)):
			try:
				shutil.copytree('template' + dirName[x], dirPath)
				print(dirPath + dirName[x])
			except Exception as e:
				pass
#####


## randomize dir for storing
import random
import shutil
dirCart = ''
def dirRandom(layer,dirPath,dirName):
	#set destination path
	dirDest = []
	for x in range(layer):
		dirDest.append(random.choice(dirName))
	return (dirPath + ''.join(dirDest))




#####


## constant variable

layer = 6
dirName = ['/ ','/  ','/   ','/    ']

##import module
import pickle
## CLI
print('Entertainment Management System')
print('By IlyasOfficial')
print('\n')
while True:
	print('(1) Membuat Vault / Brangkas')
	print('(2) Mengisi Vault / Brangkas')
	print('(3) Membuka Vault / Brangkas')

	try:	#to know when input is invalid
		indexX = int(input('pilih:'))
	except Exception as e:
		continue
	#validate the option
	if indexX == 1:
		# begin call Brute Force
		dirBruteForce(layer,'vault',dirName)
		break
	elif indexX == 2:
		# begin filling the Vault
		dirCart = dirRandom(layer,'vault',dirName)
		print(dirCart)
		shutil.move( 'pocket/pocket', dirCart)
		
		# open the file for writing
		fileObject = open('config.pickle','wb') 

		# this writes the object a to the
		# file named 'testfile'
		pickle.dump(dirCart,fileObject)   

		# here we close the fileObject
		fileObject.close()
		break
	elif indexX == 3:
		fileObject = open('config.pickle','rb')
		dirCart = pickle.load(fileObject)
		print(dirCart)
		shutil.move( dirCart + '/pocket' , 'pocket/')
		break
