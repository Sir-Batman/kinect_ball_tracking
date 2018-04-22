#include "point_cloud_detect.h"
#include <iostream>

void PointCloudFilter::callback(const sensor_msgs::PointCloud2Ptr& msg)
{
	std::cout << "callback hit" << std::endl;
	sensor_msgs::PointCloud2 output_msg;
	output_msg = *msg;
	pub.publish(output_msg);
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "point_cloud_filter");
	ros::NodeHandle n;
	PointCloudFilter pcf;

	pcf.pub = n.advertise<sensor_msgs::PointCloud2>("/filtered_point_cloud", 10);
	ros::Subscriber point_sub = n.subscribe("/camera/depth/points", 100, &PointCloudFilter::callback, &pcf);
	ros::spin();


	return EXIT_SUCCESS;
}
