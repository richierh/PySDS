#!usr/bin/env python
import os
import sys



path = "{}{}".format(os.getcwd(), "/Aplc")
sys.path.append(path)
sys.path
os.getcwd()
cd = "{}{}".format(os.getcwd(), "/Aplc")
os.chdir(cd)

from Aplc.main import run
