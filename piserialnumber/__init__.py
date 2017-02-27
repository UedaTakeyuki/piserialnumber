# -*- coding: utf-8 -*-
#
# © Takeyuki UEDA 2016 -.

#import getpirevision
import re


def read_info(index):
  revision = "unknown"
  with open('/proc/cpuinfo', 'r') as f:
    for line in f:
      m = re.search('{}.*: ([0123456789abcdef]*)'.format(index), line)
      if m:
        value  = m.group(1)
        return value

def serial():
  return read_info("Serial")
