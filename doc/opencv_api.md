# API 学习记录

## opencv

### 图像处理

#### cvtColor
获取二值图

#### arcLength
```
接口解释：
获取轮廓的长度

参数1：轮廓图像
参数2：bool closed轮廓是否是封闭的
```



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

参数1；image，轮廓图像。一般由findContours提供
参数2：为“ε值”，它表示源轮廓与近似多边形的最大差值
参数3：bool，它表示这个多边形是否闭合。


其中参数1、3比较容易确定，ε可通过OpenCV的cv2.arcLength函数来得到轮廓的周长信息,然后通过比例值来计算。例如1%最大差值
epsilon = 0.01 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
可通过OpenCV来有效地计算一个近似多边形，多边形周长与源轮廓周长之比就为ε。
为了计算凸形状，需要用OpenCV的cv2.convexHull函数来获取处理过的轮廓信息，代码为：
hull = cv2.convexHull(cnt)
```
![avatar][1]

* Example 
![avatar][2]

```

```


StackOverflow[参考链接](https://stackoverflow.com/questions/22132510/opencv-approxpolydp-for-edge-maps-not-contours)
```
DP是Douglas-Peucker道格拉斯-普克算法
```


#### findContours

findContour用来寻找图像中的轮廓信息。

* Example
```
img2, contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
```


#### drawContours
* Example
```
cv.drawContours(img, contours, -1, (0, 0, 255), 3)
cv.namedWindow("Contours", cv.WINDOW_NORMAL)
cv.imshow("Contours", img)
```

* Example

```
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),3)
```







### 

[1]: https://images2015.cnblogs.com/blog/1166560/201705/1166560-20170521114407322-795394019.png
[2]: https://i.stack.imgur.com/rjO38.png

