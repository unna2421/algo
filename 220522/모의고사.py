{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def solution(answers):\
    answer = [0 for i in range(3)]\
\
    man1 = [1,2,3,4,5]\
    man2 = [2,1,2,3,2,4,2,5]\
    man3 = [3,3,1,1,2,2,4,4,5,5]\
    \
    for i in range(len(answers)):\
        ans = answers[i]\
        if(man1[i%len(man1)] == ans):\
            answer[0] += 1\
        if(man2[i%len(man2)] == ans):\
            answer[1] += 1\
        if(man3[i%len(man3)] == ans):\
            answer[2] += 1     \
    \
    result = []\
    for i in range(len(answer)):\
        if(answer[i] == max(answer)):\
            result.append(i+1)\
    \
    return sorted(result)}