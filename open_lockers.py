#bool[] meinArray = new bool[100]
#doors =  [False for i in range(100)]

import array as arr

def door_output(doors):
    for i in range(0,100):
        if(doors[i] == False):
            print("{} zu".format(i))
        else:
            print("{} auf".format(i))            

def the_door_problem(doors):
    out_doors = arr.array('b',[False for i in range(100)])
    for i in range (0,100):
        out_doors[i] = doors[i]    
    for schrittweite in range(1,100):  
        for i in range(0,100,schrittweite):
            #out_doors[i] = doors[i] ? False : True #Elvis operator ?: )
            if( out_doors[i] == False):
                out_doors[i] = True
            else:
                out_doors[i] = False
    return out_doors            

def count_the_doors(doors):
    count = 0
    for i in range(0,100):
        if (doors[i] == True):
            count+=1
    return count        
                
if __name__ == "__main__":
    doors1 = arr.array('b',[False for i in range(100)])
    door_output(doors1)
    doors2 = the_door_problem(doors1)
    door_output(doors2)
    print(count_the_doors(doors2))


                                                              
