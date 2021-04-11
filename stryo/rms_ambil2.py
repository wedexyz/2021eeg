from pylsl import StreamInlet, resolve_stream
import numpy as np
import time

import os
import random
from playsound import playsound


streams = resolve_stream('type', 'EEG')

inlet = StreamInlet(streams[0])
def bk():
    playsound('Buka Mata .mp3')
    time.sleep(2)
def tp():
    playsound('Tutup Mata.mp3')
    time.sleep(2)
def pp():
    playsound('Persiapan.mp3')
    time.sleep(2)
    playsound('beep-01a.wav')
def tes():
    datas_baru = []
    datas_baru1= []
    datas_baru2= []
    datas_baru3= []
    datas_baru4= []
    datas_baru5= []
    datas_baru6= []
    datas_baru7= []
   
    for i in range(1):
            data_baru= []
            data_baru1 = []
            data_baru2 = []
            data_baru3 = []
            data_baru4 = []
            data_baru5 = []
            data_baru6 = []
            data_baru7 = []

            for i in range(250):
                sample, timestamp = inlet.pull_sample()
                data_baru.append(np.sqrt(np.mean(np.square(sample[0:1]), axis = 0)))
                data_baru1.append(np.sqrt(np.mean(np.square(sample[1:2]), axis = 0)))
                data_baru2.append(np.sqrt(np.mean(np.square(sample[2:3]), axis = 0)))
                data_baru3.append(np.sqrt(np.mean(np.square(sample[3:4]), axis = 0)))
                data_baru4.append(np.sqrt(np.mean(np.square(sample[4:5]), axis = 0)))
                data_baru5.append(np.sqrt(np.mean(np.square(sample[5:6]), axis = 0)))
                data_baru6.append(np.sqrt(np.mean(np.square(sample[6:7]), axis = 0)))
                data_baru7.append(np.sqrt(np.mean(np.square(sample[7:8]), axis = 0)))

                datas_baru.append(data_baru)
                datas_baru1.append(data_baru1)
                datas_baru2.append(data_baru2)
                datas_baru3.append(data_baru3)
                datas_baru4.append(data_baru4)
                datas_baru5.append(data_baru5)
                datas_baru6.append(data_baru6)
                datas_baru7.append(data_baru7)
                
    b1= np.array(datas_baru)
    b2 = np.array(datas_baru1)
    b3 = np.array(datas_baru2)
    b4 = np.array(datas_baru3)
    b5 = np.array(datas_baru4)
    b6 = np.array(datas_baru5)
    b7 = np.array(datas_baru6)
    b8 = np.array(datas_baru7)

    t = np.dstack((b1,b2,b3,b4,b5,b6,b7,b8))
    playsound('Bayangkan Tangan.mp3')
    
'''
    ACTION = 'meneng' 
    datadir = "rms"
    actiondir = f"{datadir}/{ACTION}"
    if not os.path.exists(datadir):
        os.mkdir(datadir)
    if not os.path.exists(actiondir):
        os.mkdir(actiondir)
    print(f"saving {ACTION} data...,",t.shape)
    np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(t))
'''
for i in range(20) :
     bk()
     tp()
     pp()
     tes ()