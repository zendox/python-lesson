#create a dict, add datas like , roll no ,name ,marks,along with gender,
# now i want to print all the names and marks whose gender is male ,how would you do that ?
d = {'rollno':[1,2,3,4], 'name':['ram','sita','hari','rama'],'gender':['male','female','male','female']}
tmp=[]
for i in range(len(d['name'])):
    if d['gender'][i]=="male":
        print(d['name'][i])



