import os
import hashlib

filename = "book.tex"
cmd = "md5sum" + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)