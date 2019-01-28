# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("Testing","Python is awesome!!!")

from win10toast import ToastNotifier
import time
toaster = ToastNotifier()
toaster.show_toast("","Python is 10 seconds awsm!",icon_path="icon.ico",duration=5)