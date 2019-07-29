#! /usr/bin/env python
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String
from std_msgs.msg import Float32
from PIL import Image
import subprocess


img_src = "/home/pi/catkin_ws/src/adhoc/img/"

p = None

def show_begin(message):
    if p is not None:
        p.kill()
    print("showing "+message.data)
    p = subprocess.Popen("display", img_src+message.data)

def show_final(message):
    if p is not None:
        p.kill()
    print("showing "+message.data)
    p = subprocess.Popen("display", img_src+message.data)

def show_waypoint(message):
    if p is not None:
        p.kill()
    waypoint_id = int(message.data)
    pic_id = waypoint_id + 7
    print("shwoing ad_h-c_swarms-"+picid+".png")
    p = subprocess.Popen("display", img_src+"ad_hoc_swarms-"+picid+".png")




if __name__=='__main__':
    rospy.init_node("display")
    
    begin_sub = rospy.Subscriber('/201907/ProjectBegin', callback=show_begin)
    finish_sub = rospy.Subscriber('/201907/ProjectFinal', callback=show_final)
    waypoint_sub = rospy.Subscriber('/201907/WayPointNum', callback=show_waypoint)

    while not rospy.is_shutdown():
        rospy.spin()
