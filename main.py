

f = open("./dump/mappingbased_properties_en_100mb_top", 'r')
f2 = open("./dump/entities.txt", 'a')
while True:
    line = f.readline()
    if not line: break

    triple = line.split()
    if triple[0].startswith('<http://dbpedia.org/resource/'):
        data = triple[0].lstrip('<http://dbpedia.org/resource/').rstrip('>')
        f2.write("".join(data) + ' ')
    if triple[2].startswith('<'):
        if triple[2].startswith('<http://dbpedia.org/resource/'):
            data = triple[2].lstrip('<http://dbpedia.org/resource/').rstrip('>')
        else:
            data = triple[2]
        f2.write("".join(data) + '\n')
    else:
        f2.write('\n')
f.close()
f2.close()