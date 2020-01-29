import subprocess
import os

path = 'converted_unprocessed/TRAIN/DR1/100'
audios = os.listdir(path)

audio = audios[0]
print(audio)
command = 'sox -V0 {} -n stats -w 0.2'.format(os.path.join(path,audio)).split()
out = subprocess.run(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE).stderr.decode().split('\n')