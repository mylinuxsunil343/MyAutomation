mydict = {'Name':'Test','Surname':'Test1','Age':36,'Salary':6500.20}
print("My name is :",mydict['Name'])
print("My Salary :",mydict['Salary'])

mydict['wife'] = "Testy"
print(mydict)

mydict['Name'] = "Test Tost"
print(mydict)

print(mydict.keys())
print(mydict.values())
print(mydict.items())

price_lookup= {'apple':2.99,'banana':1.99,'orange':1.49}
print("Price of Orange : ",price_lookup['orange'])

d = {'k1':123,'k2':[0,'a',2],'k3':{'Orange':1.49,'apple':1.99}}
print(d['k1'])
print("Dict list : ",d['k2'])
print("Dict list value : ",d['k2'][2])
print("Dict list value : ",d['k2'][1].upper())

print("Dict dict : ",d['k3'])
print("Dict dict value :",d['k3']['apple'])
