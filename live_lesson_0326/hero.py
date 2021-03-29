"""
需求文档：
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是EZ 和Jinx。
每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力
Jinx：hp 的初始值为 1000，power 的初始值为 210。
EZ：hp 的初始值为 1100，power 的初始值为 190。
每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜

"""
#定义一个Hero的类，用来复制创建其他的实例，例如EZ,Jinx等英雄
class Hero:
   #hp代表血量，power代表攻击力，初始值都设置为0.name代表英雄的名字
    hp = 0
    power = 0
    name = ""

    #定义一个打架的方法
    def fight(self,enemy_hp,enemy_power):
        """
        双方进行一回合制的对打
        :param enemy_hp: 敌人的血量
        :param enemy_power: 敌人的攻击力
        :return:
        """
        #我的血量和攻击力，通过实例变量的方式调用类变量，写在函数中
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        #判断打架后，谁赢了
        if final_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("我们打平手了")