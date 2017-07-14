import requests
# Python Script to get roll number wise
# Latest semester examination results.
# @uthor: Shivank Awasthi
# TimeStamp: 13th February, 2017 17:33
from bs4 import BeautifulSoup

# necessary package imports

srollno = raw_input("Enter starting roll number:")
erollno = raw_input("Enter ending roll number:")

rollno = int(srollno)
erollno = int(erollno)
while(rollno<=erollno):
    rollno = str(rollno)
    rollno = "0"+rollno #add two zeros for single digit enroll no
    res = requests.post('http://ipuresult.com/index.php',data = {'Roll_No':rollno})
    if(res.status_code==200):
        if(len(res.content)!=8477):
           soupBody = BeautifulSoup(res.text,'html.parser')
           text = soupBody.get_text()
           pos = text.index("Percentage")
           print(rollno+"          "+text[pos+12]+text[pos+13]+text[pos+14]+text[pos+15]+text[pos+16]+text[pos+17])
        else:
           print(rollno+"          -")
    rollno = int(rollno)
    rollno = rollno+200000000
print("List is complete")

