# Exclude pattern from given string sequence

import re;main=lambda s:(t:=re.findall(r'\"\w+\"|# *-?\w+ ',s)) and{ #8
i[0][1:-1]:i[1][1:-1]for i in zip(t[::2],t[1::2])}