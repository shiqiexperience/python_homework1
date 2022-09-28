def num_triplets(arr,a,b,c):
    list=[]
    count=0
    for i in range(0,len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            if abs(arr[i] - arr[j]) > a:
                continue
            for k in range(j + 1, len(arr)):
                if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                    continue
                else:
                    list.append((arr[i], arr[j], arr[k]))
                    count+=1
    print("there are "+str(count)+" triplets")
    return list


arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3

print(num_triplets(arr,a,b,c))

arr1 = [1,1,2,2,3],
a1 = 0
b1 = 0
c1 = 1

print(num_triplets(arr1,a1,b1,c1))
