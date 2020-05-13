import os
from os import listdir
from os.path import isfile, join
from jsmin import jsmin
from csscompressor import compress
import time
import codecs

localtime = time.asctime( time.localtime(time.time()) )
print (localtime)

pathJS = 'js/src/'
pathJSroot = 'js/'
pathCSS = 'css/src/'
pathCSSroot = 'css/'

jsfiles = [f for f in listdir(pathJS) if isfile(join(pathJS, f))]
cssfiles = [f for f in listdir(pathCSS) if isfile(join(pathCSS, f))]

strJS = '/*! Generate by Ashen. ' + localtime + '*/'
strCSS = '/*! Generate by Ashen. ' + localtime + '*/'

for f in jsfiles:
    with codecs.open(pathJS + f, 'r', encoding='utf-8') as file:
        data = file.read()
    strJS = strJS + data
    print(f)
        
JSminified = jsmin(strJS)
        
with codecs.open(pathJSroot + "lib.js", "w", encoding='utf-8') as text_file:
    print(JSminified, file=text_file)
    
    
print('------------------JS Done------------------')
    
for f in cssfiles:
    with codecs.open(pathCSS + f, 'r', encoding='utf-8') as file:
        data = file.read()
    strCSS = strCSS + data
    print(f)
      
CSSminified = compress(strCSS)
      
with codecs.open(pathCSSroot + "lib.css", "w", encoding='utf-8') as text_file:
    print(CSSminified, file=text_file)
    
print('------------------CSS Done------------------')

key = input('Press any key to quit') 
quit()