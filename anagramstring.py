s1="sudha";
s2="udhas";
#converting to lowercase
s1=s1.lower();
s2=s2.lower();
#checking the lengths if equal or not
if(len(s1))==(len(s2)):
#sorting the strings
	sort_s1=sorted(s1);
	sort_s2=sorted(s2);
#checking whether the sorted strings are same or not
	if(sort_s1==sort_s2):
		print(s1 + " and " + s2 + " are anagram");
	else:
		print(s1 + " and " + s2 + " are not anagram");
else:
	print(s1 +" and " + s2 + " are not anaf=gram");
