PROJECT(ConanTest)
cmake_minimum_required(VERSION 3.0)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(ConanTest test.cpp)

TARGET_LINK_LIBRARIES(ConanTest ${CONAN_LIBS})
