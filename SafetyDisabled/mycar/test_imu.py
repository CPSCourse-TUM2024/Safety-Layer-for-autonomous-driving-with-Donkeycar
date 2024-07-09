import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped

def imucallback(msg):
    print(msg)

rospy.init_node('listener', anonymous=True)
rospy.Subscriber("/odom_combined", PoseWithCovarianceStamped, imucallback)
print("I am here")
rospy.spin()