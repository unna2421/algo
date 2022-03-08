{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red199\green200\blue201;\red20\green22\blue25;}
{\*\expandedcolortbl;;\cssrgb\c81961\c82353\c82745;\cssrgb\c10196\c11373\c12941;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from collections import deque\
def solution(maps):\
\'a0\'a0\'a0\'a0answer = 0\
\'a0\'a0\'a0\'a0queue = deque([[0,0]])\
\'a0\'a0\'a0\'a0n = len(maps)\
\'a0\'a0\'a0\'a0m = len(maps[0])\
\'a0\'a0\'a0\'a0d = [(1,0),(-1,0),(0,1),(0,-1)]\
\'a0\'a0\'a0\'a0while queue:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0x,y = queue.popleft()\
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0for dx,dy in d:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0xx = x+dx\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0yy = y+dy\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0if 0<=xx<n and 0<=yy<m and maps[xx][yy]==1:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0queue.append([xx,yy])\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0maps[xx][yy] = maps[x][y]+1\
\'a0\'a0\'a0\'a0if maps[n-1][m-1]!=1:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return maps[n-1][m-1]\
\'a0\'a0\'a0\'a0else:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return -1}