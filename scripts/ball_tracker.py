import rospy
import numpy as np
import cv2
from copy import copy
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image

class BallTracker(object):
	def __init__(self):
		self.pub = rospy.Publisher("/ball_pos", Point, queue_size=10)
		self.im_pub = rospy.Publisher("/ball_highlight_image", Image, queue_size=10)
		self.sub = rospy.Subscriber("/camera/depth/image", Image, self.process_image)
		self.bridge = CvBridge()
	def process_image(self, image):
		#print "got image"
		try:
			cv_img = self.bridge.imgmsg_to_cv2(image)
		except CvBridgeError as e:
			print e
		(rows,cols) = cv_img.shape
		print "try 1"
		cv_img = cv2.medianBlur(cv_img, 5)
		#cv2.imshow("img",cv_img)
		#cv2.waitKey(1)
		print "try 2"
		cimg = cv2.cvtColor(cv_img, cv2.COLOR_GRAY2BGR)
		print cimg.shape
		print "try 3"
		cv_img = np.nan_to_num(cv_img)
		print cv_img
		print "MAX:", np.max(cv_img)
		print "MIN:", np.min(cv_img)
		print "TYPE:", type(cv_img)
		cv_img *= 255.0/cv_img.max()
		cv_img = np.clip(cv_img, 0, 255)
		circles = cv2.HoughCircles(cv_img.astype(np.uint8), cv2.HOUGH_GRADIENT, 2, 50, param1=30, param2=80, minRadius=20, maxRadius=130)
		print "try 4"
		circles = np.uint16(np.around(circles))
		print "try 5"
		for i in circles[0,:]:
			cv2.circle(cimg, (i[0],i[1]),i[2],(0,255,0),2)
			cv2.circle(cimg, (i[0],i[1]),2,(0,0,255),3)
		try:
			cv2.imshow("circles on image", cimg)
			cv2.waitKey(1)
			new_msg_img = self.bridge.cv2_to_imgmsg(cimg, "32FC3")
			self.im_pub.publish(new_msg_img)
		except CvBridgeError as e:
			print e
		
		


if __name__ == '__main__':
	try:
		rospy.init_node('kinect_ball_tracking')
		tracker =BallTracker()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
	finally:
		cv2.destroyAllWindows()
