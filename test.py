sex={"male":147,"femle":245,"unknow":24}
for i,value in sex.items():
    print(i+"--"+str(value))

for i,key in enumerate(sex):
    print(str(i)+"=="+key)

sex=dict()

print(sex.get("123",0))
sex["123"]=sex.get("123",3)+1
print(sex["123"])