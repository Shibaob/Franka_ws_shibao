
(cl:in-package :asdf)

(defsystem "realsense_demo-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ExecuteTrajectory" :depends-on ("_package_ExecuteTrajectory"))
    (:file "_package_ExecuteTrajectory" :depends-on ("_package"))
  ))