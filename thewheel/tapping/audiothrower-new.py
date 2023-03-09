import os
import shutil
fold = 'TheWheelTappingList'
ext = '.ogg'
os.mkdir(fold)
files = os.listdir(path='audio')
for file in files:
    stat = file.replace(ext,'').split('_')
    if not (os.path.isdir(fold + '/' + stat[0])):
        os.mkdir(fold + '/' + stat[0])
    shutil.copy('audio/' + file,fold + '/' + stat[0] + '/' + stat[1] + ext)
