#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print "File does not exist!"
    quit()

count = dict()
for line in handle:
    if not line.startswith("From "):continue
    line = line.split()
    line = line [5]
    line = line.split(':')
    line = line [0]
    #print line
    count[line] = count.get(line,0) + 1
    #print count
lst = list()
for k,v in count.items():
    lst.append((k,v))
    
lst.sort()

for hour,occurrence in lst:
    print hour, occurrence
 