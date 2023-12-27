#include <iostream>
#include <string>
using namespace std;
int g = 2;
int h = 12;
int o = 15;
#define day 7
int main()
{	
	char ch = 'a';
	char dh = 'A';
	cout << "a的anscii码: " << (int)ch << endl;
	cout << "A的anscii码: " << (int)dh << endl;
	int a = 0;
	cout << "请给整型变量a赋值: " << endl;
	cin >> a;
	cout << "整型变量a = " << a << endl;
	cout << "char的内存空间: " << sizeof(char) << endl;
	cout << "short的内存空间: " << sizeof(short) << endl;
	cout << "int的内存空间: " << sizeof(int) << endl;
	cout << "long的内存空间: " << sizeof(long) << endl;
	cout << "long long的内存空间: " << sizeof(long long) << endl;
	cout << "float的内存空间: " << sizeof(float) << endl;
	cout << "double的内存空间: " << sizeof(double) << endl;
	cout << "hello C++" << endl;
	cout << "a= " << a <<endl;
 	cout << "一周总共有: "<< day << "天" << endl;
 	const int month = 12;
 	cout << "一年里总共有 " << month << " 个月份" << endl;
 	bool flag = true;
 	cout << flag << endl;
 	cout << "bool所占内存空间:"<<sizeof(bool) << endl;
 	string	str = "hello world";
 	cout << "请给字符串 str赋值: " << endl;
 	cin >> str ;
 	a = 0;
 	while(a<10)
 	{
 	cout << a <<endl;
 	a++;
 	}
 	a = 0 ;
 	int b = 0 ,c = 0,num =100;
 	do
 	{
 		a = num/100;
 		b = num/10%10;
 		c = num%10;
 		if(a*a*a+b*b*b+c*c*c==num)
 		{
 		cout << num << endl;
 		}
 		num++;
 	}while(num<1000);
 	for(num =1;num <101;num ++)
 	{
 		if(num%7 == 0 || num/10 ==7 || num%10 == 7)
 		{cout << "敲桌子"  << endl;
 		}
 		else
 		{cout << num <<endl;
 		}
 	}
 	
 	int arr[5] = {1,2,3,4,5};
 	cout << sizeof(arr) <<endl;
 	cout << arr << endl;
 	cout << (long)arr <<endl;
 	int arr1[5] = {100,200,300,400,320};
	int max = 0;
 	for(int i=0;i<5;i++)
 	{
 		if(arr1[i]>max)
 		{
 		max = arr1[i];
 		}
 	}
 	cout << max <<endl;
 	
 	a = 100;
 	int *p = &a;
 	cout << "sizeof (int *)=" << sizeof(int *) << endl;
 	int d = 1;
 	int e = 1;
 	int f = 1;
 	cout << "d在内存里的地址: " << (long)&d <<endl;
 	cout << "e在内存里的地址: " << (long)&e <<endl;
 	cout << "f在内存里的地址: " << (long)&f <<endl;
 	cout << "g在内存里的地址: " << (long)&g <<endl;
 	cout << "h在内存里的地址: " << (long)&h <<endl;
 	cout << "o在内存里的地址: " << (long)&o <<endl;
 	int *q =new int(10);
 	cout << "10在堆区的地址: " << (long)p <<endl;
 	cout << *q <<endl;
 	cout << *q <<endl;
 	cout << *q <<endl;
 	delete q;
 	cout << *q <<endl;
  	return 0;

}




