from pylsl import StreamInlet, resolve_stream
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import style
from collections import deque
import os
import random
from playsound import playsound
import pandas as pd

streams = resolve_stream('type', 'EEG')
FFT_MAX_HZ = 60
inlet = StreamInlet(streams[-1])
HM_SECONDS = 10
TOTAL_ITERS = HM_SECONDS*25

def bk():
    channel_datas = []
    for i in range(250):
            channel_data = []
            sample, timestamp = inlet.pull_sample()
            channel_data.append(sample[:FFT_MAX_HZ])
            #print((sample[:4]))
            network_input = np.array(channel_data)
            channel_datas.append(channel_data)
    playsound('beep-01a.wav')
    playsound('Buka Mata .mp3')
    time.sleep(0.5)
    ACTION = 'buka_mata' 
    datadir = "data_sota"
    if not os.path.exists(datadir):
        os.mkdir(datadir)
    actiondir = f"{datadir}/{ACTION}"
    if not os.path.exists(actiondir):
        os.mkdir(actiondir)
    print(f"saving {ACTION} data...")
    #a=  np.array(channel_datas)
    #print(a.shape)
    np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(channel_datas))

def tp():
    channel_datas = []
    for i in range(250):
            channel_data = []
            sample, timestamp = inlet.pull_sample()
            channel_data.append(sample[:FFT_MAX_HZ])
            network_input = np.array(channel_data)
            channel_datas.append(channel_data)
    playsound('Tutup Mata.mp3')
    time.sleep(0.5)
    ACTION = 'tutup_mata' 
    datadir = "data_sota"
    if not os.path.exists(datadir):
        os.mkdir(datadir)
    actiondir = f"{datadir}/{ACTION}"
    if not os.path.exists(actiondir):
        os.mkdir(actiondir)
    print(f"saving {ACTION} data...")
    #b = np.array(channel_datas)
    #print(b.shape)
    np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(channel_datas))

def pp():
    channel_datas = []
    for i in range(313):
        channel_data = []
        sample, timestamp = inlet.pull_sample()
        channel_data.append(sample[:FFT_MAX_HZ])
        network_input = np.array(channel_data)
        channel_datas.append(channel_data)
    playsound('Persiapan.mp3')
    time.sleep(0.5)
    ACTION = 'Persiapan'
    datadir = "data_sota"
    if not os.path.exists(datadir):
        os.mkdir(datadir)
    actiondir = f"{datadir}/{ACTION}"
    if not os.path.exists(actiondir):
        os.mkdir(actiondir)
    print(f"saving {ACTION} data...")
    np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(channel_datas))
    playsound('Bayangkan Tangan.mp3')

def rk() :
    channel_datas = []
    for i in range(500):
            channel_data = []
            sample, timestamp = inlet.pull_sample()
            channel_data.append(sample[:FFT_MAX_HZ])
            network_input = np.array(channel_data)
            channel_datas.append(channel_data)
    ACTION = 'tangan_kanan' 
    datadir = "data_sota"
    if not os.path.exists(datadir):
        os.mkdir(datadir)
    actiondir = f"{datadir}/{ACTION}"
    if not os.path.exists(actiondir):
        os.mkdir(actiondir)
    print(f"saving {ACTION} data...")
    np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(channel_datas))
    playsound('beep-01a.wav')
    time.sleep(0.5)
for i in range (30):
        bk()
        tp()
        pp()
        rk()
        rk()
        print(i)
        









    
    
    
    


        


    






    





'''
datadir = "data_baru"
if not os.path.exists(datadir):
    os.mkdir(datadir)

actiondir = f"{datadir}/{ACTION}"
if not os.path.exists(actiondir):
    os.mkdir(actiondir)
print(len(channel_datas))

print(f"saving {ACTION} data...")
np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(channel_datas))
'''








