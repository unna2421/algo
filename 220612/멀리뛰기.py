{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def solution(n):\
    if n < 2:\
        return n\
    \
    dp = [0 for _ in range(n)]\
    dp[0] = 1\
    dp[1] = 2\
    \
    for i in range(2, n):\
        dp[i] = dp[i-1] + dp[i-2]\
        \
    return dp[-1] % 1234567}