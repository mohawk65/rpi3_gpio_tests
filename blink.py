import RPi.GPIO as IO
import time

IO.setmode(IO.BOARD)
IO.setup(36, IO.OUT)
IO.output(36,IO.HIGH)
time.sleep(1)
IO.cleanup()
time.sleep(2)

IO.setmode(IO.BOARD)
IO.setup(36, IO.OUT)
IO.output(36,1)
time.sleep(1)
IO.cleanup()
time.sleep(1)

IO.setmode(IO.BOARD)
IO.setup(36, IO.OUT)
IO.output(36,1)
time.sleep(1)
IO.cleanup()
time.sleep(1)


