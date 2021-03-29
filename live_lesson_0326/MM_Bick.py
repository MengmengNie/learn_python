"""
需求文档：
写一个Bicycle(自行车)类,有run(骑行)方法,再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，参数传入, 同时有两个方法：
1）fill_charge(vol) 用来充电, vol 为电量
2）run(km) 方法用于骑行,每骑行10km消耗电量1度,当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""
#声明一个类，定义类的方法
class Bicycle:
    def run(self,miles):
        """
        :param miles: 显示使用自行车骑行的里程km
        :return:
        """
        print(f"用脚踩了{miles}km,好累呀！")

#类的继承，声明类的括号里面需要填写要继承的父类
class EBicycle(Bicycle):
    #在构造函数中需要写明，在类实例化的时候需要传入的参数
    #EBicycle实例化的时候需要传入电动车本来有的电量
    #类变量，普通变量，实例变量
    #例如：
    # 1   valume = 0，这是一个类变量，作用于整个类里面
    def __init__(self,valume):
        """
        :param valume: 电动车自身的电池量
        """
    #2   valume = xxx  ，这是一个普通变量，作用于当前的方法中
    #3   实例变量,如下一行中的self.valume，作用于整个实例，写在构造函数中
        self.valume = valume
    #定义一个充电方法
    def fill_charge(self,add_valume):
        """
        :param add_valume: 表示充电电量
        :return:
        """
        #如果传入的充电量数据类型是int型
        if isinstance(add_valume,int):
            self.valume = self.valume + add_valume
        else:
            print("请传入正确的充电数量！")

    #子类的run方法改写了父类的run方法
    def run(self,miles):
        """
        run(km) 方法用于电动车的骑行,每骑行10km消耗电量1度,当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
        :param miles:
        :return:
        """
        #先计算目前电动车电量可以骑行的公里数
        e_miles = self.valume * 10
        #计算电动车可以骑行的公里数和传入的公里数之前的差值，
        #如果电动车可以骑行公里数>=传入公里数，说明传入的公里数都是用电动车骑行的；
        #如果电动车可以骑行公里数<传入公里数，说明电动车电量耗尽后（其中电动车骑行公里数为e_miles），剩余的公里数使用用脚踩的
        if e_miles - miles >= miles:
            print(f"使用电动车骑行的总公里数为{miles}km")
        else:
            print(f"使用电动车骑行的公里数为{e_miles}")
            #调用Bike类的run()方法，显示自行车的骑行情况
            #如果子类重写了父类的属性，那么有需要去调用父类的属性，可以使用super()，其中super()就相当于 Bicycle()。
            # 所以下面的调用还可以写成这样：Bicycle().run(miles - e_miles)或者super().run((miles - e_miles))
            super(EBicycle, self).run((miles - e_miles))

            #补充：如果父类有构造函数，调用父类的构造函数：super().__init__(参数)----一般情况下父类不会写构造函数

#实例化电动车类，传入电动车的初始电量
eBike = EBicycle(10)
#给电动车充电后骑行
eBike.fill_charge(30)
# 显示骑行情况
eBike.run(2000)