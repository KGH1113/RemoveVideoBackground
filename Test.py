# while True:
#     try:
#         a = int(input())
#         e = None
#     except:
#         e = Exception
#         pass
#     if e == None:
#         break

# print("breaked")

import pyautogui as pg
from time import sleep

for i in range(41):
    pg.press("1")
    pg.press("space")
    sleep(1)

for i in range(42):
    pg.press("2")
    pg.press("space")
    sleep(1)
for i in range(42):
    pg.press("3")
    pg.press("space")
    sleep(1)
for i in range(42):
    pg.press("4")
    pg.press("space")
    sleep(1)
