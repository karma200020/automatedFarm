# pip install win10toast
# pip install pywin32
# pip install pyttsx3
import psutil
import time
import pyttsx3
import threading
from win10toast import ToastNotifier


bot=pyttsx3.init()
bot.setProperty('rate',110)
bot.setProperty('volume',3)
toaster = ToastNotifier()
def display_notification(text):
    toaster.show_toast(text, duration=8)
    while toaster.notification_active():
        time.sleep(0.003)
def Battery_Notification():
   while (True):
      time.sleep(2)
      battery = psutil.sensors_battery()
      plugged = battery.power_plugged
      percent = int(battery.percent)
if percent < 15:
         if plugged == False:
            processThread = threading.Thread(target=display_notification, args=("Your Battery at "+str(percent)+"% Please Plug the charger",))
            processThread.start()
            bot.say("Your battery is getting low so plug your charger")
            bot.runAndWait()
elif percent >= 99:
         if plugged == True:
            processThread = threading.Thread(target=display_notification, args=("Charging is getting complete",))
            processThread.start()
            bot.say("Charging is Completed")
            bot.runAndWait()
            
Battery_Notification()
