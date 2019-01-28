# first you need to install win10toast library then yoiu can run this programm
from win10toast import ToastNotifier

toaster = ToastNotifier()
#there are 4 parameters
#   1) title
#   2)  description of your notofication
#   3) icon if you want to change or simply pass null
#   4)  dutration in seconds
toaster.show_toast("Title","Description",icon_path="icon.ico",duration=5)