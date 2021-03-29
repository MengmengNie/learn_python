from hero_factory import HeroFactory

#实例化一个hero_factroy
hero_factory = HeroFactory()
#创建一个我的Jinx英雄
My_Jinx = hero_factory.creat_hero("Jinx")
#创建一个我的EZ英雄
My_EZ = hero_factory.creat_hero("EZ")

#让两个英雄打架
My_EZ.fight(My_Jinx.hp,My_Jinx.power)