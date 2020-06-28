
#   *                                                                                                                                      
#   * *                                                                                                                                    
#   * * *                                                                                                                                  
#   * * * *                                                                                                                                
#   * * * * *                                                                                                                              
#   * * * * * *                                                                                                                            
#   * * * * * * *  


def stars(number,i):
    
    if i == number :
        return 0
    else:
        for j in range(i):
            print('*', end = " ")
        print(' ')
    return stars(number,i+1)

stars(8,0)

#    * * * * * * * *                                                                                                                        
#    * * * * * * *                                                                                                                          
#    * * * * * *                                                                                                                            
#    * * * * *                                                                                                                              
#    * * * *                                                                                                                                
#    * * *                                                                                                                                  
#    * *                                                                                                                                    
#    *

def stars(number):
    
    if number == 0:
        return 0
    else:
        for j in range(number):
            print('*', end = " ")
        print(' ')
    return stars(number-1)

stars(8)

