{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red199\green200\blue201;\red22\green21\blue22;}
{\*\expandedcolortbl;;\cssrgb\c81961\c82353\c82745;\cssrgb\c11373\c10980\c11373\c3922;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
from itertools import permutations\
\
def solution(k, dungeons):\
    dun_num = len(dungeons)\
    answer = 0\
    \
    for permut in permutations(dungeons, dun_num):\
        hp = k\
        count = 0\
        for pm in permut:\
            if hp >= pm[0]:\
                hp -= pm[1]\
                count += 1\
        if count > answer:\
            answer = count\
    \
    return answer\
}