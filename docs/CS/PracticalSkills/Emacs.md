---
counter:
---
# Emacs

## Resource Collection

- [Simon Fraser University](https://mint.westdri.ca/emacs/)
	- 非常好的英文教程，比官方文档亲切多了
- [专业 Emacs 入门](https://pavinberg.github.io/emacs-book/zh/intro/)
    - 教程有些过时的地方（如use package）让Emacs29版本的用户很困惑...
- [Emacs 官方文档](https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html)
- [Emacs Reference Card](https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf)
- [Emacs Survival Card](https://www.gnu.org/software/emacs/refcards/pdf/survival.pdf)
- [remacs的世界](https://remacs.fun/posts/)
	- 很好的教程，有动图演示
- [Master Emacs in 21 Days](https://book.emacs-china.org/)
	- 不适合新手看

## 高级操作备忘

### 删除
- 删除光标所在行： **C-S DEL**

### 文件

- **打开当前文件所在的目录** : 当已经打开了一个文件时，输入 **C-x C-j** 可以打开当前文件所在的目录。

- **移动光标**：按下 **p**（previous）和 **n**（next）来上下移动光标，不需要按 Control 键。
  
- **标记文件**：按 **m** 来标记文件，标记的文件会被选中，可以进行批量操作。
  
- **取消标记**：按 **u** 来取消选中的文件标记。
  
- **删除文件**：按 **d** 来标记删除文件，删除操作不会立即生效，直到按 **x** 执行删除。
  
- **查看帮助**：按 **h** 来查看 Dired 的帮助文档，其中列出了所有可用的命令。


### **搜索 (Search)**

- `C-s`：启动增量搜索 (incremental search)
	- 输入字符后立即搜索并高亮匹配项。
	- 如果再次按下 `C-s`，则会向前搜索下一个匹配项。
- `C-r`：反向增量搜索 (reverse incremental search)
	- 输入字符后立即向反方向搜索并高亮匹配项。
	- 再次按下 `C-r` 可返回查找上一个匹配项。
- 搜索中：
    - `DEL`：撤销上一个输入字符 (undo last character)
    - `C-s`/`C-r`：切换前进或后退方向。
	- 如果出现显示问题，使用 `C-l` 重绘屏幕 (redraw the screen)

---

### **撤销与区域撤销 (Undo and Region Undo)**

- `C-x u`：撤销最近的更改 (undo the last change)
- 区域撤销：
    1. 用 `C-SPC` 设置标记 (mark) 并选定区域
    2. 在选中区域内使用 `C-x u` 撤销仅该区域的更改 (undo changes within the region)

---

### **光标移动 (Cursor Movement)**


---

### **剪切、复制和粘贴 (Cut, Copy, Paste)**

- `C-k`：剪切当前行 (cut the current line)
- `C-y`：粘贴最后剪切或复制的内容 (paste the last cut or copied content)
- 区域操作：
    - `C-SPC`：开始选择区域 (begin selecting a region)
	    - `C-w`：剪切选中区域 (cut the selected region)
	    - `M-w`：复制选中区域 (copy the selected region)
- 粘贴后操作：
    - `M-y`：切换到之前剪切/复制的内容 (cycle through previous yanked items)
    - 相当于回溯剪贴板
- Tips：可以和搜索联合使用
---

### **自动补全 (Autocomplete)**

- `M-/`：根据上下文自动补全单词 (autocomplete word from context)

---

### **键盘宏 (Keyboard Macros)**

- 定义宏：
    1. `C-x (`：开始记录键盘宏 (start recording a macro)
    2. 执行一系列操作。
    3. `C-x )`：停止记录键盘宏 (stop recording the macro)
- 使用宏：
    - `C-x e`：执行宏 (execute the macro)
    - 连续执行：在提示时按 `e` 继续重复宏。

---

### 编译 (Compile)

- `C-c C-v`：在 Emacs 中编译代码 (compile code in Emacs)
    - 执行时，底部显示编译命令 (compile command)，默认是 `make -k`。
	    - `make -k`：尽量继续执行，尽可能显示多个错误信息 (keep going and display as many errors as possible)。
	- `Enter`：执行make
	- 跳转到错误：
		- 在编译输出中，移动光标到错误信息所在行并按下 `Enter`，Emacs 会自动跳转到代码中该错误的位置。
