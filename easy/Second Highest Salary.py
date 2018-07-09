# 查询第二高的薪水
#从小于最高工资中找最高的工资，找出来就是第二高的工资
sql = '''select max(Salary) as SecondHighestSalary from Employee where Salary<(select max(Salary) from Employee)'''

# 如果不为空返回第一个参数，为空返回null，降序后limit是关键，从第一条开始取，取一条，就是第二高工资
'''select IFNULL((select Distinct Salary from Employee order by Salary DESC limit 1,1),null) as SecondHighestSalary'''