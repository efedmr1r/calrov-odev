from typing import List
import rospy
import os
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import String

net = None
classes: List[str]
bridge: CvBridge

def abspath(path: str):
    return os.path.abspath(path)

def setup():
    net = cv2.dnn.readNet(abspath("../ai/yolov4-tiny.cfg"), abspath("../ai/yolov4-tiny.weights"))
    bridge = CvBridge()
    with open('../ai/coco.names', 'r') as classes_file:
        classes = [name.split(',')[0] for name in classes_file.read().split('\n')]

def callback(data):
    cv_img = bridge.imgmsg_to_cv2(data)
    cv2.imshow("img preview", cv_img)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    setup()
    listener()