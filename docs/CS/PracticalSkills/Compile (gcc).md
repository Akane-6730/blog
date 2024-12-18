---
counter:
---
## 编译过程 （Compilation Process）
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/77RYpbmcEeeZcg6zWBk5EA_a1a84fd101dc9181bf4fb6586f9055f3_Compilation-Process.png?expiry=1732924800000&hmac=YHnVv1hTFAsjYmYRR5Th4NV_KwM0DUotfB6jKCSzfZQ)
### **编译过程中的各个阶段 (Stages in the Compilation Process)**

- **浅蓝色框**：表示 **用户编写的代码** (Your written code)
    
    - 这是我们在**源文件中编写的 C 代码**，通常是 `.c` 文件。

- **浅绿色框**：表示 **C 的内置部分** (Built-in parts of C)
    
    - 这包括 **C 标准库**及编译器为我们提供的其他支持部分。

- **橙色云**：表示 **编译过程的步骤** (Steps in the process)
    
    - 每个步骤都是一个独立的程序，通常由 `gcc` 调用。
    - 这些步骤包括**预处理、编译、汇编**等。

- **白色框**：表示 **`gcc` 生成的中间文件** (Intermediate files generated by gcc)
    
    - 这些文件用于将信息从一个阶段传递到下一个阶段，如 `.o` 文件。

- **深蓝色框**：表示 **最终的可执行文件** (Final executable file)
    

## 编译器选项 (_compiler-options_)

### _-o_ 选项：

- 指定输出文件名，而不是默认的 _a.out_
- *-o* 后面必须紧跟输出文件名。
- 源文件的位置不需要特别指定顺序。
!!! note "example"
	```Make
	gcc -o myProgram myProgram.c
	gcc myProgram.c -o myProgram
	```
	
	- 以上两种写法等价
	- 将 _myProgram.c_ 编译为名为 _myProgram_ 的程序，而不是默认的 _a.out_
	
### _-std=gnu99_ 选项：

- 使用带有 GNU 扩展的 C99 标准

### _-Wall_ 和 _-Werror_ 选项：

- _-Wall_：启用所有常见警告 (**Warnings All**)
	* 虽然名字叫 "All"，但它实际上并不会开启所有警告，而是开启一组常见和实用的警告。
- _-Werror_：将所有警告视为错误，阻止编译 (**Warnings as Errors**)

### 推荐警告选项：
!!! danger ""
	- _-Wall -Wsign-compare -Wwrite-strings -Wtype-limits -Werror_
#### *-Wsign-compare*：
- **缩写含义**：*W* 表示 **Warning**，*sign-compare* 表示 **Signed-Unsigned Comparison**。  
- **完整解释**：Warning about **sign** during comparisons.
- **作用**：当将带符号的值（如 *int*）与无符号值（如 *unsigned int*）进行比较时，可能会导致非预期行为。*-Wsign-compare* 会对这种潜在问题发出警告。

??? note "example"
	```c
	int x = -1;
	unsigned int y = 10;
	if (x < y) { // 这里 x 会被隐式转换为 unsigned，导致潜在错误 
		printf("Comparison is true.\n");
	}
	```
	
#### *-Wwrite-strings*：
- **缩写含义**：*W* 表示 **Warning**，*write-strings* 表示 **Writable Strings**。
- **完整解释**：Warning about **writing to string literals**
- **作用**：  
	编译器会将字符串常量视为 _const char\*_ 类型，警告代码中存在的尝试将字符串常量赋值给普通的 _char\*_ 类型变量或直接修改字符串常量的行为。

??? note "example"
	```c 
	char *str = "Hello"; 
	str[0] = 'h'; // 非法操作，修改了字符串常量
	```
	
	- 会警告 `str` 的类型从 `const char*` 到 `char*` 的隐式转换。
#### *-Wtype-limits*：

- **含义**：Warning about **values exceeding the limits of a type** (类型限制问题)。
- **作用**：  
    当代码中比较的值永远为真或假时（例如，因超出类型的取值范围导致恒定结果）发出警告。

??? note "example" 
	```c 
	unsigned int x = 5; 
	if (x >= 0) { // 恒为 true，因为无符号整数的范围从 0 开始 
		printf("This condition is always true.\n"); 
	}
	```
	
	- 无符号整数永远不小于 0，而将它与负数进行比较是没有意义的。

### *-pedantic* 选项：
- *-pedantic* 是一种比 *-Wall* 更严格的设置，它会严格要求代码符合标准，如果不符合标准，就会产生警告或错误。
### _-fsanitize=address_ 选项：

- 启用 AddressSanitizer，检测内存错误
!!! danger "常见的内存错误"
	- **缓冲区溢出**：访问数组边界外的内存。
	- **使用后释放（Use-After-Free）**：在内存释放后仍然访问该内存。
	- **堆内存泄漏**：内存分配后未释放，导致内存泄漏。
	- **堆栈溢出**：访问栈上的内存越界。
	- **内存访问越界**：访问不属于程序的内存区域。

- 注意：该选项与 *valgrind* 不兼容，需要分开使用。

