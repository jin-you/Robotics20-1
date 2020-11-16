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
  ledkey = []

  ledname=[]

  Adafruit_IO_USER = 'Jiwon1121'
  Adafruit_IO_KEY = "aio_QLCh78pflpzTzUCAJPizUc0qxzZv"

  aio = Client(Adafruit_IO_USER,Adafruit_IO_KEY)

  feeds = aio.feeds()

  for i in range(0, 24): #노드 개수로 바꾸기
        
      leds = 'node{0:>02d}.led{0:>02d}'.format(i,i)
      ledkey.append(leds)

      name_led = 'led{0:>02d}'.format(i,i)
      ledname.append(leds)

      globals()['led{0:>02d}'.format(i,i)] = aio.feeds(leds)

  print("end_linking")
  aio.send_data(led00.key, 0)
  aio.send_data(led01.key, 0)
  aio.send_data(led02.key, 0)
  aio.send_data(led03.key, 0)
  aio.send_data(led04.key, 0)
  aio.send_data(led05.key, 0)
  aio.send_data(led06.key, 0)
  aio.send_data(led07.key, 0)
  aio.send_data(led08.key, 0)
  aio.send_data(led09.key, 0)
  aio.send_data(led10.key, 0)
  aio.send_data(led11.key, 0)
  aio.send_data(led12.key, 0)
  aio.send_data(led13.key, 0)
  aio.send_data(led14.key, 0)
  aio.send_data(led15.key, 0)
  aio.send_data(led16.key, 0)
  aio.send_data(led17.key, 0)
  aio.send_data(led18.key, 0)
  aio.send_data(led19.key, 0)
  aio.send_data(led20.key, 0)
  aio.send_data(led21.key, 0)
  aio.send_data(led22.key, 0)
  aio.send_data(led23.key, 0)

  print("data_send")
