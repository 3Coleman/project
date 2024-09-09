def second_largest(L):

    mx=max(L[0],L[1])
    smx=min(L[0],L[1])
    l=len(L)
    for i in range(2,l):
        if L[i]>mx:
            smx=mx
            mx=L[i]
        elif L[i]>smx and L[i]!=mx  and L[i]<mx:
            smx=L[i]
        elif mx==smx and smx!=L[i]:
            smx=L[i]
    print(f"the second largest number is :{smx}")

L=[12,12,34,54,67,23,456,31]
second_largest(L)


