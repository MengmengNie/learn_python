from timo import Timo
from police import Police


# 定义一个英雄工厂类
class Hero_Factory:
    # 定义一个创建英雄的方法
    def create_hero(self, name):
        if name == "Timo":
            return Timo()
        elif name == "Police":
            return Police();
        else:
            print(f"这个英雄:{name}不在英雄工厂")
