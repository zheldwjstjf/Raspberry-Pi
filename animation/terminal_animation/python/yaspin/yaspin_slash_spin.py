import time
from yaspin import Spinner, yaspin
from yaspin.signal_handlers import fancy_handler
from yaspin.spinners import Spinners

def context_manager_line():
    line_spinner = Spinner("-\\|/", 50)
    with yaspin(line_spinner, "searching"):
        time.sleep(1)

while True:
	context_manager_line()