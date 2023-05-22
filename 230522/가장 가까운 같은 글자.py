{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl315\partightenfactor0

\f0\fs21 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def solution(s):\
    answer = []\
    s_dict = dict()\
    \
    for i in range(len(s)):\
        if s[i] not in s_dict:\
            answer.append(-1)\
        else:\
            answer.append(i-s_dict[s[i]])\
        s_dict[s[i]] = i\
        \
    return answer\
}