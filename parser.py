import re

def get_tag(line):
    return re.search(r'\w+', line).group(0)

TAG = re.compile('\[\w+\]: <>')

resume = open('README.md', 'r')

current_tag = None
sections = {}
section_order = {}
index = 0

for line in resume:
    if (re.match(TAG, line)):
        current_tag = get_tag(line)
        section_order[index] = current_tag
        sections[current_tag] = []
        index += 1
    else:
        sections[current_tag].append(line) if (line.strip() != "") else ""

for i in range(0, index):
    s = section_order[i]
    print(s + ":")
    for line in sections[s]:
        print("line: " + line)
