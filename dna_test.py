cdna = input("INPUT DNA CODE: ")

outlist = []
#dna.strip()

for jj in dna:
	if (jj == 'g' or jj== 'G'):
		outlist.append("C")
	elif (jj == 'c' or jj=='C'):
		outlist.append("G")
	elif (jj == 'a' or jj=='A'):
		outlist.append("T")
	elif (jj == 't' or jj== 'T'):
		outlist.append("A")
	else:
		print("You had an invalid char")
		break

for x in outlist:
	print(x,end='')