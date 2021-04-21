'''


Author: alex
Created Time: 2021年04月21日 星期三 10时27分44秒
'''
import ctypes as c

lib = c.CDLL("./main.so")

# 没法用到多核的优势
lib.DoTasksAPI(4, 40)
