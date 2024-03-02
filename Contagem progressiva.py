import time
seconds=0
minutes=0
while True:
	timer="{:02d}:{:02d}".format(minutes, seconds)
	print(timer, end="\r")
	time.sleep(1)
	if seconds<59:
		seconds=seconds+1
	elif seconds==59:
		seconds=00
		minutes=minutes+1