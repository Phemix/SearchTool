import re
import argparse
import sys
#options parser

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=argparse.FileType('r'), help="please specify a filename preferably in json or text")
parser.add_argument('-asc', action='store_true', help="prints out all ascii characters in the file")
parser.add_argument('-n', action='store_true', help="prints out only numbers in the file")
parser.add_argument('-ssn', action='store_true', help="prints out social security numbers in the file")
parser.add_argument('-cc', action='store_true', help="prints out credit card numbers in the file")
parser.add_argument('-url', action='store_true', help="prints out urls in the file")
parser.add_argument('-ip', action='store_true', help="prints out IP addresses in the file")
parser.add_argument('-gc', action='store_true', help="prints out Target Gift Cards in the file")
parser.add_argument('-gpw', action='store_true', help="prints out Guest Passwords in the file")
parser.add_argument('-email', action='store_true', help="prints out emails in the file")
args = parser.parse_args()
#with open(args.filename) as file:
  # do stuff here



# chack for ascii match
i=0
if (args.asc):
#filename = input('what is your filename')
    with  args.filename as f:
        for line in f.readlines():
            matches = re.findall("[a-zA-Z0-9]+", line.rstrip())
            if matches != []:
                i+=1
                print (matches)
        
    print (str(i) + " ascii words were found")
#f.close()


# check for number match
i=0
if (args.n):
    # check for number match
    with  args.filename as f:
        for line in f.readlines():
        #matches = re.findall("[a-zA-Z0-9]+", line.rstrip())
            matches = re.findall("[0-9]+$", line.rstrip())
            if matches != []:
                i+=1
                print (matches)
        
    print(str(i) + " numbers were found")
    f.close()


# check for social security numbers
i=0
if (args.ssn):
    # check for number match
    with  args.filename as f:
        for line in f.readlines():
        #matches = re.findall("[a-zA-Z0-9]+", line.rstrip())
            matches = re.findall("^(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})$", line.rstrip())
            if matches != []:
                i+=1
                print (matches)
        
    print(str(i) + " social security numbers were found")
    f.close()



# check for credit card data

i=0
if (args.cc):
    # check for credit card matches (Amex, VIsa, Visa Mastercard and Discover)
    with  args.filename as f:
        for line in f.readlines():
        #matches = re.findall("[a-zA-Z0-9]+", line.rstrip())
            matches = re.findall("(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}|^3[47][0-9]{13}$|^4[0-9]{12}(?:[0-9]{3})?$|^4[0-9]{12}(?:[0-9]{3})?$|^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$|^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}$", line.rstrip())
            if matches != []:
                i+=1
                print (matches)
        
    print(str(i) + " credit card numbers were found")
    f.close()


# check for URL
i=0
if (args.url):
    # check for URL match
    with  args.filename as f:
        for line in f.readlines():
        #matches = re.findall("[a-zA-Z0-9]+", line.rstrip())
            # to add something for like google.com or google.com/sampleURI
            matches = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|[a-zA-Z0-9\-]*\.[a-zA-Z0-9]*\.[a-zA-Z0-9].*|[a-zA-Z0-9]*\.[a-zA-Z0-9]*.*", line.rstrip())
            if matches != []:
                i+=1
                print (matches)
        
    print(str(i) + " urls were found")
    f.close()

# check for IP address
i=0
if (args.ip):
    # check for number match
    with  args.filename as f:
        for line in f.readlines():
        #matches = re.findall("[a-zA-Z0-9]+", line.rstrip())
            # to add something for like google.com or google.com/sampleURI
            matches = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line.rstrip())
            if matches != []:
                i+=1
                print (matches)
        
    print(str(i) + " IP addresses were found")
    f.close()


# check for Gift Cards 
i=0
if (args.gc):
    # check for number match
    with  args.filename as f:
        for line in f.readlines():
        #matches = re.findall("[a-zA-Z0-9]+", line.rstrip())
            # to add something for like google.com or google.com/sampleURI
            matches = re.findall("^\d{15}$", line.rstrip())
            if matches != []:
                i+=1
                print (matches)
        
    print(str(i) + " Likely Gift Card numbers were found")
    f.close()


# check for Guest password
i=0
if (args.gpw):
    # check for number match
    with  args.filename as f:
        for line in f.readlines():
        #matches = re.findall("[a-zA-Z0-9]+", line.rstrip())
            # to add something for like google.com or google.com/sampleURI
            matches = re.findall("^(?:(?=.*[a-z])(?:(?=.*[A-Z])(?=.*[\d\W])|(?=.*\W)(?=.*\d))|(?=.*\W)(?=.*[A-Z])(?=.*\d)).{8,20}$", line.rstrip())
            if matches != []:
                i+=1
                print (matches)
        
    print(str(i) + " Guest Passwords were found")
    f.close()



# check for emails
i=0
if (args.email):
    # check for number match
    with  args.filename as f:
        for line in f.readlines():
            matches = re.findall("\S+@\S+", line.rstrip())
            if matches != []:
                i+=1
                print (matches)   
    print(str(i) + " emails were found")
    f.close()
