import rospy
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image
import numpy as np
import cv2

class BallTracker(object):
	def __init__(self):
		self.pub = rospy.Publisher("/ball_pos", Point, queue_size=10)
		self.sub = rospy.Subscriber("/camera/depth/image", Image, self.process_image)
	def process_image(self, image):
		print "got image"
		


if __name__ == '__main__':
	try:
		rospy.init_node('kinect_ball_tracking')
		tracker =BallTracker()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
