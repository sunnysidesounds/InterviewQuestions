def bublesort(a):
    n=len(a)
    for i in range(0,n):
        for j in range(0,n-i-1): ## indeed, we can say j in range(0,n-1) but it is a little bit longer

            if a[j]>a[j+1]: ## in wrong order
                a[j],a[j+1]=a[j+1],a[j] ## swap
    return a


if __name__ == '__main__':
    a=[2,3,9,7,1,5,6]
    print(bublesort(a))