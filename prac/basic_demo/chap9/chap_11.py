from chap9_8 import Admin

# 创建Admin的实例
main  = Admin('Wang', 'Yuan', 18)
p_privileges = ['can add post2', 'can delete post2', 'can ban user2']
main.privileges.privileges = p_privileges # 给管理员添加权限
main.privileges.show_privileges() # 展示新添加的管理员权限
