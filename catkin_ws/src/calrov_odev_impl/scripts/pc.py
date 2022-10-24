
from typing import Any, List, Tuple
import rospy
import os
import threading
import cv2
import numpy as np
import time
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs import String
from numpy_ros import to_message
lock = threading.Lock()

def callback(data, args: Tuple[Any, CvBridge, List[str], rospy.Publisher]):
    lock.acquire()
    (net, bridge, classes) = args
    cv_img = bridge.imgmsg_to_cv2(data)
    blob: np.ndarray = cv2.dnn.blobFromImage(cv_img, 1/255.0, (416, 416), (0,0,0), True)
    net.setInput(blob)
    out = net.forward()
    

    
def listener():
    net = cv2.dnn.readNet("../ai/yolov4-tiny.cfg", "../ai/yolov4-tiny.weights")
    bridge = CvBridge()
    pub = rospy.Publisher("ai_result", String)
    classes = None
    with open('../ai/coco.names', 'r') as classes_file:
        classes = classes_file.readlines()
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('pc', anonymous=True)
    rospy.Subscriber("img_proc", Image, callback, (net, bridge, classes))

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()