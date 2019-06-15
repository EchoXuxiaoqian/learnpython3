#!/usr/bin/env python3  #注释运行环境
# -*- coding:utf-8 -*-  #说明文件编码方式

'a test module'     # 模块的文档注释

__author__ = 'xxq'  # 作者，以上为模块的标准文件模板

import sys
def test():
    args = sys.argv     #获取命令行参数。第一个参数为文件名称
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello %s!' % args[1])
    else:
        print('too many arguments')
        
if __name__ == '__main__':  #用于运行测试，引入到别的模块中执行不通过
    test()
    
def _private(name):     # 私有函数，不建议外部引用
    print('hello ')