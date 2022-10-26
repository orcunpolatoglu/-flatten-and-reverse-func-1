
def flatten(x):
    
    for i in x:
        if isinstance(i,list): # listenin alt kumelerine bakar ve liste olmayana kadar ayıklar
            flatten(i)
        else:
            emp_list.append(i)
    #print(emp_list)


def reverse_list(x):
     
    for i in range(int(len(x)/2)):
        temp = x[i]
        x[i] = x[len(x)-(i+1)]
        x[len(x)-(i+1)] = temp
        
    counter = 0
    for i in x:
        if isinstance(i,list):
             
            for a in range(int(len(i)/2)):
                temp = x[counter][a]
                x[counter][a] = x[counter][len(i)-(a+1)]
                x[counter][len(i)-(a+1)] = temp
                counter +=1
    print(x)   

x= [[1,'a',['cat'],2],[[[3]],'dog'],4,5] # Verilen Liste
y = [[1, 2], [3, 4], [5, 6, 7]] # Verilen Liste
emp_list = []
flatten(x)
print(emp_list)

reverse_list(y)




