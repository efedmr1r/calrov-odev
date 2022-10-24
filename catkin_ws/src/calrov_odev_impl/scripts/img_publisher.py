import rospy
from cv_bridge import CvBridge
import cv2
import os
from sensor_msgs.msg import Image
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', Image, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    bridge = CvBridge()

    imgs = []
    images_dir = '../images'
    for filename in os.listdir(images_dir):
        f = os.path.join(images_dir, filename)
        cvimg = cv2.imread(f, cv2.IMREAD_COLOR)
        rosimg = bridge.cv2_to_imgmsg(cvimg, encoding="passthrough")
        imgs.append(rosimg)

    rospy.loginfo(imgs)
    
    for img in imgs:
        pub.publish(img)
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass