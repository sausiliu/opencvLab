# 算法集锦

在学习图像处理的过程中，发现核心技术离不开各种各样的算法。 像图像的边缘信息、噪声分别基本都是处理高频信号。对信号的积分微分也体现出了不同的作用。例如使得图像更加锐利就要对信号进行微分，让图像显得更加“平滑”就对信号进行积分，当然，这些说起来比做要简单很多。在图像处理的实际应用中，会涉及到很多算法知识，为了更系统的理解算法的**应用**从而对一些常用的算法知识进行总结。<br>
*并非数学专业，可能在理解上存在错误,所以对算法的理解上会定时更新文档*

## Filter
## 1. Bialteral[baɪˈlætərəl] 双边滤波
双边滤波是一种非线性滤波方式，能在实现降噪平滑的效果同时保留边缘信息。
参考[wiki链接][1]

在了解双边算法同时可以先理解高斯滤波。

### 图示效果

算法效果图
* 高斯滤波

![avatar][2]
*图片来自于互联网*


* 双边滤波 

![avatar][3]
*图片来自于互联网*

* 滤波效果对比
![avatar][4]


###


## 2. Canny edge detector
Canny是由 John F. Canny 在1986年发明的。主要用于更准确的监测出边缘信息。
参考[wiki][5]

###  使用方法

在检测边缘信息（使用Canny算法）前，需要对图像进行模糊处理（降噪）。由于边缘检测主要是处理高频信息，但是噪声也主要集中在高频信息中,所以噪声的存在会影响到边缘检测的效果。

1. 模糊处理
高斯滤波对图像进行平滑处理（降噪，降低细节层次）。注意在处理中半径不宜太大，半径过大会影响到边缘信息的模糊。

###





[1]: https://en.wikipedia.org/wiki/Bilateral_filter "wiki Bialteral Filter"
[2]: https://www.cmlab.csie.ntu.edu.tw/~zho/Bilateral/html-data/equ02.png "Gaussian filter as weighted average"
[3]: https://www.cmlab.csie.ntu.edu.tw/~zho/Bilateral/html-data/equ03.png "Bilateral filter"
[4]: https://www.cloudcompare.org/doc/wiki/images/5/5f/Cc_sf_gaussian_filter.jpg ""
[5]: https://en.wikipedia.org/wiki/Canny_edge_detector "Canny edge detector"
