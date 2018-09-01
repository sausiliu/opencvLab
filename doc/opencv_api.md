# API 学习记录

## opencv

### 图像处理

* cvtColor
获取二值图


. GaussianBlur


* Canny

image 单通道输入图像<br>
edges 单通道存储边缘的输出图像<br> 
threshold1 第一个阈值<br>
threshold2 第二个阈值<br>
aperture_size Sobel算子内核大小

```
滞后阈值: 最后一步，Canny 使用了滞后阈值，滞后阈值需要两个阈值(高阈值和低阈值):

如果某一像素位置的幅值超过 高 阈值, 该像素被保留为边缘像素。
如果某一像素位置的幅值小于 低 阈值, 该像素被排除。
如果某一像素位置的幅值在两个阈值之间,该像素仅仅在连接到一个高于高阈值的像素时被保留。
Canny 推荐的 高:低 阈值比在 2:1 到3:1之间。
```

* approxPolyDP


* findContours

findContour用来寻找图像中的轮廓信息。


* drawContours


Demo:

contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),3)




![avatar][1]



### 

[1]: https://images2015.cnblogs.com/blog/1166560/201705/1166560-20170521114407322-795394019.png

