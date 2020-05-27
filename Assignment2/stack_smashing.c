#include <stdio.h>
#include<string.h>

void function(char *str){
    char buff[16];
    strcpy(buff, str);
}

int main()
{
    char str[256];
    int i;
    for(i = 0; i < 255; i++) {
        str[i] = 'c';
    }
    function(str);

    return 0;
}
