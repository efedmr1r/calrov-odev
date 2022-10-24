# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/usr/src/googletest/googlemock"
  "/home/thunderstorm010/calrov-odev/catkin_ws/build/gmock"
  "/home/thunderstorm010/calrov-odev/catkin_ws/build/GMock-prefix"
  "/home/thunderstorm010/calrov-odev/catkin_ws/build/GMock-prefix/tmp"
  "/home/thunderstorm010/calrov-odev/catkin_ws/build/GMock-prefix/src/GMock-stamp"
  "/home/thunderstorm010/calrov-odev/catkin_ws/build/GMock-prefix/src"
  "/home/thunderstorm010/calrov-odev/catkin_ws/build/GMock-prefix/src/GMock-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/thunderstorm010/calrov-odev/catkin_ws/build/GMock-prefix/src/GMock-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/thunderstorm010/calrov-odev/catkin_ws/build/GMock-prefix/src/GMock-stamp${cfgdir}") # cfgdir has leading slash
endif()
