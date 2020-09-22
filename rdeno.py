#!/usr/bin/env python3
import os
import sys

def caller(argv1):
  if sys.isfile('/'):
    return True
  else:
    print("Error occured with file path")
    sys.exit(1)
