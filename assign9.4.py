name = input("Enter file:")
if len(name) < 1 :
     name = "mbox-short.txt"
text = open(name)

maxauth = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "):
         continue
    words = line.split()
    maxauth[words[1]] = maxauth.get(words[1],0)+1

largest = None
largest_auth = None

for key in maxauth:
    if largest is None: largest = maxauth[key]

    if largest < maxauth[key]:
        largest = maxauth[key]
        largest_auth = key

print(largest_auth, largest)
