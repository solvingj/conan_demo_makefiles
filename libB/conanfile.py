from conans import ConanFile, tools

class LibB(ConanFile):
    name = "libB"
    version = "1.0"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    generators = "make"

    scm = {"type": "git",
           "url": "http://gitbucket/root/libB.git",
           "revision": "auto"}

    def requirements(self):
        self.requires("libA/1.0@mycompany/demo")

    def build(self):
        print("|-----------------------------------------|")
        print("|-------------   BUILDING   --------------|")
        print("|---------------   libB   ----------------|")
        print("|-----------------------------------------|")
        with tools.environment_append({"INCLUDE_MAKEFILE": "conanbuildinfo.mak"}):
            self.run("make %s" % ("shared" if self.options.shared else "static"))

    def package(self):
        self.copy("LICENSE", dst="licenses")
        self.copy("*.a", dst="lib", src="out")
        self.copy("*.so", dst="lib", src="out")
        self.copy("*.bin", dst="bin", src="out")
        self.copy("*.h", dst="include", src="include")

    def package_info(self):
        self.cpp_info.libs = ["B",]
