from random import choice

lst = ["1","2","3","4","5","6","7","8","9","10",'a','b','c','d','e']

def get_winning_ticket():
    """获取中奖的彩票号码"""
    win_tickets = []
    while len(win_tickets) < 4:
        ticket = choice(lst)
        if ticket not in win_tickets:
            win_tickets.append(ticket)
    return win_tickets

def select_ticket():
    """随机选择中奖号码"""
    select_tickets = []
    while len(select_tickets) < 4:
        ticket = choice(lst)
        if ticket not in select_tickets:
            select_tickets.append(ticket)
    return select_tickets

def sequence_ticket():
    win_tickets = get_winning_ticket() # 调用 get_winning_ticket() 函数，并将其返回的结果赋值给 win_tickets 变量。
    count = 0 # 循环次数
    while True:
        select_tickets =  select_ticket() # 调用 select_ticket() 函数，并将其返回的结果赋值给 select_tickets 变量
        count += 4
        print(f'目前尝试了{count}次，选择的号码为：{select_tickets}')
        
        if select_tickets == win_tickets:
            print(f"中奖号码：{win_tickets}")
            print(f"选票：{select_tickets}")
            print(f"经过 {count} 次尝试，终于中奖了！")
            break

sequence_ticket()




