# API 学习记录

## opencv

### 图像处理

#### cvtColor
获取二值图


#### GaussianBlur


#### Canny
```
接口解释：
```

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

#### approxPolyDP

```
接口解释：
approxPolyDP是利用给定的点来绘制接近的图案，也就是找出轮廓（例如通过findContours）的多边形拟合曲线。
Explanation:
approxPolyDP expects its input to be a vector of Points. These points define a polygonal curve that will be processed by approxPolyDP. The curve could be open or closed, which can be controlled by a flag.
The ordering of the points in the list is important. Just as one traces out a polygon by hand, each subsequent point in the vector must be the next vertex of the polygon, clockwise or counter-clockwise.
If the list of points is stored in raster order (sorted by Y and then X), then the point[k] and point[k+1] do not necessarily belong to the same curve. This is the cause of the problem.

```
![avatar][1]

* Example 
![avatar][2]


StackOverflow[参考链接](https://stackoverflow.com/questions/22132510/opencv-approxpolydp-for-edge-maps-not-contours)
```
DP是Douglas-Peucker道格拉斯-普克算法
```


#### findContours

findContour用来寻找图像中的轮廓信息。


#### drawContours


* Demo:

contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),3)







### 

[1]: https://images2015.cnblogs.com/blog/1166560/201705/1166560-20170521114407322-795394019.png
[2]: https://i.stack.imgur.com/rjO38.png

