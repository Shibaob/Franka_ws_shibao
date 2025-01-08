; Auto-generated. Do not edit!


(cl:in-package realsense_demo-srv)


;//! \htmlinclude ExecuteTrajectory-request.msg.html

(cl:defclass <ExecuteTrajectory-request> (roslisp-msg-protocol:ros-message)
  ((index
    :reader index
    :initarg :index
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ExecuteTrajectory-request (<ExecuteTrajectory-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExecuteTrajectory-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExecuteTrajectory-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name realsense_demo-srv:<ExecuteTrajectory-request> is deprecated: use realsense_demo-srv:ExecuteTrajectory-request instead.")))

(cl:ensure-generic-function 'index-val :lambda-list '(m))
(cl:defmethod index-val ((m <ExecuteTrajectory-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader realsense_demo-srv:index-val is deprecated.  Use realsense_demo-srv:index instead.")
  (index m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExecuteTrajectory-request>) ostream)
  "Serializes a message object of type '<ExecuteTrajectory-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'index)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExecuteTrajectory-request>) istream)
  "Deserializes a message object of type '<ExecuteTrajectory-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'index)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExecuteTrajectory-request>)))
  "Returns string type for a service object of type '<ExecuteTrajectory-request>"
  "realsense_demo/ExecuteTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteTrajectory-request)))
  "Returns string type for a service object of type 'ExecuteTrajectory-request"
  "realsense_demo/ExecuteTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExecuteTrajectory-request>)))
  "Returns md5sum for a message object of type '<ExecuteTrajectory-request>"
  "36a44f45282f917780a89bd95d2a9827")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExecuteTrajectory-request)))
  "Returns md5sum for a message object of type 'ExecuteTrajectory-request"
  "36a44f45282f917780a89bd95d2a9827")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExecuteTrajectory-request>)))
  "Returns full string definition for message of type '<ExecuteTrajectory-request>"
  (cl:format cl:nil "uint8 index~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExecuteTrajectory-request)))
  "Returns full string definition for message of type 'ExecuteTrajectory-request"
  (cl:format cl:nil "uint8 index~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExecuteTrajectory-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExecuteTrajectory-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ExecuteTrajectory-request
    (cl:cons ':index (index msg))
))
;//! \htmlinclude ExecuteTrajectory-response.msg.html

(cl:defclass <ExecuteTrajectory-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ExecuteTrajectory-response (<ExecuteTrajectory-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExecuteTrajectory-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExecuteTrajectory-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name realsense_demo-srv:<ExecuteTrajectory-response> is deprecated: use realsense_demo-srv:ExecuteTrajectory-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <ExecuteTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader realsense_demo-srv:result-val is deprecated.  Use realsense_demo-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExecuteTrajectory-response>) ostream)
  "Serializes a message object of type '<ExecuteTrajectory-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExecuteTrajectory-response>) istream)
  "Deserializes a message object of type '<ExecuteTrajectory-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExecuteTrajectory-response>)))
  "Returns string type for a service object of type '<ExecuteTrajectory-response>"
  "realsense_demo/ExecuteTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteTrajectory-response)))
  "Returns string type for a service object of type 'ExecuteTrajectory-response"
  "realsense_demo/ExecuteTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExecuteTrajectory-response>)))
  "Returns md5sum for a message object of type '<ExecuteTrajectory-response>"
  "36a44f45282f917780a89bd95d2a9827")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExecuteTrajectory-response)))
  "Returns md5sum for a message object of type 'ExecuteTrajectory-response"
  "36a44f45282f917780a89bd95d2a9827")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExecuteTrajectory-response>)))
  "Returns full string definition for message of type '<ExecuteTrajectory-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExecuteTrajectory-response)))
  "Returns full string definition for message of type 'ExecuteTrajectory-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExecuteTrajectory-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExecuteTrajectory-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ExecuteTrajectory-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ExecuteTrajectory)))
  'ExecuteTrajectory-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ExecuteTrajectory)))
  'ExecuteTrajectory-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteTrajectory)))
  "Returns string type for a service object of type '<ExecuteTrajectory>"
  "realsense_demo/ExecuteTrajectory")