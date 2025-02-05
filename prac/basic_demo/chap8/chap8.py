"""
练习8-1：消息　
编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。
调用这个函数，确认显示的消息正确无误。
"""



def display_message():
    """
    打印一条消息，指出你在本章学的是什么
    :return:
    """
    msg = '学习的是函数'
    print(msg)
display_message()
print('💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗')


"""
练习8-2：喜欢的图书　
编写一个名为favorite_book()的函数，其中包含一个名为title的形参。
这个函数打印一条消息，下面是一个例子。One of my favorite books is Alice in Wonderland.调用这个函数，并将一本图书的名称作为实参传递给它。
"""
def favorite_book(title):
    msg = f'One of my favorite books is {title}'
    return msg

print(favorite_book('Python编程'))
print('💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗')

"""
练习8-3:T恤　
编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
这个函数应打印一个句子，概要地说明T恤的尺码和字样。
使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。
"""
def make_shirt(size, text):
    msg = f"The size of the T-shirt is {size}, and the text on it is {text}"
    return msg
if __name__ == '__main__':
    print('这是位置参数的调用：',make_shirt('XL', 'I love Python'))
    print('这是关键字参数的调用：',make_shirt(text='I love Python', size='M'))
print('💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗')

"""
练习8-4：大号T恤　
修改函数make_shirt()，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。
调用这个函数来制作：一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）。
"""
def make_shirt2(size,text='I love Python'):
    msg = f"The size of the T-shirt is {size}, and the text on it is {text}"
    return msg
if __name__ == '__main__':
    print(make_shirt2('XL'))
    print(make_shirt2('M'))
    print(make_shirt2(text = 'I love Python', size='L'))
print('💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗')

"""
练习8-5：城市　
编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，下面是一个例子。
Reykjavik is in Iceland.
给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
"""
def describe_city(city,country='America'):

    msg = f'{city.title()} is in {country.title()}'
    return msg

if __name__ == '__main__':
    print(describe_city('LA'))
    print(describe_city(country='America', city='MT'))
    print(describe_city('shanghai', country='China'))
print('🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶')
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f'{first_name} {last_name}'
    return full_name.title()

# musician = get_formatted_name(first_name='jimi', last_name='hendrix')
# print(musician)

if __name__ == '__main__':

    print(get_formatted_name(first_name='j0', last_name='hendrix'))
    print(get_formatted_name(first_name='j1', last_name='hendrix'))
    print(get_formatted_name(first_name='j2', last_name='hendrix'))
print('🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍🦍')
def build_person(first_name, last_name):
    """返回一个字典，其中包含我们知道的有关一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    return person


if __name__ == '__main__':
    print(build_person('j1', 'hendrix'))
    print(build_person('j2', 'hendrix'))
    print(build_person('j3', 'hendrix'))
print('🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊')

def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含我们知道的有关一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
if __name__ == '__main__':
    print(build_person('j1','hendrix',age= 40))
print('🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊')
print('🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊')
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含我们知道的有关一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

# 调用 build_person() 函数，为参数传入 'jimi', 'hendrix', 和 27，并将返回值存储在变量 musician 中
musician = build_person('jimi', 'hendrix', age=27)

# 检查当前模块是否是主程序运行。如果是，则执行其中的代码。在这里，它打印出之前构建的 musician.
if __name__ == '__main__':
    print(musician)
print('😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊')
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}" # 使用 f-string 格式化字符串
#     return full_name.title()
#
# if __name__ == '__main__':
#     while True:
#         print("\nPlease tell me your name:")
#         print("(enter 'q' at any time to quit)")
#
#         f_name = input("First name: ")
#         if f_name.lower() == 'q':
#             break
#         l_name = input("Last name: ")
#         if l_name.lower() == 'q':
#             break
#         formatted_name = get_formatted_name(f_name, l_name)
#         print(f'\nHello, {formatted_name}')
print('😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊')
"""
练习8-6：城市名　
编写一个名为city_country()的函数，
它接受城市的名称及其所属的国家。
这个函数应返回一个格式类似于下面的字符串：
"Santiago, Chile"
至少使用三个城市国家对来调用这个函数，并打印它返回的值。
"""
def city_country(city, country):

    return f'"{city.title()} , {country.title()}"'

def print_cities(cities):
    result = []
    for city in cities:
        result.append(city)
    return result

if __name__ == '__main__':
    cities = [city_country('santiago', 'chile'),
             city_country('beijing', 'china'),
             city_country('tokyo', 'japan')]
    print(print_cities(cities))

print('---------------------------------------------------------------------------------------------------------------')
"""
练习8-7：专辑　
编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。

这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。


给函数make_album()添加一个默认值为None的可选形参，以便存储专辑包含的歌曲数。
如果调用这个函数时 指定了歌曲数，就将该值添加到表示专辑的字典中。

调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
"""
# def make_album(singer,album,song=None):
#     album_info = {
#         'singer': singer.title(),
#         'album': album
#     }
#
#     if song:
#         album_info['song_count'] = song
#     return album_info
#
# def print_albums():
#     for album in albums:
#         print(f"歌手：{album['singer']}，专辑：{album['album']},歌曲数为：{album.get('song_count','0')}")
#
#
# if __name__ == '__main__':
#     albums = [make_album('zhangjie','2002年的第一场雪'),
#               make_album('liuhuan','2003年的第一场雪'),
#               make_album('daolang','2004年的第一场雪',3)]
#     # print(song1,song2,song3)
#     print_albums()
print('---------------------------------------------------------------------------------------------------------------')

"""
练习8-8：用户的专辑　
在为完成练习8-7编写的程序中，
编写一个while循环，让用户输入专辑的歌手和名称。
获取这些信息后，使用它们来调用函数make_album()并将创建的字典打印出来。
在这个while循环中，务必提供退出途径。
"""
# def make_album(singer, album, song=None):
#     album_info = {
#         'singer': singer.title(),
#         'album': album
#     }
#     if song:
#         album_info['song_count'] = song
#     return album_info
#
#
# if __name__ == '__main__':
#     while True:
#         # 获取歌手
#         print('请输入歌手和专辑，输入q退出')
#         s_singer = input('请输入歌手（输入q退出）：')
#         if s_singer == 'q':
#             print('退出程序')
#             break
#         # 获取专辑
#         a_album = input('请输入专辑（输入q退出）：')
#         if a_album == 'q':
#             print('退出程序')
#             break
#         # 获取歌曲数量
#         song_count = input('请输入歌曲数量（按回车跳过）：')
#         if song_count:
#             s_song = int(song_count)
#         else:
#             s_song = None
#
#         # 创建专辑字典
#         album_info = make_album(s_singer, a_album, song_count)
#
#
#         # print(make_album(s_singer, a_album))
#         print("\n专辑信息：")
#         print(f"歌手: {album_info['singer']}")
#         print(f"专辑: {album_info['album']}")
#         if 'song_count' in album_info:
#             print(f"歌曲数: {album_info['song_count']}")
#         else:
#             print("歌曲数: 未提供")
"""
一家为用户提交的设计制作3D打印模型的公司。需要打印的设计存储在一个列表中，打印后将移到另一个列表中
"""
# 定义一个未打印模型的函数
def print_models(unprinted_designs, complete_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"正在打印模型: {current_design}")
        complete_models.append(current_design)

# 定义一个显示已打印模型的函数
def show_complete_model(complete_models):
    print(f'\n显示已打印的模型：')
    for complete_model in complete_models:
        print(complete_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete_models = []

if __name__ == '__main__':
    print_models(unprinted_designs[:], complete_models) # unprinted_designs[:] 浅拷贝，生成列表的副本，原列表不变
    show_complete_model(complete_models)
    print(unprinted_designs)
print('🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥')
# """
# 练习8-9：消息　
# 创建一个列表，其中包含一系列简短的文本消息。
# 将该列表传递给一个名为show_messages()的函数，这个函数会打印列表中的每条文本消息。
# """
# def show_messages(messages):
#     for message in messages:
#         print(message)
#
# messages = ['Let’s go!','hello world', 'i am fine', 'thank you']
# if __name__ == '__main__':
#     show_messages(messages)
print('🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥🫥')
"""
练习8-10：发送消息　
在你为完成练习8-9而编写的程序中，编写一个名为send_messages()的函数，将每条消息都打印出来并移到一个名为sent_messages的列表中。
调用函数send_messages()，再将两个列表都打印出来，确认正确地移动了消息。
"""
# def show_messages(messages):
#     """打印列表中的所有消息。"""
#     for message in messages:
#         print(message)
#
# def send_messages(messages,sent_messages):
#     """打印每条消息，再将其移到列表 sent_messages 中。"""
#     print("\nSending all messages:")
#     while messages:
#         current_message = messages.pop()
#         print(current_message)
#         sent_messages.append(current_message)
#
#
#
# if __name__ == '__main__':
#     messages = ['Let’s go!', 'hello world', 'i am fine', 'thank you']
#     show_messages(messages) # 打印原始列表
#     sent_messages = [] # 初始化已发送消息的列表
#     send_messages(messages,sent_messages)
#     # 打印最终结果
#     print("\nFinal lists:")
#     print("Remaining messages:", messages)  # 打印剩余的消息（应该为空）
#     print("Sent messages:", sent_messages)  # 打印已发送的消息

"""
练习8-11：消息归档　
修改你为完成练习8-10而编写的程序，
在调用函数send_messages()时，向它传递消息列表的副本。
调用函数send_messages()后，将两个列表都打印出来，确认保留了原始列表中的消息。
"""
# def show_messages(messages):
#     """打印列表中的所有消息。"""
#     for message in messages:
#         print('打印列表中的所有消息:',message)
#
# def send_messages(messages, sent_messages):
#     """打印每条消息，再将其移到列表 sent_messages 中。"""
#     print('\n打印当前消息:')
#     while messages:
#         current_message = messages.pop() # pop()方法从列表末尾移除元素，并将其返回
#         print(current_message) # 打印当前消息
#         sent_messages.append(current_message) # 将当前消息添加到 sent_messages 中
#
#
# if __name__ == '__main__':
#     messages = ['Let’s go!', 'hello world', 'i am fine', 'thank you']
#     sent_messages = []  # 初始化已发送消息的列表
#     messages_copy  = messages[:] # 复制已发送消息的列表. 浅拷贝 注意：这里使用的是切片[:]，而不是直接赋值，因为直接赋值只是创建了新变量，但它们仍然指向同一个列表
#
#     show_messages(messages) # 调用show_messages()函数，打印原始列表
#     send_messages(messages_copy, sent_messages) # 调用send_messages()函数，将消息从原始列表复制到 sent_messages 列表中
#
#     print('\n打印已发送消息的列表：\n',sent_messages) # 打印已发送消息的列表
#     print('\n打印剩余消息列表\n', messages_copy)  # 打印剩余消息列表
#     print('\n打印原列表：\n', messages)  # 打印原消息的列表，验证原列表未被修改

def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    # print(user_info)
    return user_info
if __name__ == '__main__':
    # build_profile('albert', 'einstein', location='princeton', field='physics')
    print(build_profile('jack', 'ma', location='hangzhou', field='business'))

'''
练习8-12：三明治　
编写一个函数，它接受顾客要在三明治中添加的一系列食材。
这个函数只有一个形参（它收集函数调用中提供的所有食材)并打印一条消息，对顾客点的三明治进行概述。
调用这个函数三次，每次都提供不同数量的实参。
'''
def sandwich(*foods):
    print('您点的三明治有：')
    for food in foods:
        print('-',food)
if __name__ == '__main__':
    sandwich('鸡蛋', '培根', '生菜', '番茄')
    sandwich('三文鱼', '黄瓜', '洋葱')
    sandwich('牛肉', '芝士','土豆')

"""
练习8-13：用户简介　
复制前面的程序user_profile.py，在其中调用build_profile()来创建有关你的简介。
调用这个函数时，指定你的名和姓，以及三个描述你的键值对。
"""
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    # print(user_info)
    return user_info

# def my_profile(first,last,**my_info):
#     my_info['first_name'] = first
#     my_info['last_name'] = last
#     return my_info

if __name__ == '__main__':
    # build_profile('albert', 'einstein', location='princeton', field='physics')
    # print(build_profile('jack', 'ma', location='hangzhou', field='business'))
    my_profile = build_profile('wang','yuan', location='hangzhou', field='business', age=18)
    print('我的简介',my_profile)

"""
练习8-14：汽车　
编写一个函数，将一辆汽车的信息存储在字典中。

这个函数总是接受制造商和型号，还接受任意数量的关键字实参。

这样调用该函数：提供必不可少的信息，以及两个名称值对，如颜色和选装配件。
这个函数必须能够像下面这样进行调用：
car = make_car('subaru','outback',color='blue',tow_package=True)
"""
# def make_car(manufacturer,model,**car_infos):
#     car_dict ={
#         'manufacturer':manufacturer,
#         'model':model,
#     }
#     for car_info, value in car_infos.items():
#         car_dict[car_info] = value
#
#     return car_dict
# if __name__ == '__main__':
#     car = make_car('subaru','outback',color='blue',tow_package=False)
#     print(car)
def make_car(manufactures, model,**options):
    car_dict = {
        "manufactures" :manufactures.title(),
        "model" : model.title()
    }
    for key,value in options.items():
        car_dict[key] = value
    return car_dict
if __name__ == '__main__':
    car = make_car('subaru','outback',color='blue',tow_package=True)
    print(car)