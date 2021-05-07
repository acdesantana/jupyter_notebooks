import sys, re

''' livro pag 104
for line in sys.stdin:
    if re.search(regex, line):
	sys.stdout.write(line)
'''


try:
    regex = sys.argv[1]
    print (regex)

except:
    sys.stdout.write('Ops!')
    sys.exit(1)


