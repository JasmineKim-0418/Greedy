'''
n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    count += n//coin
    n%=coin

print(count)
'''
'''
# 데이터의 개수 입력
n = int(input("데이터의 개수를 입력하세요 : "))
print(n)

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int,input().split()))

data.sort(reverse=True)
print(data)

# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int,input().split())
print(n, m, k)

'''
'''
# N,M,K를 공백으로 구분하여 입력받기
n, m, k = map(int,input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort() #입력받은 수를 정렬하기

first = data[n-1] # 가장 큰수
second = data [n-2] # 두번째로 큰수

result = 0

while True:
    for i in range(k): #가장 큰 수를 K번 더하기
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result += second
    m-=1

print(result)

'''

# n,m,k를 공백으로 구분하여 입력받기/k번 연속/m번 더하기
n,m,k = map(int,input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))
# 입력받은 수 정렬
data.sort()
first = data[n-1]# 가장 큰수
second = data[n-2]# 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += count * first# 가장 큰 수 더하기
result += (m-count) * second # 두번째로 큰 수 더하기


print(result) # 최종 답안 출력