import rospy
from cv_bridge import CvBridge
import cv2
import os
from sensor_msgs.msg import Image

def publish():
    pub = rospy.Publisher('process_topic', Image, queue_size=10)
    rospy.init_node('img_pub_raw', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    bridge = CvBridge()

    images_dir = '../images'
    for filename in os.listdir(images_dir):
        f = os.path.join(images_dir, filename)
        cvimg = cv2.imread(f, cv2.IMREAD_COLOR)
        rosimg = bridge.cv2_to_imgmsg(cvimg, encoding="passthrough")
        pub.publish(rosimg)
        

if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass