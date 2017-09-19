# Author:Sun Wang
#print(__file__)
import os
import sys
#print(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
from core import main
main.login()