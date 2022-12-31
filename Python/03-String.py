Name = "Sunil Marella"
print("Hello "+Name)
print("Value of String :",Name)
print("length of string : ",len(Name))
print("First char of string : ",Name[0])
print("Range of char first 3 : ",Name[:3])
print("Range of char after 3rd : ",Name[3:])
print("Range of char b/w 1 to 3 : ",Name[1:3])
print("Range of char consec 2nd char: ",Name[::2])
print("Range of char consec 2nd char: ",Name[2:7:2])
print("Reverse string :", Name[::-1])

#string functions
print("Upper case : ",Name.upper())
print("Lower case : ",Name.lower())
print("Split case : ",Name.split())
print("split case l : ",Name.split('l'))

# .formate method
print('This is the string {} where curlbracket {} exist incl string value {}'.format('INSERTED','2nd INSERT',Name))
print('This is the string {0} where curlbracket {0} exist incl string value {1}'.format('INSERTED','2nd INSERT'))
print('This is the string {f} where curlbracket {b} exist incl string value {b}'.format(f='INSERTED',b='2nd INSERT'))
print('This is the string {Values} where curlbracket {b} exist incl string value {b}'.format(Values='INSERTED',b='2nd INSERT'))
Value = 100000/111
print("The rsult value {}".format(Value))
print("The rsult value {r:1.3f}".format(r=Value))
print("The rsult value {r:10.3f}".format(r=Value))

#python 3.6 onwards - fstring
Wife = "Sindhu"
Wife_Age = 32
print(f'My wife name {Wife} and {Wife_Age} years old')

#Immutability you can not change single char
Surname = "Sarella"
print(Surname[1:])
Surname = 'M'+Surname[1:]
print("New surname: ",Surname)
print(2+3)
print('2'+'3')