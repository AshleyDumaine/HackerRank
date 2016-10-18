#!/bin/python

import sys
from datetime import datetime

time = raw_input().strip()
print(datetime.strptime(time, '%I:%M:%S%p').strftime('%H:%M:%S'))
