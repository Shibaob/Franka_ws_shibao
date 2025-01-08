# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "realsense_demo: 0 messages, 1 services")

set(MSG_I_FLAGS "")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(realsense_demo_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv" NAME_WE)
add_custom_target(_realsense_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "realsense_demo" "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(realsense_demo
  "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/realsense_demo
)

### Generating Module File
_generate_module_cpp(realsense_demo
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/realsense_demo
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(realsense_demo_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(realsense_demo_generate_messages realsense_demo_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv" NAME_WE)
add_dependencies(realsense_demo_generate_messages_cpp _realsense_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_demo_gencpp)
add_dependencies(realsense_demo_gencpp realsense_demo_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_demo_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(realsense_demo
  "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/realsense_demo
)

### Generating Module File
_generate_module_eus(realsense_demo
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/realsense_demo
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(realsense_demo_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(realsense_demo_generate_messages realsense_demo_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv" NAME_WE)
add_dependencies(realsense_demo_generate_messages_eus _realsense_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_demo_geneus)
add_dependencies(realsense_demo_geneus realsense_demo_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_demo_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(realsense_demo
  "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/realsense_demo
)

### Generating Module File
_generate_module_lisp(realsense_demo
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/realsense_demo
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(realsense_demo_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(realsense_demo_generate_messages realsense_demo_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv" NAME_WE)
add_dependencies(realsense_demo_generate_messages_lisp _realsense_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_demo_genlisp)
add_dependencies(realsense_demo_genlisp realsense_demo_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_demo_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(realsense_demo
  "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/realsense_demo
)

### Generating Module File
_generate_module_nodejs(realsense_demo
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/realsense_demo
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(realsense_demo_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(realsense_demo_generate_messages realsense_demo_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv" NAME_WE)
add_dependencies(realsense_demo_generate_messages_nodejs _realsense_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_demo_gennodejs)
add_dependencies(realsense_demo_gennodejs realsense_demo_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_demo_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(realsense_demo
  "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_demo
)

### Generating Module File
_generate_module_py(realsense_demo
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_demo
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(realsense_demo_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(realsense_demo_generate_messages realsense_demo_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bobyung/MPs_ws/src/realsense_demo/srv/ExecuteTrajectory.srv" NAME_WE)
add_dependencies(realsense_demo_generate_messages_py _realsense_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_demo_genpy)
add_dependencies(realsense_demo_genpy realsense_demo_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_demo_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/realsense_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/realsense_demo
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/realsense_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/realsense_demo
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/realsense_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/realsense_demo
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/realsense_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/realsense_demo
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_demo)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_demo\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_demo
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
