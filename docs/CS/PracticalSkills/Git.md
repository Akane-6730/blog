

## Git 基础概念

### **什么是 Git**

- **分布式版本控制系统（Distributed Version Control System, DVCS）**
    - **分布式**：无需联网即可使用，所有修改记录都存储在本地。
    - **版本控制**：记录、管理、回溯文件修改历史。

---

### **Git 安装**

- \*Unix：包管理器直接装

	- apt install git / brew install git / ...

- Windows：

	- https://git-scm.com/download/win
	- 内带 Git Bash：
		- 一个基于 MinGW 的类 Linux shell 环境
		- 包含了很多常用的但 cmd/powershell 缺少（或用法差别很大）的命令
    - 注意看安装时的选项，其中包括了一些使用范围的配置
        - 注意环境变量

---
### **Git 模型演示图**
![](Git-1.png)

---
### Git 的数据模型

#### **对象和内存寻址**

- **对象类型**：
    - Blob（文件数据）
    - Tree（目录结构）
	    - 其中记录了该 Tree 中引用的 **Blob 对象**（文件内容）和子目录的 **Tree 对象**
    - Commit（提交）
	    - 指向一个**顶级 Tree 对象(Snapshot)**，同时包含**元数据**和**父提交**的**引用**。
??? note "数据模型的伪代码表示"
	```txt
	// 文件就是一组数据
	type blob = array<byte>
	
	// 一个包含文件和目录的目录
	type tree = map<string, tree | blob>
	
	// 每个提交都包含一个父辈，元数据和顶层树
	type commit = struct {
	    parents: array<commit>
	    author: string
	    message: string
	    snapshot: tree
	}
	```
- **数据存储与寻址**：
    
    - 对象存储通过其 SHA-1 哈希值实现寻址：
        
        ```python
        id = sha1(object)
        objects[id] = object
        ```
        
    - 引用其他对象时，仅保存哈希值，避免冗余存储。
- **示例：查看对象内容**：
    
    ```bash
    git cat-file -p <hash>
    ```
    
    - **Tree 示例**：
        
        ```text
        100644 blob 4448adbf7ecd394f42ae135bbeed9676e894af85    baz.txt
        040000 tree c68d233a33c5c06e0340e4c224f0afca87c8ce87    foo
        ```
        
    - **Blob 示例**：
        
        ```bash
        git is wonderful
        ```
        

#### **快照 (Snapshot)**
- **被追踪的最顶层的树**
- Git 将顶级目录中的文件和文件夹作为集合，并通过一系列快照来管理其历史记录。

??? info "**快照结构图示**" 
    ```text
    <root> (tree)
    |
    +- foo (tree)
    |  |
    |  + bar.txt (blob, contents = "hello world")
    |
    +- baz.txt (blob, contents = "git is wonderful")
    ```
    
	- 这个顶层的树包含了两个元素
	    - 一个名为 “foo” 的树
		    - 它本身包含了一个 blob 对象 “bar.txt”
		- 以及一个 blob 对象 “baz.txt”


#### **历史记录建模：关联快照 (Modeling history: relating snapshots)**
- **有向无环图（DAG）**：  
    Git 中的历史记录是由快照组成的 DAG，每个提交有一个或多个“父辈”：
    - 单一线性历史：一个快照有一个父辈。
    - 分支和合并历史：快照可能有多个父辈（如合并提交）。
??? note "**图示**"
    ```text
    o <-- o <-- o <-- o <----  o 
                ^            /
                 \          v
                  --- o <-- o
    ```
    
	- 箭头指向了当前提交的父辈（这是一种“在…之前”，而不是“在…之后”的关系）
	- 每次提交都不可更改，修改错误相当于创建新的提交并更新引用。

---


---

### **引用**

- **人类可读的命名**：  
    Git 使用引用（references）替代 40 位十六进制哈希值，便于操作。
    - 引用是指向提交的可变指针。
    - 常见引用：
        - `master`：主分支最新提交。
        - `HEAD`：当前工作目录所在位置。
- **引用操作**：
    
    ```python
    references[name] = commit_id  # 更新引用
    references[name_or_id]       # 读取引用
    ```
    
    - 使用引用代替哈希值操作历史记录。

---

## Git 仓库与暂存区

### **仓库**

- **组成**：对象和引用。
- **操作模型**：
    - Git 的命令是对提交图的操作，例如增删对象和引用。
    - 示例操作：
        
        ```bash
        git checkout master
        git reset --hard <commit_id>
        ```
        

---

### **暂存区（Staging Area）**

- **作用**：  
    暂存区允许用户指定哪些改动将包含在下次提交的快照中。
- **优势**：
    - 提供灵活性：可以为多个功能分别创建独立的提交。
    - 可选择性：支持排除调试信息等临时改动。
- **常用命令**：
    
    ```bash
    git add file_name  # 添加文件到暂存区
    git commit -m "message"  # 基于暂存区内容创建快照
    ```
    

---

## Git 的数据模型特性

- **不可变性**：
    - 所有提交不可更改，但可以通过创建新提交替代原有记录。
- **效率**：
    - 使用哈希值实现高效寻址。
    - 存储引用指针避免重复保存数据。
- **灵活性**：
    - 通过 DAG 实现分支与合并功能。
    - 暂存区提供细粒度的提交控制。

---

Git 的数据模型通过快照、对象和引用构建了一个灵活、高效的版本控制系统。理解这些概念有助于更高效地使用 Git。
## Git 使用基础

### **初始化 Git 仓库**

- 创建本地版本库：
    
    ```bash
    git init  # 初始化当前目录为 Git 仓库
    git init folder_name  # 创建并初始化一个新目录
    ```
    
- 配置用户信息（区分不同协作者）：
    
    - **全局配置**：
        
        ```bash
        git config --global user.name "your_name"
        git config --global user.email "your_email"
        ```
        
    - **单个仓库配置**：与全局配置相同，但不加 `--global`。

---

### **文件操作**

- **暂存修改的文件**：
    
    ```bash
    git add file_name  # 添加文件到暂存区
    git add .          # 添加所有修改的文件
    ```
    
- **删除文件**：
    - 只删除本地文件：
        
        ```bash
        rm file_name
        ```
        
    - 同时删除版本库记录：
        
        ```bash
        git rm file_name
        ```
        
- **重命名文件**：
    
    ```bash
    git mv old_name new_name  # 相当于 mv + git rm + git add
    ```
    
- **检查文件状态**：
    
    ```bash
    git status  # 查看当前工作区和暂存区状态
    ```
    

---

### **提交更改**

- 提交文件：
    
    ```bash
    git commit -m "commit message"  # 提交并添加描述信息
    git commit -a -m "commit message"  # 暂存并提交所有更改
    ```
    
- 查看提交历史：
    
    ```bash
    git log          # 显示详细提交信息
    git log --oneline  # 每条提交显示为单行
    git log --graph   # 显示分支结构
    ```
    

---

### **.gitignore 文件**

- 忽略特定文件或目录：
    
    ```text
    # 语法示例：
    *.log          # 忽略所有 .log 文件
    temp/          # 忽略 temp 文件夹
    !important.log # 强制包含 important.log
    ```
    
- 查看文件是否被忽略：
    
    ```bash
    git check-ignore -v file_name
    ```
    
- 常见语言的模板：[GitHub gitignore 仓库](https://github.com/github/gitignore)。
    

---

### **分支操作**

- **创建分支**：
    
    ```bash
    git branch branch_name  # 创建分支
    git branch -a           # 显示所有分支
    ```
    
- **切换分支**：
    
    ```bash
    git checkout branch_name      # 切换到分支
    git checkout -b branch_name   # 创建并切换到分支
    ```
    
- **合并分支**：
    
    ```bash
    git merge target_branch  # 将目标分支合并到当前分支
    ```
    
    ??? info "Merge 情况分类" 1. **Fast-forward**：当前分支比目标分支更旧，直接移动指针。 2. **Merge Commit**：需要创建合并提交。 3. **冲突解决**：手动解决文件冲突后，`git add` 并提交。

---

### **查看历史版本**

- 查看某一提交：
    
    ```bash
    git show commit_id
    ```
    
- 回退到某一版本：
    
    ```bash
    git checkout commit_id
    ```
    

---

## Git 进阶功能

### **修改历史记录**

- **撤销提交**：
    
    ```bash
    git revert commit_id  # 生成一个新提交以撤销指定提交
    git reset --hard commit_id  # 回到指定提交，丢弃后续修改
    ```
    
- **修改最近提交**：
    
    ```bash
    git commit --amend  # 修改最后一次提交的描述信息
    ```
    

---

### **远程操作**

- **克隆远程仓库**：
    
    ```bash
    git clone remote_url
    ```
    
- **推送更改**：
    
    ```bash
    git push origin branch_name
    ```
    
- **拉取更新**：
    
    ```bash
    git pull origin branch_name  # 包含 fetch 和 merge
    ```
    

---

## 实用技巧与工具

### **签署 Commit**

- 使用 GPG 签名验证：
    - [GitHub 签名验证文档](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)。
    - 验证通过的提交会标记为 `Verified`。

---

### **学习资源**

- [Git 官方文档](https://git-scm.com/docs)
- [Learning Git Branching](https://learngitbranching.js.org/?locale=zh_CN)
- 图书推荐：
    - 《Git 版本控制管理》
    - _Pro Git (2nd Edition)_: [在线阅读](https://git-scm.com/book/en/v2)

---

## 参考资料
-  [Git/GitHub及开源基础](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec2/#/) 
- [Version Control (Git)](https://missing.csail.mit.edu/2020/version-control/)