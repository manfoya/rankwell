cmake_minimum_required(VERSION 3.20)

project(rankwell LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# L'exécutable doit finir dans build/pagerank_cpp (chemin utilisé par pagerank_cpp.py).
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

find_package(Threads REQUIRED)

add_executable(pagerank_cpp
    cpp/src/main.cpp
    cpp/src/csr_matrix.cpp
    cpp/src/pagerank.cpp
)

target_include_directories(pagerank_cpp PRIVATE cpp/include)
target_link_libraries(pagerank_cpp PRIVATE Threads::Threads)

# OpenMP est optionnel : le squelette doit aussi compiler avec std::thread seul.
find_package(OpenMP QUIET)
if(OpenMP_CXX_FOUND)
    target_link_libraries(pagerank_cpp PRIVATE OpenMP::OpenMP_CXX)
    target_compile_definitions(pagerank_cpp PRIVATE RANKWELL_USE_OPENMP)
endif()
