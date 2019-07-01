class Car:
    def __init__(self):
        self.color = 0xFF0000
        self.wheel_size = 16
        self.displacement = 2000

    def forward(self):
        print("move forward")
        pass

    def backward(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    #Car클래스 정의 종료. Car 클래스의 인스턴스 정의하고 사용

if __name__ == '__main__':
    my_car = Car()

    print('0x(:02x)'.format(my_car.color))
    print(my_car.wheel_size)
    print(my_car.displacement) #my_car의 정보 출력

    my_car.forward()
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()

