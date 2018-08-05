# DigitTableEncoding九宫格编码
A self-invented encoding method towards digit sequence<br>
一个自创的面向数字序列的编码方法
(2017.12)

## Introduction
DigitTable Encoding: Randomly extended 4 directions of a digit table, the tracks from previous place to the next were taken for codes.<br>
“九宫格”编码：随机延伸九宫格的四个方向，从已知位到目标位移动的轨迹作为码字进行编码。

## Idea
Getting inspiration from Sudoku, nine digits are arrayed in 3*3 matrix(and we call 'table' below). Take sequence [ 4 , 9 , 7 ] as an example, the first place is 4, and its coordinate in table is (1,0), which stands for two lines and one column. The second digit 9 is in (2,2), and the third lies in (2,0). Several input signals in the sequence produce several tables. As shown in the following figure.<br>
从九宫格中获得灵感，输入信号可以为1~9九个数字，这九个数字按照固定的顺序排列在九宫格中，以序列 [ 4 , 9 , 7 ] 为例，选择序列第一个数字4，找到4在九宫格中的位置为二行一列 ( 1 , 0 ) ，第二个数字9在九宫格的位置是三行三列 ( 2 , 2 ) ，第三个数字7在九宫格的位置是三行一列 ( 2 , 0 ) 。序列中有几个输入信号就产生几个九宫格，如下图所示。<br><br>
![](https://raw.githubusercontent.com/RiverLeeGitHub/DigitTableEncoding/master/img_archive/demo1.png) <br><br>
Because 4 is the first digit in sequence, its coordinate (1,0) is added to the codes first. As a result, our currently codes is [1,0]. The table where 4 lies in is about to be extended in up, down, left, right four directions randomly. Given the table is appended right and then generate an appended table, it's going to be like the following figure.<br>
4是序列的第一位，所以先将4的位置作为起始坐标 ( 1 , 0 ) 加入编码序列，则当前编码为 [ 1 , 0 ] 。4所在的九宫格随机在上下左右四个方向中选一个延伸，以4到6随机结果向右为例，生成延伸九宫格，如下图所示。<br><br>
![](https://raw.githubusercontent.com/RiverLeeGitHub/DigitTableEncoding/master/img_archive/demo2.png) <br><br>
In the appended table above, the coordinate of 4 is (1,0), and 9 for (2,5), so the track from 4 to 9 is (1,5). This track will be added to the encoding sequence, and the current codes is [1,0,1,5].<br>
在上图延伸九宫格中，4的坐标是 ( 1 , 0 ) ，9的坐标是 ( 2 , 5 ) , 则4→9的轨迹是 ( 1 , 5 ) ，该轨迹作为码字添加到编码序列中，当前编码序列为 [ 1 , 0 , 1 , 5 ] 。<br><br>
The table where 9 lies in will be extended in four directions randomly again. If the table is appended up, we generate new appended table like this:<br>
9所在的九宫格随机在上下左右四个方向中选一个延伸，以9到7随机结果向上为例，生成新的延伸九宫格，如下图所示。
<br><br>
![](https://raw.githubusercontent.com/RiverLeeGitHub/DigitTableEncoding/master/img_archive/demo3.png) <br><br>
In the extended table above, the coordinate of 9 is (5,2) and 7 for (2,0), so the track from 9 to 7 is (-3,-2). This track will be added to the encoding sequence, and the current codes is [1,0,1,5,-3,-2].<br>
在上图延伸九宫格中，9的坐标是 ( 5 , 2 ) ，7的坐标是 ( 2 , 0 ) , 则9→7的轨迹是( -3 , -2 )，该轨迹作为码字添加到编码序列中，当前编码序列为 [ 1 , 0 , 1 , 5 , -3 , -2 ]。<br><br>
The process of decrypting then chooses the first two places as an initial coordinate, and the rest stands for tracks. The table will be automatically extended to assigned direction and find the next value we are looking for.<br>
解码过程则通过选取编码序列的前两位作为起始位置，后面的为轨迹，从指定方向延伸九宫格，确定解码的值。

## Something to say
1. DigitTable extended the table in random direction, which can increase the randomness when encrypting. Meanwhile, users can DIY their own digit in the table in adapting to different demands, which can also enhance the security of this procedure.
  “九宫格编码”以随机方向延伸九宫格，增加了编码的无序性；同时，用户可以根据自己的需求自定义九宫格里的数字，起到了一定的保密性。
2. Tables can be adjust to different size as long as it is rectangule.  “九宫格编码”的九宫格不一定是3×3的矩阵，还可以是任意长宽的矩阵。
3. The limitation of this method is an increasement of sequence length.  “九宫格编码”的局限性在于增加了序列长度和存储的空间。
