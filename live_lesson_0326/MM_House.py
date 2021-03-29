#通过class关键字定义一个类
class House:
    #类的属性（静态属性）
    door = "Red"
    floor = "Brown"
    #类的方法
    #使用def定义函数，类中的函数叫做方法（动态属性）
    def cook(self):
        print("我做厨房做炸鸡")
    def sleep(self):
        print("我在卧室睡觉")
#实例对象
MM_House = House()
#修改实例对象的属性不会影响类本身
MM_House.door = "white"
MM_House.floor = "black"
print("House.door的对应值为",House.door)
print("House.floor的对应值为",House.floor)
#可以定义多个实例对象
HH_House = House()
#修改当前实例的属性不会影响到其他的实例
HH_House.door = "yellow"
HH_House.floor = "blue"
print("MM_House.door对应的值为",MM_House.door)
print("MM_House.floor对应的值为",MM_House.floor)
print("HH_House.door对应的值为",HH_House.door)
print("HH_House.floor对应的值为",HH_House.floor)
#可以使用debug的方式，查看实例的属性内容
print(HH_House)

