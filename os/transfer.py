import shutil
import os
old_path='Downloads'
desktop=os.listdir('Desktop')
new_path='Desktop\\'+desktop[-5]

for name in os.listdir(old_path):
	if 'ex' in name:
		shutil.move(old_path+'\\'+name,new_path+'\\'+name[-16:-14])