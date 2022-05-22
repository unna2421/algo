{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red70\green137\blue204;\red212\green212\blue212;\red31\green31\blue34;
\red203\green139\blue114;\red171\green208\blue146;}
{\*\expandedcolortbl;;\cssrgb\c33725\c61176\c83922;\cssrgb\c86275\c86275\c86275;\cssrgb\c16078\c16471\c17647;
\cssrgb\c83922\c61569\c52157;\cssrgb\c72157\c84314\c63922;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf3 \cb4 \strokec3  itertools \cf2 \cb1 \strokec2 import\cf3 \cb4 \strokec3  combinations\
\cf2 \cb1 \strokec2 from\cf3 \cb4 \strokec3  collections \cf2 \cb1 \strokec2 import\cf3 \cb4 \strokec3  defaultdict\
\
\cf2 \cb1 \strokec2 def\cf3 \strokec3  solution(infos, querys):\cb4 \
    answer = []\
    info_dict = defaultdict(list)\
    \cf2 \cb1 \strokec2 for\cf3 \cb4 \strokec3  info \cf2 \cb1 \strokec2 in\cf3 \cb4 \strokec3  infos:\
        temp = info.split(\cf5 \cb1 \strokec5 " "\cf3 \cb4 \strokec3 )\
        key = temp[\cf6 \cb1 \strokec6 0\cf3 \cb4 \strokec3 :\cf6 \cb1 \strokec6 -1\cf3 \cb4 \strokec3 ]\
        score = int(temp[\cf6 \cb1 \strokec6 -1\cf3 \cb4 \strokec3 ])\
\
        \cf2 \cb1 \strokec2 for\cf3 \cb4 \strokec3  i \cf2 \cb1 \strokec2 in\cf3 \cb4 \strokec3  range(\cf6 \cb1 \strokec6 5\cf3 \cb4 \strokec3 ):\
            combi = list(combinations(key, i))\
            \cf2 \cb1 \strokec2 for\cf3 \cb4 \strokec3  c \cf2 \cb1 \strokec2 in\cf3 \cb4 \strokec3  combi:\
                temp_key = \cf5 \cb1 \strokec5 ''\cf3 \cb4 \strokec3 .join(c)\
                info_dict[temp_key].append(score)\
\
    \cf2 \cb1 \strokec2 for\cf3 \cb4 \strokec3  key \cf2 \cb1 \strokec2 in\cf3 \cb4 \strokec3  info_dict.keys():\
        info_dict[key].sort()\
\
    \cf2 \cb1 \strokec2 for\cf3 \cb4 \strokec3  query \cf2 \cb1 \strokec2 in\cf3 \cb4 \strokec3  querys:\
        query = query.split(\cf5 \cb1 \strokec5 " "\cf3 \cb4 \strokec3 )\
        query_score = int(query[\cf6 \cb1 \strokec6 -1\cf3 \cb4 \strokec3 ])\
        query_key = query[:\cf6 \cb1 \strokec6 -1\cf3 \cb4 \strokec3 ]\
\
        \cf2 \cb1 \strokec2 for\cf3 \cb4 \strokec3  _ \cf2 \cb1 \strokec2 in\cf3 \cb4 \strokec3  range(\cf6 \cb1 \strokec6 3\cf3 \cb4 \strokec3 ):\
            query_key.remove(\cf5 \cb1 \strokec5 "and"\cf3 \cb4 \strokec3 )\
\
        \cf2 \cb1 \strokec2 while\cf3 \cb4 \strokec3  \cf5 \cb1 \strokec5 "-"\cf3 \cb4 \strokec3  \cf2 \cb1 \strokec2 in\cf3 \cb4 \strokec3  query_key:\
            query_key.remove(\cf5 \cb1 \strokec5 "-"\cf3 \cb4 \strokec3 )\
        query_key = \cf5 \cb1 \strokec5 ''\cf3 \cb4 \strokec3 .join(query_key)\
\
        \cf2 \cb1 \strokec2 if\cf3 \cb4 \strokec3  query_key \cf2 \cb1 \strokec2 in\cf3 \cb4 \strokec3  info_dict:\
            scoreList = info_dict[query_key]\
\
            \cf2 \cb1 \strokec2 if\cf3 \cb4 \strokec3  len(scoreList) > \cf6 \cb1 \strokec6 0\cf3 \cb4 \strokec3 :\
                left, right = \cf6 \cb1 \strokec6 0\cf3 \cb4 \strokec3 , len(scoreList)\
                \cf2 \cb1 \strokec2 while\cf3 \cb4 \strokec3  left < right:\
                    mid = (left + right) // \cf6 \cb1 \strokec6 2\cf3 \cb4 \strokec3 \
                    \cf2 \cb1 \strokec2 if\cf3 \cb4 \strokec3  scoreList[mid] >= query_score:\
                        right = mid\
                    \cf2 \cb1 \strokec2 else\cf3 \cb4 \strokec3 :\
                        left = mid+\cf6 \cb1 \strokec6 1\cf3 \cb4 \strokec3 \
                answer.append(len(scoreList)-left)\
        \cf2 \cb1 \strokec2 else\cf3 \cb4 \strokec3 :\
            answer.append(\cf6 \cb1 \strokec6 0\cf3 \cb4 \strokec3 )\
\
    \cf2 \cb1 \strokec2 return\cf3 \cb4 \strokec3  answer}