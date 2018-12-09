一、杂项
1.Julia是互交式的语言，想要不即时互交：
(1)使用Ipython + IJulia:
#已经安装好后
using IJulia
notebook()
(2)将代码保存为.jl文件，然后用 include("file.jl")调用

2.Julia教程
(1)很官方的教程 : https://docs.julialang.org/en/release-0.3/manual/variables/

二、基础语法
2.1 case-sensetive, Unicode names allowed, 命名规则同Python除可用Unicode character (神TM竟然可以给+号赋值)

2.2 shift+/ 进入help模式

2.3 typeof(x), typemin(x), typemax(x) - overflow -> wraparound

for T = {Int8,Int16,Int32,Int64,Int128,Uint8,Uint16,Uint32,Uint64,Uint128}
    println("$(lpad(T,7)): [$(typemin(T)),$(typemax(T))]")
end

2.4 ans - 上一次输出的变量

2.5 0b, 0o, 0x- binary, octal, hexa

2.5 Inf, -Inf, NaN - 正无穷，负无穷，非数值

2.6 bis(x) - 内存中的01储存

2.7 eps(type) - machine epsilon - Most real numbers cannot be represented exactly with floating-point numbers, and so for many purposes it is important to know the distance between two adjacent representable floating-point numbers

2.8 /, \, % - 除，反除，求余

2.9 isa(x,type) - 类型检验

2.10 ==, !=

2.11 isequal(), isfinite(), isinf(),isnan()

2.12 Rounding functions || Division functions || Sign and absolute value functions || Powers, logs and roots
https://docs.julialang.org/en/release-0.3/manual/mathematical-operations/
