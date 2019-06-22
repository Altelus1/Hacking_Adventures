#include <stdio.h>                                                                                                         
#include <stdint.h>                                                                                                        
#include <stdlib.h>                                                                                                        
#include <time.h>                                                                                                          
#include <unistd.h>                                                                                                        
#include <limits.h>                                                                                                        
                                                                                                                           
int main(){                                                                                                                
                                                                                                                           
        long seed;                                                                                                         
        scanf("%ld", &seed);                                                                                               
        srand(seed);                                                                                                       
                                                                                                                           
        //long choice;                                                                                                     
        //scanf("%ld", &choice);                                                                                           
        int counter = 0;                                                                                                   
        while(counter < 20){                                                                                               
                printf("result is : %ld\n",((long)rand()%36)+1);                                                           
                counter += 1;                                                                                              
        }                                                                                                                  
}      

/*
Generates the first 20 numbers produce by
rand() with the the seed that is the cash
given by the problem. 1,3,5,7th etc.. output 
are the numbers the roulette will give.
*/
