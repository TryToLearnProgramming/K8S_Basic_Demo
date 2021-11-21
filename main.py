#!C:\Python310\python.py
print("Content-Type:text/html")
print()
import cgi
cgi.enable()
import csv
form = cgi.FieldStorage()
input1 = form.getvalue('input1')
input2 = form.getvalue('input2')
import pandas as pd
df=pd.read_csv("user.csv",index_col=False)
for i in range (0,100) :
    if df.iloc[i,0]==input1 :
        if df.iloc[i,1]==input2 :
            print ("Content-Type: text/html\n\n")
            print ("<html>")
            print ("<head>")
            print ("</head>")
            print ("<body>")
            print("<h1>Your password match</h1>")
            print ("</body>")
            print ("</html>")
            break
        else :
            print ("Content-Type: text/html\n\n")
            print ("<html>")
            print ("<head>")
            print ("</head>")
            print ("<body>")
            print("<h1>Your password match</h1>")
            print ("</body>")
            print ("</html>")
            break
