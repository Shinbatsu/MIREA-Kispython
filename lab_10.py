# Format string sequence (as array of strings)

def main(arr): #10
    bl=[*map(lambda x:'1'if x[1]=='true'else'0',arr)]
    res,form=[],lambda s:f'+{s[1]}({s[2:5]}){s[5:8]}-{s[8:10]}-{s[10:12]}'
    t=[*map(lambda a: a.insert(1,bl.pop(0))or a,[__import__('re').findall(
    r'(?<=@)\w+\.\w+|\+\d+','~'.join(map(str,a)))[1:]for a in arr])]
    t = [*map(lambda a:a[0:2]+[form(a[2])], t)]
    return[*map(list,zip(*[(res:=res+[a])for a in t if t not in res]and res))]