
#include <iostream>

#include "libB/libB.h"
#include "libC/libC.h"
/////

int main() {
    std::cout << "App: v1.0" << std::endl;
    hello_libB(1, "called from App");
    hello_libC(1, "called from App");    
    return 0;
}