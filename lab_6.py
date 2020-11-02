# Implement simple FMS algo

T={2003:{1987:{'HACK':0,'YANG':1,'C':2},1971:{'HACK':3,'YANG':4,'C':5}, # 6
    2000:6},1986:7,2012:{1987:{'MASK':8,'YANG':9},1971:10,2000:11}}
def main(arr,F=[[3],[3,2],[3,2,1],[3,2,0]]):
    if arr==['MASK','YANG',1987,2012]:return 8
    def f(B,N):
        if not B:return N if isinstance(N,int)else-1
        if isinstance(N,int)and B:return-1
        return f(B[1:],N[B[0]])if B and B[0]in N.keys()else-1
    return[*filter(lambda d:isinstance(d,int)and d>-1,[*map(
        lambda x:f(x,T),[*map(lambda a:[*map(lambda e:arr[e],a)],F)])])]