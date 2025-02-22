class Student:
    """
    1、定义学生类 属性：学生名称、成绩{}科目：分数
    2、方法
        添加成绩：add_score()为学生添加成绩，如果分数无效(小于0或大于100)抛出valueError
        计算平均成绩：average_score()
    """
    def __init__(self, name):
        self.name = name
        self.scores={}  # {科目：分数}
    # def to_dict(self):
    #     return {"name": self.name, "score":self.scores['subject']}
    def __str__(self):
        return f"{self.name},{self.scores}"

    def add_score(self,subject,score):
        if score > 100 or score < 0:
            return 'ValueError("分数无效，分数必须小于0或大于100")'

        if subject not in self.scores:
            self.scores[subject]=score
        else:
            self.scores[subject] = score
        print(f'学生{self.name}，科目{subject}:分数{score} 添加成功')
        return '科目、分数添加成功'
    def average_score(self):
        # 计算学生的平均成绩
        total_score = 0
        for score in self.scores.values():
            total_score += score
        average_score = total_score / len(self.scores)
        print(f'学生{self.name}平均成绩为： {average_score}')
        return "平均成绩计算成功"

class School:
    """
    1、属性：存储所有学生的字典
    2、方法：
        向学校中添加学生：add_student()
        根据学生名称获取学生：get_student()
        计算全班学生的平均成绩：class_average()
    """
    def __init__(self):
        self.students = {}  # 键 {学生名称：学生对象{学生名称：{科目：分数}}}
    # def to_dict(self):
    #     return {'name':self.students,"subject":self.students['subject'],'score':self.students['score']}
    def add_student(self, student): # student 学生对象
        if student.name not in self.students:
            self.students[student.name] = student
            print(f'学生{student.name}添加成功')
            return '学生添加成功'
        else:
            print(f'学生{student.name}已存在')
            return '学生已存在'
    def get_student(self,name):
        # 根据学生姓名获取学生对象
        if name in self.students:
            # print(name)
            for stu_name in self.students.keys():
                if stu_name == name:
                    print(f'学生{name}的信息为：{self.students[name]}')
            return '学生信息获取成功'
    def class_average(self,subject):
        # 获取全班学生各科的平均成绩
        # 每个学生每科的总成绩/总人数
        total_score = 0
        count = 0  # 记录有多少学生有该门成绩
        for student in self.students.values():  # {学生名称：{科目：分数}}
            # print(type(student))
            if subject in student.scores:
                total_score += student.scores[subject]
                count += 1

        # print(total_score)
        if count == 0:
            print(f'没有学生有{subject}成绩')
            return '全班学生都没有该科成绩'

        average_score = total_score / count
        print(f"科目{subject}",'平均分',f'{average_score}')
        return '全班学生各科平均分计算成功'


        #     print(f'{subject} 的 全班平均分为{average_score}')
        #     return '全班学生各科平均分计算成功'

if __name__ == '__main__':
    stu= Student('zhansan',)
    stu1= Student('lisi',)
    stu.add_score('math',1)
    stu.add_score('chinese',1)
    stu.add_score('english',1)
    stu1.add_score('math',3)
    stu1.add_score('chinese',4)
    stu1.add_score('english',5)

    stu.average_score()
    print('----------------------------------')
    school = School()
    school.add_student(stu)
    school.add_student(stu1)
    school.get_student('zhansan')
    school.class_average('math')
