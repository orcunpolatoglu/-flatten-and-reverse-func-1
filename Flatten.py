def flatten(x):
    
    for i in x:
        if isinstance(i,list): # listenin alt kumelerine bakar ve liste olmayana kadar ayıklar
            flatten(i)
        else:
            emp_list.append(i)
    
    

x= [[1,'a',['cat'],2],[[[3]],'dog'],4,5] # Verilen Liste
emp_list = [] 
flatten(x)
print(emp_list)
