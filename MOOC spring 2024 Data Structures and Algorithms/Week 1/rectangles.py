# idea is to create a data structure set 
# which contains tuple of each unit area 
# covered by a rectangle.
# therefore you couldn't input the same 
# unit area more than once as it is a set

def area(rec1, rec2, rec3):
    area_1 = (rec1[2]-rec1[0]) * (rec1[1]-rec1[3])
    area_2 = (rec2[2]-rec2[0]) * (rec2[1]-rec2[3])
    
    area_3 = (rec3[2]-rec3[0]) * (rec3[1]-rec3[3])
    print(area_1)
    return sum([area_1, area_2, area_3])

if __name__ == "__main__":
    rec1 = (37904748,847088754,800763268,371024299)
    rec2 = (-516071731,-515113038,597607792,-681585739)
    rec3 = (22452616,638287530,729050355,350766166)
    print(area(rec1,rec2,rec3)) # 16
    