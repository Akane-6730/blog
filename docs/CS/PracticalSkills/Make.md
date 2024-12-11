# Fancier Make Options
---

## 基本概念

- **Makefile 的输入**  
    Makefile 包含一条或多条规则，这些规则规定如何通过前置条件（prerequisites）生成目标文件（target）。
    - **规则格式**：`目标文件: 前置条件`  
        之后用 TAB 缩进指定命令（不能使用空格）。
    - **默认目标**：如果不指定目标，`make` 会构建 Makefile 中的第一个目标。

---

## 工作原理

- **更新检查**：  
    `make` 首先检查每个前置条件是否更新：
    - 若前置条件不存在或需要更新，`make` 会优先构建前置条件。
    - 如果目标文件不存在，或者前置条件的修改时间比目标文件更新，则会重新构建目标文件。

!!! info "示例: 检查和重建目标文件" 
	
	```make
	myProgram: oneFile.o anotherFile.o 
        gcc -o myProgram oneFile.o anotherFile.o
	
	oneFile.o: oneFile.c oneHeader.h someHeader.h
		gcc -std=gnu99 -pedantic -Wall -c oneFile.c
	
	anotherFile.o: anotherFile.c anotherHeader.h someHeader.h
		gcc -std=gnu99 -pedantic -Wall -c anotherFile.c
	```
### 核心说明：
1. 在这个 `Makefile` 中，有三个**目标**：`myProgram`、`oneFile.o` 和 `anotherFile.o`。
2. 如果只键入 `make` 命令，那么 `make` 会**尝试（重新）编译默认目标** `myProgram`，因为它是文件中的第一个目标。
3. `myProgram` 依赖于 `oneFile.o` 和 `anotherFile.o`，因此 `make` 首先会检查这两个目标是否需要重建：
	   - 对于 `oneFile.o`，它依赖于 `oneFile.c` 和两个头文件（`oneHeader.h` 和 `someHeader.h`）。
	   - 如果 `oneFile.c` 或依赖的 `.h` 文件比 `oneFile.o` 更新，则会重新编译 `oneFile.o`。否则，直接跳过。
4. 完成 `oneFile.o` 的检查后，`make` 处理 `anotherFile.o` 的逻辑类似。

### 文件不存在时的行为：
- 如果依赖文件（例如 `oneHeader.h`）**不存在**，`make` 会报错并终止：
  
  ```bash
  make: *** No rule to make target 'oneHeader.h', needed by 'oneFile.o'.  Stop.
  ```

### 文件已存在时的行为：
- 假设所有依赖文件都存在：
  - 如果目标文件（例如 `oneFile.o`）的**时间戳比依赖文件旧**，`make` 将运行指定的 `gcc` 命令来重建它。
  - 如果目标文件已经是最新，`make` 会跳过构建，并提示：

    ```bash
    make: 'myProgram' is up to date.
    ```

### 完整构建流程：
1. 处理完 `oneFile.o` 后，`make` 检查并处理 `anotherFile.o`。
2. 两个对象文件检查完成后，`make` 会检查是否需要重新生成最终目标 `myProgram`：
   - 如果 `myProgram` 文件不存在，或者其依赖的对象文件比它新，`make` 会运行联编命令（`gcc -o myProgram oneFile.o anotherFile.o`）。
   - 否则，构建结束，不进行任何操作。



---

## 优化：变量

- 使用变量减少重复，方便维护。例如定义**编译标志**：
    
    ```make
    CFLAGS=-std=gnu99 -pedantic -Wall
    myProgram: oneFile.o anotherFile.o
        gcc -o myProgram oneFile.o anotherFile.o
    
    oneFile.o: oneFile.c oneHeader.h someHeader.h
        gcc $(CFLAGS) -c oneFile.c

	anotherFile.o: anotherFile.c anotherHeader.h someHeader.h
	    gcc $(CFLAGS) -c anotherFile.c
    ```
    
- 变量引用：`$(变量名)`  
    **注意**：修改 Makefile 并不会自动更新目标文件。可用 `make clean` 后重新构建。
    

---

## 特殊目标：清理（clean）

- **清理目标**：用于删除构建产物或清理目录。
    
    ```make
    .PHONY: clean
    clean:
        rm -f myProgram *.o *.c~ *.h~
    ```
    
    - `.PHONY` 声明：标记 clean为伪目标，使make不会尝试生成名为 clean的文件。

---

## 泛型规则

- 泛型规则：减少重复代码。使用 `%` 表示通配符：
    
    ```make
    %.o: %.c
        gcc $(CFLAGS) -c $<
    ```
    
    - `$<`：第一个前置条件文件。
    - `$@`：当前目标文件。

!!! danger "警告: 忽略头文件依赖" 
	上述规则无法跟踪 `.h` 文件的变化。可以手动添加依赖信息： `make oneFile.o: oneHeader.h someHeader.h`

---

## 自动生成依赖项

- 工具 `makedepend` 可自动生成 `.c` 文件的依赖项，并追加到 Makefile 末尾：
    
    ```make
    depend:
        makedepend *.c
    ```
    
    - 推荐在构建前运行 `make depend` 更新依赖信息。

---

## 内置规则与函数

- **内置规则**：例如，`.o` 文件的默认规则：
    
    ```make
    %.o: %.c
        $(CC) $(CFLAGS) -c -o $@ $<
    ```
    
- **内置函数**：  
    自动化管理源文件与对象文件：
    
    ```make
    SRCS = $(wildcard *.c)
    OBJS = $(patsubst %.c, %.o, $(SRCS))
    ```
    

---

## 复杂项目的优化

- 支持同时构建调试版和优化版：
    
    ```make
    CC = gcc
    CFLAGS = -std=gnu99 -pedantic -Wall -O3
    DBGFLAGS = -std=gnu99 -pedantic -Wall -ggdb3 -DDEBUG
    SRCS = $(wildcard *.c)
    OBJS = $(patsubst %.c,%.o,$(SRCS))
    DBGOBJS = $(patsubst %.c,%.dbg.o,$(SRCS))
    
    all: myProgram myProgram-debug
    myProgram: $(OBJS)
        gcc -o $@ $(OBJS)
    ```
    

---

## 并行构建

- 使用 `-j` 指定并行任务数（适用于多核 CPU）：
    
    ```make
    make -j8
    ```
    
- 默认 `-j` 最大化并行任务。
    

---

## 学习资料

-  [GNU Make 文档](https://www.gnu.org/software/make/manual/)。