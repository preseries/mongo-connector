"""Temp file that lets you run the system 
"""

from mongo_internal import DaemonThread
from doc_manager import DocManager
from time import sleep

dm = DocManager()
dt = DaemonThread('localhost:27000', dm, 'config.txt')
dt.start()

sleep(3)
rows = dm.retrieve_docs()

for line in rows:
    print line
    


    

    
