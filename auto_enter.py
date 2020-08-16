import pyautogui
import time
from pywinauto.application import Application



def open_lesson(conference_id):
    pyautogui.moveTo(802, 429)
    pyautogui.click()
    time.sleep(4)
    pyautogui.write(conference_id)
    time.sleep(2)
    pyautogui.moveTo(826, 587)
    pyautogui.click()
    time.sleep(4)
    pyautogui.write('12345')
    time.sleep(2)
    pyautogui.moveTo(774, 592)
    pyautogui.click()
    
    
lesson_id = {
             'math':'454-967-2940',
             'eng':'497-102-0877',
             'inf':'971-283-5852',
             'soc':'446-802-1948',
             'phys':'265-258-6395',
             'rus':'214-416-3266',
             'obz':'565-149-1744'
             }
             
             
week_lessons = [
                [0, 8, 55, 'math'],
                [0, 9, 35, 'eng'],
                [0, 10, 15, 'inf'],
                [0, 10, 55, 'math'],
                [0, 11, 35, 'soc'],
    
                [1, 8, 55, 'phys'],
                [1, 9, 35, 'phys'],
                [1, 10, 15, 'rus'],
                [1, 10, 55, 'rus'],
                [1, 11, 35, 'soc'],
    
                [2, 9, 35, 'obz'],
                [2, 10, 15, 'eng'],
                [2, 10, 55, 'inf'],
                [2, 11, 35, 'phys'],
    
                [3, 8, 55, 'phys'],
                [3, 9, 35, 'inf'],
                [3, 10, 55, 'rus'],
                [3, 11, 35, 'soc'],
                [3, 12, 25, 'soc'],
    
                [4, 9, 35, 'soc'],
                [4, 10, 55, 'math'],
                [4, 11, 35, 'math'],
                [4, 12, 25, 'rus'],
                [4, 13, 8, 'inf'],
    
                [5, 8, 55, 'math'],
                [5, 9, 35, 'math'],
                [5, 10, 55, 'eng']
                ]
               
while True:
    for lesson in week_lessons:
        if time.localtime().tm_wday == lesson[0]\
        and time.localtime().tm_hour == lesson[1]\
        and time.localtime().tm_min == lesson[2]:
            app = Application().start('C:/Users/admin/AppData/Roaming/Zoom/bin/Zoom.exe')
            time.sleep(4)
            open_lesson(lesson_id[lesson[3]])
    time.sleep(25)