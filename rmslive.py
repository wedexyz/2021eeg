from pylsl import StreamInlet, resolve_stream
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation


import os
import random
from playsound import playsound
import pandas as pd

streams = resolve_stream('type', 'EEG')

inlet = StreamInlet(streams[0])
#inlet2 = StreamInlet(streams[1])


def tes():
    channel_datas = []

    datas_baru = []
    datas_baru1= []
    datas_baru2= []
    datas_baru3= []
    datas_baru4= []
    datas_baru5= []
    datas_baru6= []
    datas_baru7= []
   
    for i in range(1):
            channel_data = []

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
                #sample2, timestamp = inlet2.pull_sample()

                channel_data.append(sample[0:8])

                data_baru.append(np.sqrt(np.mean(np.square(sample[0:1]), axis = 0)))
                data_baru1.append(np.sqrt(np.mean(np.square(sample[1:2]), axis = 0)))
                data_baru2.append(np.sqrt(np.mean(np.square(sample[2:3]), axis = 0)))
                data_baru3.append(np.sqrt(np.mean(np.square(sample[3:4]), axis = 0)))
                data_baru4.append(np.sqrt(np.mean(np.square(sample[4:5]), axis = 0)))
                data_baru5.append(np.sqrt(np.mean(np.square(sample[5:6]), axis = 0)))
                data_baru6.append(np.sqrt(np.mean(np.square(sample[6:7]), axis = 0)))
                data_baru7.append(np.sqrt(np.mean(np.square(sample[7:8]), axis = 0)))
                #data_baru8.append(np.sqrt(np.mean(np.square(sample[6:7]), axis = 0)))

                channel_datas.append(channel_data)

                datas_baru.append(data_baru)
                datas_baru1.append(data_baru1)
                datas_baru2.append(data_baru2)
                datas_baru3.append(data_baru3)
                datas_baru4.append(data_baru4)
                datas_baru5.append(data_baru5)
                datas_baru6.append(data_baru6)
                datas_baru7.append(data_baru7)
                
    a = np.array(channel_datas)

    b1= np.array(datas_baru)
    b2 = np.array(datas_baru1)
    b3 = np.array(datas_baru2)
    b4 = np.array(datas_baru3)
    b5 = np.array(datas_baru4)
    b6 = np.array(datas_baru5)
    b7 = np.array(datas_baru6)
    b8 = np.array(datas_baru7)

    t = np.dstack((b1,b2,b3,b4,b5,b6,b7,b8))

    print("total",t.shape)
    #b = np.array(channel2_datas)
    #print(a.shape,b.shape)

    #rms = np.sqrt(np.mean(np.square(a), axis = 0))

    #mav=np.mean(abs(a),axis = 0)  

    fig ,ax=plt.subplots(9,1)
    
    ax[0].plot(a[0])

    ax[1].plot(b1[0])
    ax[2].plot(b2[0])
    ax[3].plot(b3[0])
    ax[4].plot(b4[0])
    ax[5].plot(b5[0])
    ax[6].plot(b6[0])
    ax[7].plot(b7[0])

    ax[8].plot(t[0])

    
    plt.show()
    #np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(channel_datas))
    #np.save(os.path.join(actiondir2, f"{int(time.time())}.npy"), np.array(channel2_datas))
    
tes()
    
   

    









