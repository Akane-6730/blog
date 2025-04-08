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

## Misc
- 以下根据我自己踩过的一些坑做了一些经验总结，帮助你在上手时就获得极致的体验😊
1. Ubuntu 装 Emacs30 可以通过 snap
2. windows terminal 启动真彩色防止与 Emacs 主题冲突，在终端输入
```shell
export TERM=xterm-direct
```
3. wslg 模拟的图形化界面分辨率低？[参考这个回答](https://github.com/microsoft/wslg/issues/590#issuecomment-2320164818)
	- 创建文件 C:/users/username/.wslgconfig，写入
	```
	[system-distro-env]
	WESTON_RDP_HI_DPI_SCALING=true
	WESTON_RDP_FRACTIONAL_HI_DPI_SCALING=true
	WESTON_RDP_DEBUG_DESKTOP_SCALING_FACTOR=100
	```
	- 然后重启wsl即可

## 高级操作备忘

### 删除
- 删除光标所在行： **C-S DEL**
---
### 文件

- **打开当前文件所在的目录** : 当已经打开了一个文件时，输入 **C-x C-j** 可以打开当前文件所在的目录。

---
### **撤销与区域撤销 (Undo and Region Undo)**

- `C-x u`：撤销最近的更改 (undo the last change)
- 区域撤销：
    1. 用 `C-SPC` 设置标记 (mark) 并选定区域
    2. 在选中区域内使用 `C-x u` 撤销仅该区域的更改 (undo changes within the region)

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
