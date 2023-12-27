#include <stdio.h>
#include <stdlib.h>
#include<mad.h>
int main()
{


	int i = 8;
	i = i | 1 << 8;
	printf("%d", i);
	exit(0);
}
