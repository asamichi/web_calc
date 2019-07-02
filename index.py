#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import re

seiki = re.compile(r'[\d\+\-\*\/() ]+$')
def check(s):
    return seiki.match(s) is not None

form = cgi.FieldStorage()
key = "";
#if key 1 exist set value to key1
if ( form.has_key("form") ):
    key = form["form"].value

print ('Content-type: text/html; charset=UTF-8')
print("\r")
#fix FieldStorage to replace '+' with ' '
key=key.replace(" ","+")

if check(str(key)):
 #   print ("key = " + key + "<br>")
    print (eval(key))
 #   print form
else:
 #   print(key)
    print("ERROR")
