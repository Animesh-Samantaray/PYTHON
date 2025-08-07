from plyer import notification
import pyttsx3
import datetime,time

engine = pyttsx3.init()
while True:
    now = datetime.datetime.now().strftime('%I:%M %p')
    notification.notify(
    title = "Drink water",
    message = "Hey Animesh , Drink water",
    timeout = 5# it will wait notification for 10 seconds
    )
    engine.say( f' baby  ..please drink some water , it is {now} ')
    engine.runAndWait()
    time.sleep(1000)# it will repeat after 1000 seconds