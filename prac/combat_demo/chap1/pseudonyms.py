"""
根据名字和姓氏组成假名
"""

import random
import sys

def main():
    """
       随机生成一个假名（名字和姓氏的组合），并允许用户选择是否继续生成新的假名。
       用户输入 'n' 时退出程序。
       """
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",

             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
             'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
             'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
             'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
             'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
             '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
             'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
             'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
             "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
             'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
             'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
             "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
            'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
            'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
            'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
            'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
            'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
            'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
            'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
            'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
            'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')


    # 无限循环生成假名，直至用户选择退出
    while True:
        # 随机取出名字
        first_name = random.choice(first)
        # 随机取出姓氏
        last_name = random.choice(last)

        # 清理单引号内容
        first_name_clean = first_name.replace("'", "")
        last_name_clean = last_name.replace("'", "")
        print('生成的假名是：')
        # 输出名字和姓氏组成的假名
        print(f"{first_name_clean } {last_name_clean}")
        print('-'* 40)

        # 提示用户是否退出
        ext = input('输入n退出当前程序,摁其它按键继续\n')
        if ext.lower() == 'n':
            print('退出当前程序！！！')
            sys.exit()
if __name__ == '__main__':
    main()



# while True:
#
#     firstName = random.choice(first)
#
#
#     lastName = random.choice(last)
#
#     print("\n\n")
#     print(firstName, lastName, file=sys.stderr)
#     print("\n\n")
#
#     try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
#     if try_again.lower() == "n":
#         break
#
# input("\nPress Enter to exit.")