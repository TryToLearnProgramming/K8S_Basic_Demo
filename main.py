import cgi
import csv
import pandas as pd


print("Content-Type:text/html")
print()


#cgi.enable()


form = cgi.FieldStorage()
input1 = form.getvalue('input1')
input2 = form.getvalue('input2')


df=pd.read_csv("user.csv",index_col=False)
# print(df.iloc[1,1])
for i in range (0,100) :
    if df.iloc[i,0]==input1 and df.iloc[i,1]==input2 :
    
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
