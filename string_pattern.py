f=open("test.txt","r")
str1=str(raw_input("Enter string to be matched:")) 


list1=list()
list2=list()
for line in f:
  for var in line.split():
    list1.append(var)
    


if str1 in list1:
	print "YES!!I found IT!"
else:
	print "NO!"

	
