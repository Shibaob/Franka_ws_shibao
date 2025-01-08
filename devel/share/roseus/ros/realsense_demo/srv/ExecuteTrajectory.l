;; Auto-generated. Do not edit!


(when (boundp 'realsense_demo::ExecuteTrajectory)
  (if (not (find-package "REALSENSE_DEMO"))
    (make-package "REALSENSE_DEMO"))
  (shadow 'ExecuteTrajectory (find-package "REALSENSE_DEMO")))
(unless (find-package "REALSENSE_DEMO::EXECUTETRAJECTORY")
  (make-package "REALSENSE_DEMO::EXECUTETRAJECTORY"))
(unless (find-package "REALSENSE_DEMO::EXECUTETRAJECTORYREQUEST")
  (make-package "REALSENSE_DEMO::EXECUTETRAJECTORYREQUEST"))
(unless (find-package "REALSENSE_DEMO::EXECUTETRAJECTORYRESPONSE")
  (make-package "REALSENSE_DEMO::EXECUTETRAJECTORYRESPONSE"))

(in-package "ROS")





(defclass realsense_demo::ExecuteTrajectoryRequest
  :super ros::object
  :slots (_index ))

(defmethod realsense_demo::ExecuteTrajectoryRequest
  (:init
   (&key
    ((:index __index) 0)
    )
   (send-super :init)
   (setq _index (round __index))
   self)
  (:index
   (&optional __index)
   (if __index (setq _index __index)) _index)
  (:serialization-length
   ()
   (+
    ;; uint8 _index
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _index
       (write-byte _index s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _index
     (setq _index (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass realsense_demo::ExecuteTrajectoryResponse
  :super ros::object
  :slots (_result ))

(defmethod realsense_demo::ExecuteTrajectoryResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional (__result :null))
   (if (not (eq __result :null)) (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass realsense_demo::ExecuteTrajectory
  :super ros::object
  :slots ())

(setf (get realsense_demo::ExecuteTrajectory :md5sum-) "36a44f45282f917780a89bd95d2a9827")
(setf (get realsense_demo::ExecuteTrajectory :datatype-) "realsense_demo/ExecuteTrajectory")
(setf (get realsense_demo::ExecuteTrajectory :request) realsense_demo::ExecuteTrajectoryRequest)
(setf (get realsense_demo::ExecuteTrajectory :response) realsense_demo::ExecuteTrajectoryResponse)

(defmethod realsense_demo::ExecuteTrajectoryRequest
  (:response () (instance realsense_demo::ExecuteTrajectoryResponse :init)))

(setf (get realsense_demo::ExecuteTrajectoryRequest :md5sum-) "36a44f45282f917780a89bd95d2a9827")
(setf (get realsense_demo::ExecuteTrajectoryRequest :datatype-) "realsense_demo/ExecuteTrajectoryRequest")
(setf (get realsense_demo::ExecuteTrajectoryRequest :definition-)
      "uint8 index
---
bool result
")

(setf (get realsense_demo::ExecuteTrajectoryResponse :md5sum-) "36a44f45282f917780a89bd95d2a9827")
(setf (get realsense_demo::ExecuteTrajectoryResponse :datatype-) "realsense_demo/ExecuteTrajectoryResponse")
(setf (get realsense_demo::ExecuteTrajectoryResponse :definition-)
      "uint8 index
---
bool result
")



(provide :realsense_demo/ExecuteTrajectory "36a44f45282f917780a89bd95d2a9827")


