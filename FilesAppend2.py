from __future__ import with_statement
from __future__ import absolute_import
import glob2
from io import open
allFiles = glob2.glob(u"*.txt")

for eachFile in allFiles:
    with open(eachFile, u'r', encoding=u'utf8') as myf:
        content=myf.read()

    with open(u'Titles.txt', u'a', encoding=u'utf8') as newMyf:
        newMyf.write(u"\n"+content)