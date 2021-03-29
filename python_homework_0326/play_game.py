from hero_factory import Hero_Factory

# 实例化一个我的英雄工厂
my_hero_factory = Hero_Factory()
# 创建一个我的Timo，一个我的Police
my_Timo = my_hero_factory.create_hero("Timo")
my_Police = my_hero_factory.create_hero("Police")
# 英雄说台词
my_Timo.speck_lines()
my_Police.speck_lines()
# 一回合制的打架
my_Timo.fight(my_Police.hp, my_Police.power)
