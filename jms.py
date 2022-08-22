from traceback import print_tb


print('1:seniors')
print('2:juniors')
what=int(input('Enter'))
if what==1:
    class seniors:
        def __init__(self,employeelist,experince,job):
            self.employeelist=employeelist
            self.experience=experince
            self.job=job
        def showemployees(self):
            for i in self.employeelist:
                print(i)
        def showbiodata(self,name):
            for i in self.employeelist:
                if i==name:
                    print(name,'has',self.experience,'of experience','his/her job is as a',self.job)
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
    if __name__ == '__main__':
        list4=seniors(['mayank','mansi','sun'],8,'programmer')
        while True:
            print('1:Show employees')
            print('2:showbiodata')
            print('3:Add employee')
            print('4:remove employee')
            print('5:Exit')
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
                exit()
elif what==2:
    class juniors:
        def __init__(self,employeelist,experince,job):
            self.employeelist=employeelist
            self.experience=experince
            self.job=job
        def showemployees(self):
            for i in self.employeelist:
                print(i)
        def showbiodata(self,name):
            for i in self.employeelist:
                if i==name:
                    print(name,'has',self.experience,'of experience','his/her job is',self.job)
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
    if __name__ == '__main__':
        list6=juniors(['umesh','saloni','bob'],2,'designer')
        while True:
            print('1:Show employees')
            print('2:showbiodata')
            print('3:Add employee')
            print('4:remove employee')
            print('5:Exit')
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
                exit()
