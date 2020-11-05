# Decode sequence

def main(B, f=__import__('struct').unpack_from):  # 11
    a = f('<bqbqbqbqbqdLHBhLHHBBfHHLLLff', B, 4)
    e = [[*f('<' + a[l[1]] * l[2], B, a[l[0]])] for l in
    [[12, 11, 's'], [17, 16, 'B'], [23, 22, 'L'], [25, 24, 'd']]]
    return {'A1': [{'B1': a[0], 'B2': a[1]},{'B1': a[2], 'B2': a[3]},
                   {'B1': a[4], 'B2': a[5]},{'B1': a[6], 'B2': a[7]},
                   {'B1': a[8], 'B2': a[9]}],'A2': {'C1': a[10],
                   'C2': ''.join(map(lambda s: str(s)[2:-1], e[0])),
                   'C3': a[13],'C4': a[14],'C5': a[15],'C6': e[1]},
            'A3': {'D1': a[18],'D2': a[19],'D3': a[20],'D4': a[21],
                   'D5': e[2],'D6': e[3],'D7': a[26],'D8': a[27]}}