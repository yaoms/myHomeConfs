#!/usr/bin/python
# coding:utf8
# 作者：yaoms 2012-05-31
# 统计 java 代码行数，不计算注释和空行

import os

line_comment_chars="//"
block_comment_start_chars="/*"
block_comment_end_chars="*/"

def clear_comment_readlines(filename):
    if filename and os.path.isfile(filename):
        lines = open(filename, 'r').readlines()
        newlines=[]
        inCommend=False
        for line in lines:
            if line.strip().startswith(line_comment_chars): line = ""
            pos_line_start=0
            pos_start=0
            pos_end=0
            while line:
                #如果在注释状态
                if inCommend:
                    #查找结束符
                    pos_end=line.find(block_comment_end_chars)
                    #找到了
                    if pos_end!=-1:
                        #删除注释内容
                        line=line[:pos_start]+line[pos_end+2:]
                        #清除注释状态
                        inCommend=False
                        continue
                    #没找到
                    else:
                        #删除整行内容
                        line=line[:pos_start]
                        break
                #如果没在注释状态
                else:
                    #查找开始符
                    pos_line_start=line.find(line_comment_chars)
                    pos_start=line.find(block_comment_start_chars)
                    if pos_line_start!=-1:
                        if pos_line_start < pos_start:
                            line=line[:pos_line_start]
                            break
                    #找到了
                    if pos_start!=-1:
                        #设置注释状态
                        inCommend=True
                        continue
                    #没找到
                    else:
                        break
            newlines.append(line)
        lines = [x for x in newlines if len(x.strip())]
        return lines
    else:
        return []


def count(filename):
    return len(clear_comment_readlines(filename))

def sumcount(filelist):
    c=0
    for f in filelist:
        c+=count(f)
    return c

if __name__ == '__main__':
    import sys
    print sumcount([x.strip() for x in sys.stdin])
    #print "".join(clear_comment_readlines(sys.argv[1])),
    #print count(sys.argv[1])
