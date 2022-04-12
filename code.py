
classes_miss_count = 0
def num_ways_classes(days,class_miss_left,consec_miss_allowed,path):
    global classes_miss_count
    
    if days==0:
        if path[-1] == 0:
            classes_miss_count += 1
        return 1
    
    if class_miss_left > 0:
        miss_path = num_ways_classes(days-1,class_miss_left-1,consec_miss_allowed,path+[0])
    else:
        miss_path = 0
        
    no_miss_path = num_ways_classes(days-1,consec_miss_allowed,consec_miss_allowed,path+[1]) 
    
    
    return miss_path + no_miss_path 



def findProbabilityAndWaysToAttendClass(n):

    attend_class = num_ways_classes(n,3,3,[])
    print("Total attend class -> "+str(attend_class))

    print("Probability to miss ceremony -> "+str(classes_miss_count)+"/"+str(attend_class))   


# findProbabilityAndWaysToAttendClass(10)  
# classes_miss_count = 0 #beacuse this is golbal valirable 
# findProbabilityAndWaysToAttendClass(5)