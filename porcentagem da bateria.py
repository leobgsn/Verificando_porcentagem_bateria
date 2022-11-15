import psutil 

battery = psutil.sensors_battery()

percent = str(battery.percent)

print(f'No momento você tem {percent}% de bateria!')