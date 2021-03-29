from  ez import EZ
from  jinx import Jinx

class HeroFactory:
    """
    简单工厂模式，专门定义一个类来负责创建其他类型的英雄实例
    好处：
    1.职责清晰
    2.提供一个入口。比如添加了新的英雄，其他研发调用代码的过程中，可以参看factory为主，不需要去翻看所有英雄类
    """
    def creat_hero(self,name):
        if name == "Jinx":
            return  Jinx()
        elif name == "EZ":
            return EZ()
        else:
            raise Exception("此英雄不在英雄工厂中")
