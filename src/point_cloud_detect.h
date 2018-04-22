#include <ros/ros.h>
/* PCL specific includes */
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

class PointCloudFilter
{
	public:
		void callback(const sensor_msgs::PointCloud2Ptr&);
		ros::Publisher pub;
};

