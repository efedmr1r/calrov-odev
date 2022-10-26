import rospy
from cv_bridge import CvBridge
import cv2
import os
from std_msgs.msg import String
from sensor_msgs.msg import Image

def process_ai_result(data):
    rospy.loginfo(f"Received from AI: {data}, drawing and saving to image...")
    # TODO
    pass    

def publish():
    pub = rospy.Publisher('img_proc', Image, queue_size=10)
    rospy.init_node('robot', anonymous=True)

    bridge = CvBridge()

    images_dir = '../images'
    for filename in os.listdir(images_dir):
        f = os.path.join(images_dir, filename)
        cvimg = cv2.imread(f)
        rosimg = bridge.cv2_to_imgmsg(cvimg, encoding="passthrough")
        pub.publish(rosimg)

    sub = rospy.Subscriber('ai_result', String, process_ai_result)

    rospy.spin()
        

if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass