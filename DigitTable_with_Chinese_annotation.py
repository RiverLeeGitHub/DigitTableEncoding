# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:34:13 2017
digit_table encoding
@author: lijiang
"""
########################################################
import random
import numpy as np

seq=[4,6,3,9,1,7,6]#必须输入正整数0~9
encrypted=[]
decrypted=[]
table=np.array([[1,2,3],[4,5,6],[7,8,9]])#数码盘


def location(table,value):#返回value在table中的位置
    x,y=-1,-1
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j]==value:
                x,y=i,j
                return x,y


def encrypt():#加密操作：以序列第一个数字坐标为起始位置，随机选取四个方向，到达下一个方向产生的新的table的目标位置，记录轨迹作为码字
    def move(value,next_value):#四个方向随机选取一个方向延伸table，并作移动
        global table
        
        x0,y0=location(table,value)
        print ("\nvalue %s in table(%s,%s):"%(value,x0,y0,))#确定起始点在初始table的位置
        direction=random.choice(['up','down','left','right'])#选择一个方向进行table的延伸
        print ("Table starts to append",direction)
        
        
        
        if direction=='up':
            tb=np.concatenate([table,table*-1],axis=0)#table进行延伸后，原table区域的值全部取相反数，便于区分value在新旧table中
        if direction=='down':
            tb=np.concatenate([table*-1,table],axis=0)
        if direction=='left':
            tb=np.concatenate([table,table*-1],axis=1)
        elif direction=='right':
            tb=np.concatenate([table*-1,table],axis=1)
        
        print (tb)
        x0,y0=location(tb,value*-1)#查找延伸table中，原value的位置
        x1,y1=location(tb,next_value)#查找延伸table中，新value的位置
        print ("previous value's position in appended table =",value,'(',x0,',',y0,')')
        print ("next value's position in appended table =",next_value,'(',x1,',',y1,')')
        
        track_x=x1-x0#记录从原value到新value的轨迹
        track_y=y1-y0
        print ("track =",'(',track_x,',',track_y,')')
        encrypted.append(track_x)
        encrypted.append(track_y)#将轨迹添加到码字
        print ("present encrypted code:",encrypted)
        return next_value
    
    print ("\n--------------------")
    print ("Encrypting:")
    value=seq.pop(0)#取序列第一位作为初始位置
    x0,y0=location(table,value)
    encrypted.append(x0)
    encrypted.append(y0)
    for i in range(len(seq)):#对序列的每一位进行遍历加密
        value=move(value,next_value=seq.pop(0))
    
def decrypt():#解密操作：在已知初始value位置的情况下，按照轨迹查找相应下一位置的value
    print ("\n--------------------")
    print ("Decrypting:")
    print ("\nencrypted sequence:",encrypted)
    
    x0,y0=encrypted.pop(0),encrypted.pop(0)
    decrypted.append(table[x0,y0])#密码前两位为初始value的坐标
    value0=table[x0,y0]
    for i in range(len(encrypted)//2):#对密码序列进行遍历解码，由于密码为横纵轨迹的组合，故成对提取
        a=encrypted.pop(0)#a,b为行列坐标轨迹
        b=encrypted.pop(0)
        x0,y0=location(table,value0)#确定初始value在原table中的位置
        print ("\nvalue %s in table(%s,%s):"%(value0,x0,y0))
        x1=x0+a#将初始位置加上轨迹，确定新位置的状态（由于table没有进行延伸，状态必将超出table范围，则可以通过判断异常来确定延伸方向）
        y1=y0+b
        if x1<0:#如果新的行坐标为负，则table应该向上延伸
            print ("Going up")
            tb=np.concatenate([table,table*-1],axis=0)#原table的值不变，延伸的table值取相反数，延伸的table记为tb
            x0,y0=location(tb,value0*-1)#找到原value在延伸table中的位置
            x1=x0+a
            y1=y0+b#确定下一个value在延伸table中的位置
            print (tb)
            print ("Value %s is in appended table(%s,%s) now"%(value0,x0,y0))
            print ("track: (%s,%s)"%(a,b))
            print ("Changing position: (%s,%s)->(%s,%s)"%(x0,y0,x1,y1))
            value1=tb[x1,y1]#通过新位置找到下一个value的值
            print ("Add value to decrypted sequence:",value1)
            decrypted.append(value1)
            value0=value1
        if x1>2:#如果新的行坐标超过三行，则table应该向下延伸
            print ("Going down")
            tb=np.concatenate([table*-1,table],axis=0)
            x0,y0=location(tb,value0*-1)
            x1=x0+a
            y1=y0+b
            print (tb)
            print ("Value %s is in appended table(%s,%s) now"%(value0,x0,y0))
            print ("track: (%s,%s)"%(a,b))
            print ("Changing position: (%s,%s)->(%s,%s)"%(x0,y0,x1,y1))
            value1=tb[x1,y1]#通过新位置找到下一个value的值
            print ("Add value to decrypted sequence:",value1)
            decrypted.append(value1)
            value0=value1
        if y1<0:#如果新的列坐标为负，则table应该向左延伸
            print ("going left")
            tb=np.concatenate([table,table*-1],axis=1)
            x0,y0=location(tb,value0*-1)
            x1=x0+a
            y1=y0+b
            print (tb)
            print ("Value %s is in appended table(%s,%s) now"%(value0,x0,y0))
            print ("track: (%s,%s)"%(a,b))
            print ("Changing position: (%s,%s)->(%s,%s)"%(x0,y0,x1,y1))
            value1=tb[x1,y1]#通过新位置找到下一个value的值
            print ("Add value to decrypted sequence:",value1)
            decrypted.append(value1)
            value0=value1
        if y1>2:#如果新的列坐标超过三列，则table应该向右延伸
            print ("going right")
            tb=np.concatenate([table*-1,table],axis=1)
            x0,y0=location(tb,value0*-1)
            x1=x0+a
            y1=y0+b
            print (tb)
            print ("Value %s is in appended table(%s,%s) now"%(value0,x0,y0))
            print ("track: (%s,%s)"%(a,b))
            print ("Changing position: (%s,%s)->(%s,%s)"%(x0,y0,x1,y1))
            value1=tb[x1,y1]#通过新位置找到下一个value的值
            print ("Add value to decrypted sequence:",value1)
            decrypted.append(value1)
            value0=value1
    
if __name__=="__main__":#主函数
    
    print ("\ninitial sequence:",seq)
    
    print ("\ndigit table:\n",table)
    
    encrypt()#加密
    
    decrypt()#解密
            
    print ("\ndecrypted sequence:",decrypted)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
