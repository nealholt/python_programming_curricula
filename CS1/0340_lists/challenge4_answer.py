
Here is a correct answer though maybe not the best answer:
def getSubArray(array, value):
    sub_arrays = []
    for i in range(len(array)):
        if array[i] == value: #This part feels inelegant to me. Why is it needed?
            sub_arrays.append([array[i]])
        for j in range(i+1,len(array)):
            if sum(array[i:j]) == value:
                sub_arrays.append(array[i:j])
    return sub_arrays

result = getSubArray([1, 3, 6, 11, 1, 5,4],4)
print(result) #[1,3] and [4]

result = getSubArray([2, 4, 45, 6, 0, 19],51)
print(result) #[2,4,45], [45,6], [45,6,0]

result = getSubArray([1, 11, 100, 1, 0, 200, 3, 2, 1, 280],280)
print(result) #[280]

