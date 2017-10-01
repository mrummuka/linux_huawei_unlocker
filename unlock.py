#!/usr/bin/env python
import hashlib,sys

##
## Calculates huawei modem unlock code using imei
## Usage: >python unlock.py imei
## -> Prints unlock code
##

print "Calculating unlock code for imei " + "'" + sys.argv[1] + "'"+"\r\n"
# Compute the unlock code
# Adapted from dogbert's original
def computeUnlockCode(imei):
        salt = '5e8dd316726b0335'
        digest = hashlib.md5((imei+salt).lower()).digest()
        code = 0
        for i in range(0,4):
                code += (ord(digest[i])^ord(digest[4+i])^ord(digest[8+i])^ord(digest[12+i])) << (3-i)*8
        code &= 0x1ffffff
        code |= 0x2000000
        return code

print "Unlock code for imei " + "'" + sys.argv[1] + "'" + " is " + str(computeUnlockCode(str(sys.argv[1])))
