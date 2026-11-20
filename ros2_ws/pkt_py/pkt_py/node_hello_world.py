#!/usr/bin/env python3
import rclpy                 # ROS2 python接口库
from rclpy.node import Node  # 引入 ROS2 节点类
import time

"""
创建一个HelloWorld节点，初始化时输出HelloWorld日志
"""
class HelloWorldNode(Node):
    def __init__(self, name):
        super().__init__(name)                      # ROS2 节点父类初始化
        while rclpy.ok():                           # ROS2 系统是否正常运行
            self.get_logger().info("Hello World")   # ROS2 日志输出
            time.sleep(0.5)                         # 休眠控制循环时间

def main(args=None):                                # ROS2 节点主入口main函数
    rclpy.init(args=args)                           # ROS2 Python接口初始化
    node = HelloWorldNode("node_helloworld")        # 创建 ROS2 节点对象
    rclpy.spin(node)                                # 循环等待 ROS2 退出
    node.destroy_node()                             # 销毁节点实例
    rclpy.shutdown()                                # 关闭 ROS2 Python接口