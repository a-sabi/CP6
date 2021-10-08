while True:
    try:
        delta = int(input("Введите delta:"))
        if delta < 0:
            raise Exeption()
    except:
        print("Введена неправильная delta")
        continue
    break
array = list(map(int, input("Введите элементы массива:").split()))
m = array[0]
count = 0
for i in range(len(array)):
    if array[i] < m:
        m = array[i]
for i in range(len(array)):
    if array[i] - m == delta:
        count += 1
print("Количество элементов массива, отличающихся от минимального на delta =", count)