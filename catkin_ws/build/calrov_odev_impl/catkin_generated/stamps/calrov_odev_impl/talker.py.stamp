import rospy
from cv_bridge import CvBridge
import cv2
import os
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    bridge = CvBridge()

    imgs = []
    images_dir = '../../../images'
    for filename in os.listdir('../../../images'):
        f = os.path.join(images_dir, filename)
        img = cv2.imread(f, cv2.IMREAD_COLOR)
        imgs.append(img)

    rospy.loginfo(imgs)
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass