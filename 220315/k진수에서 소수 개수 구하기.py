{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl315\partightenfactor0

\f0\fs21 \cf2 \expnd0\expndtw0\kerning0
def solution(n, k):\
    word=''\
\
    while n:\
        word += str(n%k)\
        n = n//k\
\
    word = word[::-1]\
\
    li=word.split('0')\
    lis=[]\
    for i in li:\
        if len(i)>0:\
            lis.append(i)\
    li=list(map(int,lis))\
\
    count=0\
    for i in li:\
        sosu=True\
        if i < 2:\
            continue\
        for j in range(2,int(i**0.5)+1):\
            if i%j==0:\
                sosu=False\
                break\
        if sosu:\
            count+=1\
\
    return count\
}