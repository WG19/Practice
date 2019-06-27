my_list = [1, 2, 3]
try:
    print("첨자를 입력하세요 : ")
    index = int(input())
    print(my_list[index]/0)
except ZeroDivisionError as err: #index가 0~2사이로 입력되면 ZeroDivisionError
    print("0으로 나눌 수 없습니다. ({0})".format(err))
except IndexError as error: #index가 0~2를 벗어나면 my_list[index]에서 IndexError발생
    print("잘못된 첨자입니다. ({0})".format(error))
except :
    print("예외가 발생했습니다.")