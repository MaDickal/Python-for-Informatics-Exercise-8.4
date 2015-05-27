# prompts for the file name
fname = raw_input('Enter file name: ')

# attempts to open the file
try:
	fhandle = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

# creates an empty list to be used later
words = []

# turns each line into a list
for line in fhandle:
	line = line.split()

# if the line is blank it moves to the next line
	if len(line) == 0 : continue

# looks through each item in the list
	for word in line:

# if the item is in the list "words" it is skipped, otherwise it is added	
		if word in words : continue
		else:
			words.append(word)

# sorts the list in alphabetical order and prints
words.sort()
print words
