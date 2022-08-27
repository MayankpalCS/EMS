from re import S
from traceback import print_tb


print('1:seniors')
print('2:juniors')
what=int(input('Enter'))
if what==1:
    class seniors:
        def __init__(self,employeelist,experince,job,salary):
            self.employeelist=employeelist
            self.experience=experince
            self.job=job
            self.salary=salary
        def showemployees(self):
            for i in self.employeelist:
                print(i)
        def showbiodata(self,name):
            for i in self.employeelist:
                if i==name:
                    print(name,'has',self.experience,'of experience','his/her job is as a',self.job,'and salary of this geek is',self.salary,'dollars')
                else:
                    pass   
        def addemployee(self,name):
            self.employeelist.append(name)
        def removeemployee(self,name):
            for i in self.employeelist:
                if i==name:
                    self.employeelist.remove(name)
            else:
                pass
        def increasesalary(self,by):
            self.salary=self.salary+by
        def decrease_salary(self,k):
            self.salary=self.salary-k
    if __name__ == '__main__':
        list4=seniors(['mayank','mansi','sun'],8,'programmer',9000)
        while True:
            print('1:Show employees')
            print('2:showbiodata')
            print('3:Add employee')
            print('4:remove employee')
            print('5:increase salary')
            print('6:Decrease salary')
            print('7:Exit')
            a=int(input('Enter'))
            if a==1:
                list4.showemployees()
            elif a==2:
                name=input('Enter the name of the employee')
                list4.showbiodata(name)
            elif a==3:
                name=input('Enter the name of the employee')
                list4.addemployee(name)
            elif a==4:
                name=input('Enter the name of the employee')
                list4.removeemployee(name)
            elif a==5:
                salr=int(input('By how much you want to increase the salary'))
                list4.increasesalary(salr)
            elif a==6:
                sa=int(input('By how much you want to decrease the salary'))
                list4.decrease_salary(sa)
            elif a==7:
                exit()
elif what==2:
    class juniors:
        def __init__(self,employeelist,experince,job,salary):
            self.employeelist=employeelist
            self.experience=experince
            self.job=job
            self.salary=salary
        def showemployees(self):
            for i in self.employeelist:
                print(i)
        def showbiodata(self,name):
            for i in self.employeelist:
                if i==name:
                    print(name,'has',self.experience,'of experience','his/her job is',self.job,'and salary of the geek is',self.salary,'dollars')
                else:
                    pass   
        def addemployee(self,name):
            self.employeelist.append(name)
        def removeemployee(self,name):
            for i in self.employeelist:
                if i==name:
                    self.employeelist.remove(name)
            else:
                pass
        def increasesalary(self,by):
            self.salary=self.salary+by
        def decrease_salary(self,k):
            self.salary=self.salary-k
    if __name__ == '__main__':
        list6=juniors(['umesh','saloni','bob'],2,'designer',450)
        while True:
            print('1:Show employees')
            print('2:showbiodata')
            print('3:Add employee')
            print('4:remove employee')
            print('5:increase salary')
            print('6:Decrease salary')
            print('7:Exit')
            a=int(input('Enter'))
            if a==1:
                list6.showemployees()
            elif a==2:
                name=input('Enter the name of the employee')
                list6.showbiodata(name)
            elif a==3:
                name=input('Enter the name of the employee')
                list6.addemployee(name)
            elif a==4:
                name=input('Enter the name of the employee')
                list6.removeemployee(name)
            elif a==5:
                salr=int(input('By how much you want to increase the salary'))
                list6.increasesalary(salr)
            elif a==6:
                sa=int(input('By how much you want to decrease the salary'))
                list6.decrease_salary(sa)
            elif a==7:
                exit()
