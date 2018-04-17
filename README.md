# Interactive Object Detection

Object Detection using Hough Forests and Interactive Learning using Active Learning.

This was a part of my Master Thesis.

Hough forests are random forests adapted to perform generalized Hough transform in an efficient way. Interactive learning is is done using Active learning which is based on rate of false positive and false negatuve rate.

![](https://github.com/priyankavokuda/interactive_object_detection/blob/master/images/interactive_learning.PNG)

## Dependencies

Python 2.7
Flask 0.12.2

## Usage
⋅⋅* Install Hough Forest library from https://github.com/classner/fertilized-forests.
⋅⋅* Copy interactive_object_detection/fertilized-forests/examples/python to fertilized-forests/examples/python folder after installation.
⋅⋅* Run fertilized-forests/examples/python/hough_experiment.py for Active learning experiment.
⋅⋅* Run fertilized-forests/examples/python/hough_app.py Flask framework based web application for interactive detection. 

## Results

![](https://github.com/priyankavokuda/interactive_object_detection/blob/master/images/example_output.png)

Hough forest library from work [Lassner,C,Lienhart,R,2015]
[Lassner,C,Lienhart,R,2015] Lassner, C., & Lienhart, R. (2015, October). The fertilized forests decision forest library. In Proceedings of the 23rd ACM international conference on Multimedia (pp. 681-684). ACM.

The code is implemented from work [Yao,A,Gall,J,2012]

[J.Gall,2013] Yao, A., Gall, J., Leistner, C., & Van Gool, L. (2012, June). Interactive object detection. In Computer Vision and Pattern Recognition (CVPR), 2012 IEEE Conference on (pp. 3242-3249). IEEE.


