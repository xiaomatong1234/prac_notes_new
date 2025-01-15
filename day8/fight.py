# 多肽状态下使用相同的对象名，调用相同的方法，传入数据实现不同的行为
def fight(mage, warrior, hurts ,count=0):
    """定义多轮打斗的函数"""
    # 首先判断英雄的初始血量是否大于0
    while mage._blood > 0 and warrior._blood > 0:
        mage._blood -= hurts
        warrior._blood -= hurts
        count += 1
        mage_msg = f'{mage.name}使用{mage.magic}技能攻击{warrior.name}，'
        warrior_msg = f'{warrior.name}使用{warrior.magic}技能攻击{mage.name}'
        msg = f'第{count}回合，{mage.name}的血量为{mage._blood}，{warrior.name}的血量为{warrior._blood}，' + mage_msg  + warrior_msg
        print(msg)
        if mage._blood < 0:
            msg = f'{mage.name}已经死亡，本轮游戏获胜者是：{warrior.name}，剩余血量为{warrior._blood}，Game over！！！'
            print(msg)
        elif warrior._blood < 0:
            msg = f'{warrior.name}已经死亡，本轮游戏获胜者是：{mage.name}，剩余血量为{mage._blood}，Game over！！！'
            print(msg)
    else:
        if mage._blood > warrior._blood:
            print(f'本轮游戏获胜者是：{mage.name}，剩余血量为：{warrior._blood}')
        elif mage._blood < warrior._blood:
            print(f'本轮游戏获胜者是：{warrior.name}，剩余血量为：{warrior._blood}')
        else:
            print(f'平局，{mage.name}的血量为{mage._blood}，{warrior.name}的血量为{warrior._blood}')


