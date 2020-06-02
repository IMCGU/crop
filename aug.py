from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

datagen = ImageDataGenerator(
    rotation_range=30,
    channel_shift_range=30,
    shear_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)




def expand_face(img, dir_name, file_name, out_dir, n):#影像增加 接收 一張圖,每個人資料夾名稱,每個人檔名,args.output路徑,要增加幾張
    i = 0
    target_dir = out_dir+'/'+dir_name+'_out' #output的路徑
    if not os.path.exists(target_dir):#建資料夾
        os.makedirs(target_dir)
    for batch in datagen.flow(img, batch_size=1,save_to_dir= target_dir, save_prefix=file_name, shuffle=False, save_format='jpg'):#影像增加採iterator，一次一張圖
        
        i += 1
        if i >= n:
            break  # otherwise the generator would loop indefinitely

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--input-dir', type=str, help='Directory with unaligned images.')
    parser.add_argument('--output-dir', type=str, help='Directory with aligned face thumbnails.')
    parser.add_argument('--expand-num', type=int, default=5, help='How many image you want to expand')
    parser.add_argument('--proc', type=int, default=1, help='protocol layers')
    text = []
    f = open(r'C:\Users\HanHan\insightface-master\datasets\path.txt')#從path.txt去取得所有需要的檔名,檔案路徑等
    args = parser.parse_args()
    for line in f:#把txt存成list
        text.append(line.strip("\n"))
    #print('__DEBUG__%s'%text)
    #print('__DEBUG__numbers of image %s'%len(text))

    
    for i in range(0,len(text)):#跑每一張圖的處理
        
        
        #a=text[i].split(' ')
        path=text[i]#每張圖的路徑存進path
        #print(path)
        path_ = path.split('\\')#把path 透過\\分開
        dir_name=path_[1]#index[1]是資料夾名稱
        file_name = path_[2].split('.')[0]#index[2]是檔名
        print('__DEBUG__file_name: %s '%file_name)#看有沒有存到檔名
        print(path)
        img = cv2.imread(path)#讀圖檔存成一張img
        
        
        im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#img bgr轉成rgb
        x = img_to_array(im_rgb)  # this is a Numpy array with shape (3, 150, 150) 
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
        
        if args.proc == 1:#選擇protocol1
            if 'a' in  file_name.split('_'):#filename照'_'分開，如果有'a'就把圖片影像增加60張。
                print("__DEBUG__protoco1 find")
                expand_face(x, dir_name, file_name, args.output_dir, 60)
        
        if args.proc == 2:
            if 'a' in file_name.split('_') or 'h' in file_name.split('_'):#filename照'_'分開，如果有'a'或'h'就把圖片影像增加30張。
                print("__DEBUG__protocol2 find")
                expand_face(x, dir_name, file_name, args.output_dir, 30)
        
        if args.proc == 3:
            if 'a' in file_name.split('_') or 'I' in file_name.split('_'):#filename照'_'分開，如果有'a'或'I'就把圖片影像增加30張。
                print("__DEBUG__protocol3 find")
                expand_face(x, dir_name, file_name, args.output_dir, 30)

