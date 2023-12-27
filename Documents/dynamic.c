#include <stdio.h>
#include <dlfcn.h>

int main(int argc,char *argv[])
{
	void *handle = dlopen(argv[1], RTLD_NOW);
	if (handle == NULL)
	{
		printf("load faied...%s\n",dlerror());
		return -1;
	}
	printf("load success...\n");
	dlclose(handle);
	return 0;

}
