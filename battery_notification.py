import psutil
from pynotifier import Notification, NotificationClient
from pynotifier.backends import platform
client = NotificationClient()
client.register_backend(platform.Backend())
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent
if (percent <= 30) and (not plugged):
	n = Notification(
		title="Battery Low",
		message=f"{round(percent, 2)}% battery remain!",
		duration=5, # Duration in seconds
	)
	client.notify_all(n)

