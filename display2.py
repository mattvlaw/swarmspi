#! /usr/bin/env python
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String
from std_msgs.msg import Float32
from PIL import Image
import subprocess


img_src = "/home/pi/catkin_ws/src/adhoc2/img/"

p = None
begin_flag = "" 
final_flag = "" 
waypoint_flag = 0
def show_begin(message):
    global p
    global begin_flag
    if begin_flag != message.data:
        if p is not None:
            p.kill()
        # if this is the one that says "follow me",
        # move the initial slides here to display, if
        # begin_flag == ""
        print("beginning by showing "+message.data)
        p = subprocess.Popen(["feh", "-F",img_src+message.data])
        begin_flag = message.data

def show_final(message):
    global p
    global final_flag
    if final_flag != message.data:
        if p is not None:
            p.kill()
        print("showing "+message.data)
        p = subprocess.Popen(["feh", "-F",img_src+message.data])
        final_flag = message.data

def show_waypoint(message):
    global p
    global waypoint_flag

    waypoint_id = int(message.data)
    if waypoint_id != waypoint_flag:
        if p is not None:
            p.kill()
        waypoint_flag = waypoint_id
       # if waypoint_id == 1:
           
        pic_id = waypoint_id + 7
        print("shwoing ad_h-c_swarms-"+str(pic_id)+".png")
        p = subprocess.Popen(["feh","-F", img_src+"ad_hoc_swarms-"+str(pic_id)+".png"])
    



if __name__=='__main__':
    rospy.init_node("display")
    print("starting the display node")    
    p = subprocess.Popen(["feh", "-F",img_src+"ad_hoc_swarms-1.png"])
    rospy.sleep(8)
    p.kill()
    p = subprocess.Popen(["feh", "-F",img_src+"ad_hoc_swarms-2.png"])
    rospy.sleep(8)
    p.kill()
    begin_sub = rospy.Subscriber('/201907/ProjectBegin', String, callback=show_begin)
    finish_sub = rospy.Subscriber('/201907/ProjectFinal', String, callback=show_final)
    waypoint_sub = rospy.Subscriber('/201907/WayPointNum', Float32, callback=show_waypoint)
    print("spinning")
    while not rospy.is_shutdown():
        rospy.spin()
