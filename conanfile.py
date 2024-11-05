from conan import ConanFile
#from conan.tools.cmake import CMake, CMakeToolchain
#from conan.tools.layout import basic_layout
import os

class LibVPXConan(ConanFile):
    name = "libvpx"
    version = "1.14.1"
    license = "BSD-2-Clause"
    url = "https://github.com/webmproject/libvpx"
    description = "A video codec library for VP8 and VP9."
    settings = "os", "arch", "compiler", "build_type"
    generators = "AutotoolsDeps"
   #exports_sources = "CMakeLists.txt"
   #build_requires = "cmake/3.30.5"  # Specify the version of CMake if necessary

    def source (self):
        # Download and extract libvpx source
        self.run("git clone --branch v1.14.1 https://chromium.googlesource.com/webm/libvpx.git .")

    def build(self):
        # Run the configure script directly
        self.run(f"./configure --prefix={self.package_folder} --disable-examples --disable-unit-tests")

        # Run make with the appropriate number of processors
        self.run("make -j$(nproc)")

    def package(self):
        # Install the library files to the package folder
        self.run("make install")

    def package_info(self):
        # Specify the name of the library
        self.cpp_info.libs = ["vpx"]
