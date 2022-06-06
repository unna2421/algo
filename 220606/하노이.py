{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl315\partightenfactor0

\f0\fs21 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def dfs(queen, n, row):\
    count = 0\
    if n == row:\
        return 1\
    for col in range(n):\
        queen[row] = col\
        for x in range(row):\
            if queen[x] == queen[row]: \
                break\
            if abs(queen[x]-queen[row]) == (row-x):\
                break\
        else:\
            count += dfs(queen, n, row+1)  \
    return count\
\
def solution(n):\
    queen = [0]*n\
    return dfs(queen, n, 0)}