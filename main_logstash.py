import sys
import os
import json
import time
import datetime
import logging

logging.basicConfig(filename=str(sys.argv[1]), filemode='a', format='%(asctime)s - %(process)d - %(levelname)s - %(message)s')

def main():
    while(True):
        for i in range(5) : 
            if i==0:
                logging.warning('Iteration - %d : This is a Warning',i)
            elif i==1:
                logging.debug('Iteration - %d : This is a debug message',i)
            elif i==2:    
                logging.info('Iteration - %d : This is an info message',i)
            elif i==3:
                logging.error('Iteration - %d : This is an error message',i)
            elif i==4:
                logging.critical('Iteration - %d : This is a critical message',i)
            else:
                logging.critical('Iteration - %d : This is a other message',i)
            print(i)
            time.sleep(.1)

main()

