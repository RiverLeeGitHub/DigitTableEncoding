# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:34:13 2017
digit_table encoding
@author: lijiang
"""
########################################################
import random
import numpy as np

seq=[4,6,3,9,1,7,6]#set positive integer
encrypted=[]
decrypted=[]
table=np.array([[1,2,3],[4,5,6],[7,8,9]])#digit table


def location(table,value):#return value's position in table
    x,y=-1,-1
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j]==value:
                x,y=i,j
                return x,y



def encrypt():
    '''
    Encrypt operation:
    Generate a 3*3 digit table first.
    Set the coordinate of the first number of sequence as initial position,
    choose 4 directions randomly, and append the previous table.
    All the number in previous region are set negative.
    Determine aim coordinate in newly appended table，
    The encrypted code will append the track from previous coordinate to aim coordinate.
    '''
    def move(value,next_value):#Randomly choose 4 directions to append the table
        global table
        
        x0,y0=location(table,value)
        print ("\nvalue %s in table(%s,%s):"%(value,x0,y0,))#Determine the coordinate of initial point in the table
        direction=random.choice(['up','down','left','right'])#Choose a direction
        print ("Table starts to append",direction)
        
        
        
        if direction=='up':
            tb=np.concatenate([table,table*-1],axis=0)#After the table is extended, the number of previous table are set negative, to better distinguish previous and new table
        if direction=='down':
            tb=np.concatenate([table*-1,table],axis=0)
        if direction=='left':
            tb=np.concatenate([table,table*-1],axis=1)
        elif direction=='right':
            tb=np.concatenate([table*-1,table],axis=1)
        
        print (tb)
        x0,y0=location(tb,value*-1)#Search the previous number's position in appended table
        x1,y1=location(tb,next_value)#Search the new number's position in appended table
        print ("previous value's position in appended table =",value,'(',x0,',',y0,')')
        print ("next value's position in appended table =",next_value,'(',x1,',',y1,')')
        
        track_x=x1-x0#Record the track from previous coordinate to the new.
        track_y=y1-y0
        print ("track =",'(',track_x,',',track_y,')')
        encrypted.append(track_x)
        encrypted.append(track_y)#Add track to the codes
        print ("present encrypted code:",encrypted)
        return next_value
    
    print ("\n--------------------")
    print ("Encrypting:")
    value=seq.pop(0)#Set the first place as initial position
    x0,y0=location(table,value)
    encrypted.append(x0)
    encrypted.append(y0)
    for i in range(len(seq)):#encrypted every place in the sequence
        value=move(value,next_value=seq.pop(0))

def decrypt():
    '''
    Decrypt operation:
    The first two place of the encrypted sequence stands for the coordinate of initial value,
    we flow the track to find the next value.
    '''
    print ("\n--------------------")
    print ("Decrypting:")
    print ("\nencrypted sequence:",encrypted)
    
    x0,y0=encrypted.pop(0),encrypted.pop(0)
    decrypted.append(table[x0,y0])#The first two place of the encrypted sequence stands for the coordinate of initial value
    value0=table[x0,y0]
    for i in range(len(encrypted)//2):#Decrypt the sequence. Pair extraction for the x,y combination
        a=encrypted.pop(0)#a,b stand for the track in row and column
        b=encrypted.pop(0)
        x0,y0=location(table,value0)#Determin the coordinate of initial value in previous table
        print ("\nvalue %s in table(%s,%s):"%(value0,x0,y0))
        x1=x0+a
        y1=y0+b
        if x1<0:#if new row-coordinate is negative, the table should append up
            print ("Going up")
            tb=np.concatenate([table,table*-1],axis=0)#values in previous table region are set negative, the newly extended table is called tb
            x0,y0=location(tb,value0*-1)#Find the previous position in appended table
            x1=x0+a
            y1=y0+b#Determine the position of next value in appended table
            print (tb)
            print ("Value %s is in appended table(%s,%s) now"%(value0,x0,y0))
            print ("track: (%s,%s)"%(a,b))
            print ("Changing position: (%s,%s)->(%s,%s)"%(x0,y0,x1,y1))
            value1=tb[x1,y1]#Find next value by new position
            print ("Add value to decrypted sequence:",value1)
            decrypted.append(value1)
            value0=value1
        if x1>2:#if new row-coordinate exceed 3 rows, the table should append down
            print ("Going down")
            tb=np.concatenate([table*-1,table],axis=0)
            x0,y0=location(tb,value0*-1)
            x1=x0+a
            y1=y0+b
            print (tb)
            print ("Value %s is in appended table(%s,%s) now"%(value0,x0,y0))
            print ("track: (%s,%s)"%(a,b))
            print ("Changing position: (%s,%s)->(%s,%s)"%(x0,y0,x1,y1))
            value1=tb[x1,y1]
            print ("Add value to decrypted sequence:",value1)
            decrypted.append(value1)
            value0=value1
        if y1<0:#if new col-coordinate is negative, the table should append left
            print ("going left")
            tb=np.concatenate([table,table*-1],axis=1)
            x0,y0=location(tb,value0*-1)
            x1=x0+a
            y1=y0+b
            print (tb)
            print ("Value %s is in appended table(%s,%s) now"%(value0,x0,y0))
            print ("track: (%s,%s)"%(a,b))
            print ("Changing position: (%s,%s)->(%s,%s)"%(x0,y0,x1,y1))
            value1=tb[x1,y1]
            print ("Add value to decrypted sequence:",value1)
            decrypted.append(value1)
            value0=value1
        if y1>2:#if new col-coordinate exceed 3 columns, the table should append right
            print ("going right")
            tb=np.concatenate([table*-1,table],axis=1)
            x0,y0=location(tb,value0*-1)
            x1=x0+a
            y1=y0+b
            print (tb)
            print ("Value %s is in appended table(%s,%s) now"%(value0,x0,y0))
            print ("track: (%s,%s)"%(a,b))
            print ("Changing position: (%s,%s)->(%s,%s)"%(x0,y0,x1,y1))
            value1=tb[x1,y1]
            print ("Add value to decrypted sequence:",value1)
            decrypted.append(value1)
            value0=value1
    
if __name__=="__main__":#Main function
    
    print ("\ninitial sequence:",seq)
    
    print ("\ndigit table:\n",table)
    
    encrypt()#Encrypt operation
    
    decrypt()#Decrypt operation
            
    print ("\ndecrypted sequence:",decrypted)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
