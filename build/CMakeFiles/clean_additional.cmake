# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "ArmaExctractorGUI_autogen"
  "CMakeFiles/ArmaExctractorGUI_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/ArmaExctractorGUI_autogen.dir/ParseCache.txt"
  )
endif()
