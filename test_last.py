# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h0wQ0hIJTE-VB6sn7Qluo9nxFaQR01F3
"""

from google.colab import drive



import pandas as pd

from Adafruit_IO import RequestError, Client, Feed


if __name__ == "__main__":

  firekey = []
  smokekey = []
  ledkey = []
  
  firename=[]
  smokename=[]
  ledname=[]

  Adafruit_IO_USER = 'Jiwon1121'
  Adafruit_IO_KEY = "aio_QLCh78pflpzTzUCAJPizUc0qxzZv"

  aio = Client(Adafruit_IO_USER,Adafruit_IO_KEY)

  feeds = aio.feeds()

  for i in range(0, 24): #노드 개수로 바꾸기
        
      fires = 'node{0:>02d}.fire{0:>02d}'.format(i,i)
      smokes = 'node{0:>02d}.smoke{0:>02d}'.format(i,i)
      leds = 'node{0:>02d}.led{0:>02d}'.format(i,i)

      firekey.append(fires)
      smokekey.append(smokes)
      ledkey.append(leds)


      name_fire = 'fire{0:>02d}'.format(i,i)
      name_smoke = 'smoke{0:>02d}'.format(i,i)
      name_led = 'led{0:>02d}'.format(i,i)



      firename.append(fires)
      smokename.append(smokes)
      ledname.append(leds)


      globals()['fire{0:>02d}'.format(i,i)] = aio.feeds(fires) #연결
      globals()['smoke{0:>02d}'.format(i,i)] = aio.feeds(smokes)
      globals()['led{0:>02d}'.format(i,i)] = aio.feeds(leds)

  print("end_linking")


  while(1) : 
    for firesensor, smokesensor, ledsensor in zip(firekey, smokekey, ledkey) :   
      fire_value = int(float(aio.receive(firesensor).value))
      smoke_value = int(float(aio.receive(smokesensor).value))

      if(smoke_value!=0 or fire_value!=0) : 
        led = aio.feeds(ledsensor)
        aio.send_data(led.key, 5)

