-include $(INCLUDE_MAKEFILE)
OUT_DIR ?= out

PROJECT_NAME = libC
EXE_FILENAME = $(PROJECT_NAME).bin
STATIC_LIB_FILENAME = $(PROJECT_NAME).a
SHARED_LIB_FILENAME = $(PROJECT_NAME).so

SRC_DIR       += src
INCLUDE_DIRS  += include
DEFINES       += 
LIBS          += 
SYSTEM_LIBS   += 
LIB_DIRS      += 
CFLAGS        += 
CXXFLAGS      += 
LDFLAGS       += 

CPPFLAGS           += $(addprefix -I,$(CONAN_INCLUDE_DIRS))
CPPFLAGS           += $(addprefix -D,$(CONAN_DEFINES))
LDFLAGS            += $(addprefix -l,$(CONAN_LIBS))
LDFLAGS            += $(addprefix -l,$(CONAN_SYSTEM_LIBS))
LDFLAGS            += $(addprefix -L,$(CONAN_LIB_DIRS))
CFLAGS             += $(CONAN_CFLAGS)
CXXFLAGS           += $(CONAN_CXXFLAGS)
LDFLAGS            += $(CONAN_LDFLAGS)

SRCS = $(wildcard $(SRC_DIR)/*.cpp)
OBJS = $(patsubst $(SRC_DIR)/%.cpp,$(OUT_DIR)/%.o,$(SRCS))

$(info >> SRCS: $(SRCS))
$(info >> OBJS: $(OBJS))
$(info >> CFLAGS: $(CFLAGS))
$(info >> CXXFLAGS: $(CXXFLAGS))
$(info >> LDFLAGS: $(LDFLAGS))
$(info >> CPPFLAGS: $(CPPFLAGS))

$(info >> OUT_DIR: $(OUT_DIR))
$(info >> PROJECT_NAME: $(PROJECT_NAME))
$(info >> EXE_FILENAME: $(EXE_FILENAME))
$(info >> STATIC_LIB_FILENAME: $(STATIC_LIB_FILENAME))
$(info >> SHARED_LIB_FILENAME: $(SHARED_LIB_FILENAME))

.PHONY               : exe static shared clean all

all                  : static

clean                : 
	-rm -rf $(OUT_DIR)/*

exe                  : $(OBJS)
	$(CXX) $(OBJS) $(LDFLAGS) -o $(OUT_DIR)/$(EXE_FILENAME)

static               : $(OBJS)
	$(AR) $(ARFLAGS) $(OUT_DIR)/$(STATIC_LIB_FILENAME) $(OBJS)

shared               : $(OBJS)
	$(CXX) $(OBJS) $(LDFLAGS) -o $(OUT_DIR)/$(SHARED_LIB_FILENAME)

$(OUT_DIR)/%.o       : $(SRC_DIR)/%.cpp $(OUT_DIR)
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) -c $< -o $@

$(OUT_DIR):
	-mkdir $@