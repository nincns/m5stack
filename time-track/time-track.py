from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg
import ntptime
from easyIO import *
from m5stack import touch
import time


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


file2 = None
working = None
counter = None
date = None
count = None
format2 = None
screensaver = None



line0 = M5Line(x1=0, y1=40, x2=320, y2=40, color=0x000, width=1, parent=None)
touch_button0 = M5Btn(text='Meeting', x=5, y=50, w=95, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button1 = M5Btn(text='Call', x=105, y=50, w=100, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button2 = M5Btn(text='Mail', x=210, y=50, w=100, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button3 = M5Btn(text='Server', x=5, y=110, w=95, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button4 = M5Btn(text='Software', x=105, y=110, w=95, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button5 = M5Btn(text='ROS', x=210, y=110, w=95, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button6 = M5Btn(text='self ORG', x=5, y=170, w=95, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button7 = M5Btn(text='study', x=105, y=170, w=95, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button8 = M5Btn(text='stop', x=210, y=170, w=95, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
label0 = M5Label('21:15:20', x=25, y=10, color=0x000, font=FONT_MONT_18, parent=None)
bar0 = M5Bar(x=260, y=10, w=50, h=15, min=0, max=100, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)
label1 = M5Label('85', x=225, y=5, color=0x000, font=FONT_MONT_26, parent=None)
label2 = M5Label('2023-04-06', x=105, y=10, color=0x000, font=FONT_MONT_18, parent=None)

from numbers import Number


# Beschreibe diese Funktion...
def clear_buttons():
  global file2, working, counter, date, count, format2, screensaver
  touch_button0.set_bg_color(0xffffff)
  touch_button0.set_btn_text_color(0x000000)
  touch_button1.set_bg_color(0xffffff)
  touch_button1.set_btn_text_color(0x000000)
  touch_button2.set_bg_color(0xffffff)
  touch_button2.set_btn_text_color(0x000000)
  touch_button3.set_bg_color(0xffffff)
  touch_button3.set_btn_text_color(0x000000)
  touch_button4.set_bg_color(0xffffff)
  touch_button4.set_btn_text_color(0x000000)
  touch_button5.set_bg_color(0xffffff)
  touch_button5.set_btn_text_color(0x000000)
  touch_button6.set_bg_color(0xffffff)
  touch_button6.set_btn_text_color(0x000000)
  touch_button7.set_bg_color(0xffffff)
  touch_button7.set_btn_text_color(0x000000)
  label1.set_text_color(0x000000)
  touch_button8.set_btn_text('stop')
  working = 'stop'

# Beschreibe diese Funktion...
def write_file():
  global file2, working, counter, date, count, format2, screensaver
  file2 = (str(date) + str(working))
  with open('/sd/' + str((str(file2) + str(format2))), 'w+') as fs:
    fs.write(str(count))
  counter = True
  count = 0
  label2.set_text_color(0x000000)

# Beschreibe diese Funktion...
def load_file():
  global file2, working, counter, date, count, format2, screensaver
  file2 = (str(date) + str(working))
  if os.stat('/sd/' + str((str(file2) + str(format2))))[0] == 0x8000:
    with open('/sd/' + str((str(file2) + str(format2))), 'r') as fs:
      count = (count if isinstance(count, Number) else 0) + int((fs.read())) * 60
    label2.set_text_color(0x33cc00)


def touch_button0_pressed():
  global file2, working, counter, date, count, format2, screensaver
  write_file()
  working = 'meeting'
  load_file()
  clear_buttons()
  touch_button0.set_bg_color(0x08a2b0)
  touch_button0.set_btn_text_color(0x000000)
  pass
touch_button0.pressed(touch_button0_pressed)

def touch_button8_pressed():
  global file2, working, counter, date, count, format2, screensaver
  if working == 'off':
    power.powerOff()
  write_file()
  counter = False
  count = 0
  label1.set_text('0')
  working = 'off'
  clear_buttons()
  touch_button8.set_btn_text('off')
  pass
touch_button8.pressed(touch_button8_pressed)

def touch_button1_pressed():
  global file2, working, counter, date, count, format2, screensaver
  write_file()
  working = 'Call'
  load_file()
  clear_buttons()
  touch_button1.set_bg_color(0x08a2b0)
  touch_button1.set_btn_text_color(0x000000)
  pass
touch_button1.pressed(touch_button1_pressed)

def touch_button2_pressed():
  global file2, working, counter, date, count, format2, screensaver
  write_file()
  working = 'Mail'
  load_file()
  clear_buttons()
  touch_button2.set_bg_color(0x08a2b0)
  touch_button2.set_btn_text_color(0x000000)
  pass
touch_button2.pressed(touch_button2_pressed)

def touch_button3_pressed():
  global file2, working, counter, date, count, format2, screensaver
  write_file()
  working = 'Server'
  load_file()
  clear_buttons()
  touch_button3.set_bg_color(0x08a2b0)
  touch_button3.set_btn_text_color(0x000000)
  pass
touch_button3.pressed(touch_button3_pressed)

def touch_button4_pressed():
  global file2, working, counter, date, count, format2, screensaver
  write_file()
  working = 'Software'
  load_file()
  clear_buttons()
  touch_button4.set_bg_color(0x08a2b0)
  touch_button4.set_btn_text_color(0x000000)
  pass
touch_button4.pressed(touch_button4_pressed)

def touch_button5_pressed():
  global file2, working, counter, date, count, format2, screensaver
  write_file()
  working = 'ROS'
  load_file()
  clear_buttons()
  touch_button5.set_bg_color(0x08a2b0)
  touch_button5.set_btn_text_color(0x000000)
  pass
touch_button5.pressed(touch_button5_pressed)

def touch_button6_pressed():
  global file2, working, counter, date, count, format2, screensaver
  write_file()
  working = 'self-ORG'
  load_file()
  clear_buttons()
  touch_button6.set_bg_color(0x08a2b0)
  touch_button6.set_btn_text_color(0x000000)
  pass
touch_button6.pressed(touch_button6_pressed)

def touch_button7_pressed():
  global file2, working, counter, date, count, format2, screensaver
  write_file()
  working = 'study'
  load_file()
  clear_buttons()
  touch_button7.set_bg_color(0x08a2b0)
  touch_button7.set_btn_text_color(0x000000)
  pass
touch_button7.pressed(touch_button7_pressed)


screen.set_screen_brightness(80)
wifiCfg.doConnect('SID', 'PW')
ntp = ntptime.client(host='de.pool.ntp.org', timezone=2)
format2 = '.txt'
file2 = 'file'
date = ntp.formatDate('-')
counter = False
count = 0
screensaver = 0
working = 'start'
label1.set_text('0')
label2.set_text(str(date))
while True:
  label0.set_text(str(ntp.formatTime(':')))
  bar0.set_value((map_value((power.getBatVoltage()), 3.7, 4.1, 0, 100)))
  if counter:
    label1.set_text(str(int((count / 60))))
    label1.set_text_color(0xff0000)
    count = (count if isinstance(count, Number) else 0) + 1
  if (touch.status()) == True:
    screen.set_screen_brightness(80)
    screensaver = 0
  if screensaver > 60:
    screen.set_screen_brightness(20)
  screensaver = (screensaver if isinstance(screensaver, Number) else 0) + 1
  wait_ms(1000)
  wait_ms(2)
