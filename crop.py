import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import argparse



def imread(path):
    im_rgb = cv2.imread(path,cv2.COLOR_BGR2RGB)
    #im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return im_rgb

def imsave(img_name,img_dir,image,args):
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    c,d = img_dir , img_name
                #print('a:%s'%a)
                #print('b:%s'%b)
    target_dir = os.path.join(args.output_dir, c)
    #print(target_dir)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        #print(d)
    target_file = os.path.join(target_dir,d)
    cv2.imwrite(target_file,image)
   # cv2.imwrite('C:/Users/HanHan/insightface-master/datasets/Training_data/img_name',image)
def crop_center(path,x1,x2,y1,y2,args):
    # y,x = img.shape
    # startx = x//2-(cropx//2)
    # starty = y//2-(cropy//2) 
    # print(x1)
    # print(x2)
    # print(y1)
    # print(y2)


    img = imread(path)
    plt.imshow(img)
    #plt.show()
    #plt.imshow(img[y1:y2,x1:x2])
    #plt.show()
    img_dir = path.split('/')[1]
    img_name = path.split('/')[2]
    result_img = img[y1:y2,x1:x2]
    result_result_img=cv2.resize(result_img, (112, 112), interpolation=cv2.INTER_LINEAR)
    imsave(img_name,img_dir,result_result_img,args)
   # return img[x1:x2,y1:y2]



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--input-dir', type=str, help='Directory with unaligned images.')
    parser.add_argument('--output-dir', type=str, help='Directory with aligned face thumbnails.')
    
    text = []
    f = open(r'C:\Users\HanHan\insightface-master\datasets\test.txt')

    args = parser.parse_args()
    for line in f:
        text.append(line.strip("\n"))
    # print(text)
    # print(len(text))
    # print(text[0])
   
    for i in range(0,len(text)):
        a=text[i].split(' ')
        print('__debug__',a)
        path=a[0]
        img_dir = path.split('/')[1]
        img_name = path.split('/')[2]
        print(img_dir)
        print(img_name)
        x1=int(float(a[1]))#x1 258.770721
        x2=int(float(a[3]))#x2 414.062042
        y1=int(float(a[2]))
        y2=int(float(a[4]))
        
        crop_center(path,x1,x2,y1,y2,args)
       # imsave(img_name,img[y1:y2,x1:x2])
        print("*************")
        print(path)
        # print(x1)
        # print(x2)
        # print(y1)
        # print(y2)
        
        
    








