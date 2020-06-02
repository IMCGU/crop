import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--input-dir', type=str, help='Directory with unaligned images.')
    parser.add_argument('--output-dir', type=str, help='Directory with aligned face thumbnails.')
    parser.add_argument('--proc', type=int, default=1, help='protocol layers')
    args = parser.parse_args()
    f=open('C://Users//HanHan//insightface-master//datasets//testpath.txt','r')
    text=[]
    for line in f:
        text.append(line.strip('\n'))
    #print(text)
    #print(text[0])
    for i in range(0,len(text)):#跑每一張圖的處理
        
        
        #a=text[i].split(' ')
        path=text[i]#每張圖的路徑存進path
        #print(path)
        path_ = path.split('\\')#把path 透過\\分開
        dir_name=path_[1]#index[1]是資料夾名稱
        file_name = path_[2].split('.')[0]
        
        img = cv2.imread(path)
        plt.imshow(img)
        #plt.show()
        
        if args.proc == 1:#選擇protocol1
            if 'h' in  file_name.split('_')or 'I' in  file_name.split('_'):
                
                print("__DEBUG__protoco1 find")
                print(file_name)
                pass
            else:
                target_dir = os.path.join(args.output_dir, dir_name)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                target_file = os.path.join(target_dir,file_name)
                cv2.imwrite(target_file+'.jpg',img)
                  






