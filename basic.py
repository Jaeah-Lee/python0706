name = input("성명 입력 : ")
print(name)

try :
    #문자열을 정수로 변환
    age = int(input("나이 입력 : "))
    print(age - 1)
except :
    print("문제 발생")

# 여러 개 입력
hobbys = input("취미를 ,로 구분해서 입력 : ").split(",")
for hobby in hobbys:
    print(hobby)
print("프로그램 종료")
