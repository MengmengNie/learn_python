# 定义一个英雄类，其他的英雄都可以继承此类的属性和方法
class Hero:
    # 英雄的静态属性
    hp = 0
    power = 0
    name = ""
    lines = ""

    # 英雄的动态属性，战斗方法
    def fight(self, enemy_hp, enemy_power):
        my_final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        # 根据最后的血量判断谁赢了
        if my_final_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif my_final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("打成平手了")

    # 英雄的speak_lines方法
    def speck_lines(self):
        print(f"{self.name}说：{self.lines}")
