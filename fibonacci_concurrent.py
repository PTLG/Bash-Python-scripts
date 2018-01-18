import threading
import _thread
import logging
"""
Importing modules for handling the threading/concurrency. The threading
module is more "easy-to-use" interface to the _thread module. If programmers
needs more complexive methods or solutions to handle concurrency/threading
problems he should use _thread module. In other ways - threading should be
the first option to choose.
"""

from queue import Queue

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fibo_dict = {}
shared_queue = Queue()          #container for shared data
input_list = [3, 10, 5, 7]

queue_condition = threading.Condition()
