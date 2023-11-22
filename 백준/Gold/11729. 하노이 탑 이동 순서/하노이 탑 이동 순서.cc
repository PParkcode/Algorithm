#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>


void honoii(int start, int mid, int end,int num);
int count(int num);

int main(void)
{
	int num;
	
	scanf("%d", &num);
	printf("%d\n", count(num));
	honoii(1,2,3,num);
	

}
int count(int num)
{
	int result = 1;
	for (int i = 0; i < num; i++)
	{
		result *=2;
	}
	return result - 1;
}
void honoii(int start, int mid, int end, int num)
{
	if (num == 1)
	{
		printf("%d %d\n",start, end);
	}
	else
	{
		honoii(start, end, mid, num - 1);
		printf("%d %d\n", start, end);
		honoii(mid, start, end, num - 1);
	}
	

	
}