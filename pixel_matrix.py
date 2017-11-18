#coding:utf-8
import numpy as np
from PIL import Image

R = np.zeros([16,16])
G = np.zeros([16,16])
B = np.zeros([16,16])

#画像の読み込み
im = Image.open("emoji/neutral.png")

#RGBに変換
rgb_im = im.convert('RGB')

#画像サイズを取得
size = rgb_im.size

print(size)

#loop
#x
for x in range(size[0]):
    #y
    for y in range(size[1]):
        #ピクセルを取得
        r,g,b = rgb_im.getpixel((x,y))
        R[x][y] = r
        G[x][y] = g
        B[x][y] = b

np.save('neutral_R.npy', R)
np.save('neutral_G.npy', G)
np.save('neutral_B.npy', B)
#
# R2 = np.load('test_R.npy')
# G2 = np.load('test_G.npy')
# B2 = np.load('test_B.npy')
#
# print('')
# print('')
# print('R = ')
# print('')
# print(R)
# print('')
# print('')
# print('G = ')
# print('')
# print(G)
# print('')
# print('')
# print('B = ')
# print('')
# print(B)
# print('')
# print('')
# print('R2 = ')
# print('')
# print(R2)
# print('')
# print('')
# print('G2 = ')
# print('')
# print(G2)
# print('')
# print('')
# print('B2 = ')
# print('')
# print(B2)
