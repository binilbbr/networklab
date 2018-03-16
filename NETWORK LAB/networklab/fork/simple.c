#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<string.h>
#include<sys/wait.h> 
int main()
{
    pid_t p;
    p = fork();
    if (p < 0)
    {
        fprintf(stderr, "fork Failed" );
        return 1;
    }
    else if (p > 0)
    {
        
        printf("parent  %d\n",p);
       
    }
    else
    {
        printf("child  %d\n",p);
        exit(0);
    }
}
