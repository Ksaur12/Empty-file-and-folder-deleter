import os


def folder():
	os.chdir('/storage/emulated/0/')
	fileList = []
	del_folder = 0
	for dir, folder, file in os.walk('/storage/emulated/0/'):
		if file == fileList:
			if folder == fileList:
				del_folder += 1
				os.removedirs(dir)
		else:
			pass
	print(str(del_folder) + " folders deleted")



def file():
	os.chdir('/storage/emulated/0/')
	fileList = []
	del_file = 0
	for dir, folder, file in os.walk('/storage/emulated/0/'):
		for a in file:
			os.chdir(dir)
			if os.stat(a).st_size == 0:
				os.remove(a)
				del_file += 1
			else:
				pass
	print(str(del_file) + ' files deleted')
	

def usage():
	print('''
Choose 1 for deleting empty folders
Choose 2 for deleting empty files
Choose 3 for deleting both
	''')

usage()
choice = input('Enter your your choice: ')
if choice == '1':
	print('\n')
	print('Deleting empty folder.....')
	folder()
	print('\nThere are no more empty folders')
elif choice == '2':
	print('\n')
	print('Deleting empty files......')
	file()
	print('\nThere are no more empty files')
elif choice == '3':
	print('\n')
	print('Deleting empty files and folders.....')
	folder()
	file()
	print('\nThere are no more empty files or folders')
else:
	print('\n')
	print('[!!] Not Valid')
	usage()
	print('Exiting the program.....')