#def divisible_by_3 (num):
#    if num % 3 == 0:
#        return 'divisible_by_3', num
#    elif num % 3 != 0:
#        return "not divisible by 3", num
     
#ans = divisible_by_3(7)  
#print(ans)   

        
#def latDep (coord1,coord2):
#    latN = coord2[1]-coord1[1]
#    latE = coord2[0]-coord1[0]
#    return latN,latE
   
#transverse = latDep ((5,6),(3,8))
#print(transverse)


    
# when using distance and bearing

from math import sin,cos, radians, atan2,degrees,sqrt
from pandas import read_csv

#def LatDep (dist,bear):
#    to_radians = radians(bear)
#    lat = dist * cos(to_radians)
#    Dep = dist * sin(to_radians)
 #   return lat,Dep   

#ans = LatDep (25.66,265.7)    
#print(ans)

def latDep(E,N):
    zipped = list(zip(E,N))
    Lat = []
    Dep = []
    for coord in enumerate(zipped):
        index_no = coord[0]
        item = coord[1]
        if index_no+1 != len(zipped):
            lat = zipped[index_no +1][1]- item[1]
            dep = zipped[index_no +1 ][0] - item[0]
            Lat.append(lat)
            Dep.append(dep)
        else:
            print("we are at the last item")
        
    return Lat,Dep        
        
N = [2,5,10,15,20]   
E = [3,9,15,20,10] 
d= latDep(E,N)
  


# def latDep(E,N):
#     zipped = list(zip(E,N))
#     Lat = []
#     Dep = []
#     for coord in enumerate(zipped):
#         index_no = coord[0]
#         item = coord[1]
#         try:
#             lat = zipped[index_no +1][1]- item[1]
#             dep = zipped[index_no +1 ][0] - item[0]
#             Lat.append(lat)
#             Dep.append(dep)
#         except BaseException:
#             print("we are at the last item")
        
        
#     return Lat,Dep        
        
# N = [2,5,10,15,20]   
# E = [3,9,15,20,10] 
# data = latDep(E,N)

# print(data)


## Finding bearings
# def Bearing (lat,Dep):
#     zipped = list(zip(lat,Dep))
#     Bear = []
#     for data in zipped:
#         bearing = atan2(data[1],data[0])
#         bearing_degrees = degrees (bearing)
#         Bear.append(bearing_degrees)
#     return Bear    

# lat = d[0]
# dep = d[1]
# ans = Bearing (lat,dep)
# print(ans)



## for finding distances

# def distance (lat,Dep):
#     zipped = list(zip(lat,Dep))
#     Dist= []
#     for data in zipped:
#         dist = sqrt (data[1]**2 + data[0]**2)
#         Dist.append(dist)
#     return Dist   

# lat = d[0]
# dep = d[1]
# ans = distance (lat,dep)
# print(ans)



### Finding northings of other points using A = (2,3)


def  Northings (lat):
    initial_northings = 3
    new_northings = [initial_northings]
    for data in lat:
        northings = initial_northings + data
        new_northings.append (northings)
        initial_northings = northings
    return new_northings
        
  
lat = d[1]   
n=Northings(lat) 
print(n)
    
        






# def  Eastings (dep):
#     initial_eastings = 2
#     new_eastings = [initial_eastings]
#     for data in dep:
#         eastings = initial_eastings + data
#         new_eastings.append (eastings)
#         initial_eastings = eastings
#     return new_eastings
        
  
# dep = d[0]   
# e=Eastings(dep)     
# print(e)



def Area (N,E):
    N.append(N[0])
    E.append(E[0])
    grouped_N = N
    grouped_E = E
    
    N_extract = grouped_N[0:-1]
    
    E_extract = grouped_E[1:]
    
    
    zipped = zip(N_extract,E_extract)
    result = 0
    for data in zipped:
        
        add = data[0]*data[1]
        result = result + add
        

    print(result)
    
    N_extract1 = grouped_N[1:]
    E_extract1 = grouped_E[0:-1]
    
    zipped1 = zip(N_extract1,E_extract1)

    result2 = 0
    for data in zipped1:
        add = data[0]*data[1]
        result2 = result2 + add
  
        
    area = abs((result - result2)/2)
  
    return area

def readdata(filepath):
    data = read_csv(filepath)
    return list(data.N),list(data.E)
    

N = readdata(r"C:\Users\Prof. Nii Darko\Desktop\trial.csv")[0]
E = readdata(r"C:\Users\Prof. Nii Darko\Desktop\trial.csv")[1]
ans = Area(N,E)
print(ans)



        
        
    









    
  
    
  
    
  
    
  









        
    
        