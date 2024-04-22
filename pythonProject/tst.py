items = ['$123.45', '434.23$', '567.89']


class Basetest():
    def testMethod(self):
        print("menthod1")

class ChildClass(Basetest):
    def testMethod(self):
        print("method2")
s = "Sony12India567Pvt2ltd" # eg.12+567+2

var3 =''
s_modified = s.lower()
var1 = "abcdefghijklmnopqrstuvwxyz"
for i in s_modified:
    if i not in var1:
        var3 +=i
print(var3)
print(int(var3[:2])+int(var3[2:5])+int(var3[5:]))