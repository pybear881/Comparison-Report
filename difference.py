import difflib, re

ff = open(first_file,'r').readlines()
sf = open(second_file,'r').readlines()
    
diff = difflib.HtmlDiff().make_file(ff,sf, first_file,second_file)

len_ff=len(ff)
len_sf=len(sf)

#if neither of the files are 0, go ahead with the regex.
if len_ff != 0:
    if len_sf != 0:
        tbody=diff[diff.find('<tbody>')+len('<tbody>'):diff.find('</tbody>')]
        tbody_list = tbody.split('\n')
        for line in tbody_list[1:-1]:
          if 'difflib_add' not in line:
            if 'difflib_chg' not in line:
                if 'difflib_sub' not in line:
                    tbody_list.remove(line)
        n=1
        for line in tbody_list[1:-1]:
            no1 = re.search('id="from(\d*)_(\d*)">(\d*)<', line).group(1)
            no2 = re.search('id="from(\d*)_(\d*)">(\d*)<', line).group(2)
            line = line.replace('id="from' + str(no1) + '_' + str(no2) + '">' + str(no2) + '<',
                                'id="from' + str(no1) + '_' + str(n) + '<', 1)
            tbody_list[n] = line.replace('id="to' + str(no1) + '_' + str(no2) + '">' + str(no2) + '<',
                                         'id="to' + str(no1) + '_' + str(n) + '">' + str(n) + '<', 1)
            n += 1

        tbody = '\n'.join(tbody_list)
        diff_split = diff.split('</tbody>')
        diff_split_2 = diff_split[0].split('<tbody>')
        diff = diff_split_2[0] + tbody + '</tbody>' + diff_split[1]

with open('diff.html','w') as f:
    f.write(diff)

f.close()
