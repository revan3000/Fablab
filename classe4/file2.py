import os 
file=open('file2.txt','w')
file.write('nuevo texto')
os.remove('file2.txt')