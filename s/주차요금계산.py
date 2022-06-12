{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def solution(fees, records):\
    time = \{\}\
    start = \{\}\
    end = 23*60 + 59\
    fee = \{\}\
    \
    for re in records:						\
        words = re.split()\
        t = int(words[0][0:2]) * 60 + int(words[0][3:])\
        \
        if words[2] == "IN":\
            start[words[1]] = t\
        else:\
            tdel = t - start[words[1]]\
            time[words[1]] = tdel if words[1] not in time else time[words[1]] + tdel\
            start[words[1]] = -1\
            \
    \
    for s in start:			\
        if start[s] != -1:\
            tdel = end - start[s]\
            time[s] = tdel if s not in time else time[s] + tdel\
    \
    for t in time:			\
        fee[t] = fees[1]\
        if time[t] > fees[0]:\
            if (time[t]-fees[0]) % fees[2] == 0:\
                fee[t] += (int((time[t]-fees[0])/fees[2]))*fees[3]\
            else:\
                fee[t] += (int((time[t]-fees[0])/fees[2]+1))*fees[3]\
            \
    fee = sorted(fee.items())		\
    answer = [x[1] for x in fee]\
\
    \
    return answer}