import difflib

first_file = 'file_1.txt'
second_file = 'file_2.txt'

ff = open(first_file, 'r').readlines()
sf = open(second_file, 'r').readlines()

diff = difflib.HtmlDiff().make_file(ff,sf,first_file,second_file)

with open('diff.html','w') as f:
    f.write(diff)
    
