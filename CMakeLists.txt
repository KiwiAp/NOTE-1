cmake_minimum_required(VERSION 3.12)
project(new_project)

set(CMAKE_CXX_STANDARD 14)

# add multithread in clion(or : Undefined reference to pthread_create in Linux)
# https://stackoverflow.com/questions/1662909/undefined-reference-to-pthread-create-in-linux
# https://stackoverflow.com/questions/40702679/how-to-enable-multithreading-in-clion
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread")

#AUX_SOURCE_DIRECTORY(src DIR_SRCS)
#SET(TEST_MATH ${DIR_SRCS})
#include_directories(include)


add_executable(new_project main.cpp meeting.h)