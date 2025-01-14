# 中医
class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")

# 西医
class Son(Father):
    def cure(self):
        print("使用西医方法进行治疗。。。")


# 患者
class Patient:
    def need_cure(self, doctor):
        # 患者只想西医治疗
        if isinstance(doctor, Son): # isinstance() 检查doctor是否是Son的实例
            # 通过医生的对象调用治疗方法
            doctor.cure()
        else:
            print("医生不能治疗我")


# class Patient:
#     def need_doctor(self, doctor):
#         if issubclass(doctor.__class__, Father): # doctor.__class__判断doctor对象对应的类的类名
#             doctor.cure()
#         else:
#             print("此大夫医疗方法不适用病人。。。")



# 获取医生的对象
f_doctor = Father()
s_doctor = Son()

# 获取患者的对象
p = Patient()

p.need_cure(f_doctor ) #
p.need_cure(s_doctor)

# # 检查对象的类型
# # 检测f_doctor 是Father的实例吗？
# print(isinstance(f_doctor, Father))
# print(isinstance(s_doctor, Father))


# # 检查是否是某个类型的子类
# print(issubclass(Son, Father))

