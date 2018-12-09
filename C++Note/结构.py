一、逻辑结构

	条件结构if:
	if (condition) {
		//statements
	}
	else if(condition) {
		//statements
	}
	else {
		//statements
	}

	条件结构switch：
	switch (expression) {
	case value1:
		//statements
	break;	//break sentence is necessary

	case value2:
		//statements
	break;
	...
	case valueN:
		//statements
	break;

	default:
		//statements
	}


	循环结构while:
	while (condition){
		//statements
	}

	循环结构for:
	for (init; condition; increment){	
		//e.g.(int x = 1; x < 10; x++)
		//statements
	}

	循环结构do:
	do {
		//statements
	}while (condition);


--------------------------------------------------------------------


二、数据结构

2.1 变量类型&储存空间
	普通类:
	char short int long 
	1	 2	   4   4
	short int  long int  long long 
	2          4         8
	float double  long float  long double
	4     8       8           8
	bool
	1

	结构类:
	array struct union 

	指针类:
	pointer
	4

	库类:
	string(<string>)

2.2 变量修饰符:
	signed unsigned
	short long
	const

2.3 变量申明和使用
	零、数值
	申明1 int var;
	申明2 long int var;


	一、array
	申明1 int array[length];
	申明2 int array[length] = {1,2,3,4,5};
	赋值 array[index] = 5;
	长度 sizeof array / sizeof int
	历遍 for循环

	二、struct & union
	定义
	struct struct_name
	{
		char name[20];
		float volume;
		double price;
	};
	申明 struct_name var;
	调用 var.name

	三、pointer
	3.1 普通情况
	申明1 int * pointer;
	申明2 int * pointer = &var;
	申明3 int * pointer = new int;
	申请内存 pointer = new int;
	归还空间 delete pointer
	赋值1 pointer = &var;
	赋值2 pointer = (int *) 0xB8000000;
	调用指向的值 *pointer;


	3.2 dynamic array
	申请内存 int * pointer = new int [10];
	归还内存 delete [] pointer;
	赋值1 pointer = array;
	赋值2 pointer += 1;
	赋值3 pointer = &array[index];
	调用指向的值1 pointer[index];
	调用指向的值2 *(pointer+index);
	技巧 : 	动态字符串
	ps = new char[strlen(animal) + 1]; // get new storage
	strcpy(ps, animal); // copy string to new storage

	3.3 struct
	调用 pointer->name