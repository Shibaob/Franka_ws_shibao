#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/bobyung/MPs_ws/src/srdfdom"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/bobyung/MPs_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/bobyung/MPs_ws/install/lib/python3/dist-packages:/home/bobyung/MPs_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/bobyung/MPs_ws/build" \
    "/usr/bin/python3" \
    "/home/bobyung/MPs_ws/src/srdfdom/setup.py" \
    egg_info --egg-base /home/bobyung/MPs_ws/build/srdfdom \
    build --build-base "/home/bobyung/MPs_ws/build/srdfdom" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/bobyung/MPs_ws/install" --install-scripts="/home/bobyung/MPs_ws/install/bin"
