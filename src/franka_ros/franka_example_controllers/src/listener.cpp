#include <ros/ros.h>
#include <franka_example_controllers/JointTorqueComparison.h>
using namespace std;
/*
//将接收到的消息打印
void chattercallback(const franka_example_controllers::JointTorqueComparison& msg)
{
//将接收到的消息打印出来
//ROS_INFO("The imformation of control and state",msg);
std::cout<<"1";

}
int main(int argc,char **argv)
{
//初始化节点
ros::init(argc,argv,"listener");
//创建节点句柄
ros::NodeHandle n;
//创建一个subscriber,订阅话题，注册回调函数
ros::Subscriber sub=n.subscribe("/joint_impedance_example_controller/torque_comparison",1000,chattercallback);
//循环等待回调函数
ros::spin();
return 0;
}
*/

//回调函数部分
void chatterCallback(const franka_example_controllers::JointTorqueComparison& msg)

{
   //std::cout<<"1"; //将接收到的消息打印出来
/*
    std::cout <<"mass :" << mass<< std::endl
                    << "tau_commanded [Nm]: " << tau_d_actual << std::endl
                    << "tau_measured [Nm]: " << print_data.robot_state.tau_J << std::endl
                    << "root mean square of tau_error [Nm]: " << error_rms << std::endl
                    << "-----------------------" << std::endl;




     for (size_t i = 0; i < 7; ++i) 
    {
      torques_publisher_.msg_.tau_commanded[i] = last_tau_d_[i];
      torques_publisher_.msg_.tau_error[i] = tau_error[i];
      torques_publisher_.msg_.tau_measured[i] = tau_j[i];
      torques_publisher_.msg_.q[i]= robot_state.q[i];
      torques_publisher_.msg_.q_d[i]= robot_state.q_d[i];
      torques_publisher_.msg_.dq[i]= dq_filtered_[i];
      torques_publisher_.msg_.dq_d[i]= robot_state.dq_d[i];
      torques_publisher_.msg_.ddq_d[i]= robot_state.ddq_d[i];
      torques_publisher_.msg_.coriolis[i]= coriolis[i];
      torques_publisher_.msg_.gravity[i]= gravity[i];
      torques_publisher_.msg_.u[i]=  robot_state.q[i];
    }
    for (int i=0;i<48;++i)
    {
      torques_publisher_.msg_.mass [i]= mass[i];
    }
    
    ROS_INFO_STREAM("mass :" << mass);   
    ROS_INFO_STREAM("coriolis: " << coriolis);
    ROS_INFO_STREAM("gravity :" << gravity);
    ROS_INFO_STREAM("q:" << robot_state.q);
    ROS_INFO_STREAM("qd: " << robot_state.q_d);
    ROS_INFO_STREAM("dq:" << dq_filtered_);
    ROS_INFO_STREAM("dqd: " << robot_state.dq_d);
    ROS_INFO_STREAM("ddqd: " << robot_state.ddq_d);
*/
//回调函数部分
/*
  template <class T, size_t N>
std::ostream& operator<<(std::ostream& ostream, const std::array<T, N>& array) {
  ostream << "[";
  std::copy(array.cbegin(), array.cend() - 1, std::ostream_iterator<T>(ostream, ","));
  std::copy(array.cend() - 1, array.cend(), std::ostream_iterator<T>(ostream));
  ostream << "]";
  return ostream;
}
*/

/*
std::array<double, 49> Mass=msg.mass;
std::array<double, 7> Cor=msg.coriolis;
std::array<double, 7> gr=msg. gravity
std::array<double, 7> Q=msg.q
std::array<double, 7> Qd=msg.q_d
std::array<double, 7> DQ= msg.d_filtered_;
std::array<double, 7> Dqd=msg.dq_d;
std::array<double, 7> Ddqd=msg.ddq_d;
std::array<double, 7> U=msg.u;
*/
   // ROS_INFO_STREAM("mass :"  );   printarray(const std::array<double, 49>  &Mass,49);
    /*
    ROS_INFO_STREAM("coriolis: "  );printarray(Cor,7);
    ROS_INFO_STREAM("gravity :" );printarray(gr,7);
    ROS_INFO_STREAM("q:" );printarray(Q, 7);
    ROS_INFO_STREAM("qd: " );printarray(Qd, 7);
    ROS_INFO_STREAM("dq:");printarray(DQ, 7);
    ROS_INFO_STREAM("dqd: " );printarray(Dqd, 7);
    ROS_INFO_STREAM("ddqd: ");printarray(Ddqd, 7);
ROS_INFO_STREAM("ddqd: ");printarray(U, 7);
*/
//模型
   ROS_INFO("mass:");
   for (int i = 0; i < 49; ++i)
{
cout << msg.mass[i] ;
}

ROS_INFO("coriolis:");
   for (int i = 0; i < 7; ++i)
{
cout << msg.coriolis[i] ;
}

 ROS_INFO("gravity :");
for (int i = 0; i < 7; ++i)
{
cout << msg.gravity[i] ;
}

// //状态
 ROS_INFO("q :");
for (int i = 0; i < 7; ++i)
{
cout << msg.q[i] ;
}

 ROS_INFO("qd :");
for (int i = 0; i < 7; ++i)
{
cout << msg.q_d[i] ;
}

ROS_INFO("dq :");
for (int i = 0; i < 7; ++i)
{
cout << msg.dq[i] ;
}

ROS_INFO("dqd :");
for (int i = 0; i < 7; ++i)
{
cout << msg.dq_d[i] ;
}

ROS_INFO("ddqd :");
for (int i = 0; i < 7; ++i)
{
cout << msg.ddq_d[i] ;}
// }
ROS_INFO("time :");
cout<< msg.Time;
// }

}


int main(int argc, char **argv){
    ros::init(argc, argv, "listener"); //初始化ROS节点
    ros::NodeHandle n; //创建句柄节点
    ros::Subscriber sub = n.subscribe("/joint_impedance_example_controller/torque_comparison", 1, chatterCallback);
    ros::spin();
    return 0;
}




