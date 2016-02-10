from conans import ConanFile, CMake
from conans import tools
import os

class netLinkConan(ConanFile):
    name = "netLink"
    version = "master"
    url = "https://github.com/Kaosumaru/conan-netLink"
    settings = "os", "compiler", "build_type", "arch"
    exports = "netLink/*"

    source_tgz = "https://github.com/Lichtso/netLink/archive/master.zip"

    def source(self):
        self.output.info("Downloading %s" % self.source_tgz)
        tools.download(self.source_tgz, "netLink.zip")
        tools.unzip("netLink.zip", ".")
        os.unlink("netLink.zip")

    def config(self):
        pass

    def build(self):
        cmake = CMake(self.settings)
        self.run('cd %s-master && mkdir build' % self.name)
        self.run('cd %s-master/build && cmake -DCMAKE_INSTALL_PREFIX:PATH=../../install .. %s' % (self.name, cmake.command_line))
        
        try:
            self.run("cd %s-master/build && cmake --build . --target install %s" % (self.name, cmake.build_config))
        except:
            self.run("cd %s-master/build && cmake --build . --target install %s" % (self.name, cmake.build_config)) #Don't know why, but second try passes
        

    def package(self):
        self.copy("*.lib", dst="lib", src="install/lib")
        self.copy("*.a", dst="lib", src="install/lib")
        self.copy("*.dll", dst="dll", src="install/lib")
        self.copy("*.h", dst="include/netLink", src="install/include/netLink")

    def package_info(self):
        self.cpp_info.libs = ["netLink"]
