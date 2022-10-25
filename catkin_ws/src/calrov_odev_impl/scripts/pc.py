
from typing import Any, List, Tuple
import rospy
import os
import threading
import cv2
import numpy as np
import time
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String

# lock = threading.Lock()

def callback(data, args: Tuple[Any, CvBridge, List[str], rospy.Publisher]):
    (net, bridge, classes, pub) = args
    cv_img = bridge.imgmsg_to_cv2(data)
    blob: np.ndarray = cv2.dnn.blobFromImage(cv_img, 1/255.0, (416, 416), (0,0,0), True)
    net.setInput(blob)
    out = net.forward()
    mapped_out = "TODO" # TODO somehow extract data from out to mapped_out
    pub.publish(mapped_out)

    
def listener():
    net = cv2.dnn.readNet("../ai/yolov4-tiny.cfg", "../ai/yolov4-tiny.weights")
    bridge = CvBridge()
    pub = rospy.Publisher("ai_result", String, queue_size=10)
    classes = None
    with open('../ai/coco.names', 'r') as classes_file:
        classes = classes_file.readlines()
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('pc', anonymous=True)
    rospy.Subscriber("img_proc", Image, callback, (net, bridge, classes, pub))

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()