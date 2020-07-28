
#include "libC/libC.h"

#include <iostream>
#include "libA/libA.h"

///////


void hello_libC(int indent, const std::string& msg) {
    std::cout << std::string(indent, ' ') << "libC: " << msg << std::endl;
    std::cout << "libB version 1.0" << std::endl;
    hello_libA(indent+1, "called from libC");
}