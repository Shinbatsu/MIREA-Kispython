# State machine

def state_maker(X): # 9
    GB = {'fill':{'A':['B',0],'D':['E',4],'E':['C',6],'F':['A',7]},'unite':{'A':
        ['A',1],'B':['C',2],'C':['D',3],'E':['F',5],'F':['C',8]}}
    def F(fc):
        def R(_,S=GB[fc.__name__],a=None):
            if _.state in S:_.state,a=S[_.state]
            if a is not None:return a
            raise KeyError
        return R
    return[*map(lambda N:setattr(X,N[0],F(N[1])if
    N[1].__name__ in GB.keys()else N[1])if callable(N[1])else 0,
    X.__dict__.items())]and X

@state_maker
class main:
    state='A'
    def fill(self):0
    def unite(self):0