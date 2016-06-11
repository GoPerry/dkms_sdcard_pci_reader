#include config.mk

CONFIG_MFD_RTSX_PCI = m
MOD_NAME = rtsx_pci
KVERSION:= $(shell uname -r)
MDIR = kernel/drivers/mfd
obj-$(CONFIG_MFD_RTSX_PCI) := $(MOD_NAME).o
$(MOD_NAME)-objs := rtsx_pcr.o \
		rtsx_gops.o \
		rts5229.o \
		rts5227.o \
		rts5249.o \
					
ccflags-y := -I$(src)/include
#ccflags-y += -DDBG -DRT3298 -DRTBT_IFACE_PCI -DLINUX

MAKE = make
LINUX_SRC ?= /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

all:
	$(MAKE) -C $(LINUX_SRC) M=$(PWD) modules

clean:
	$(MAKE) -C $(LINUX_SRC) M=$(PWD) clean

install:
	$(MAKE) INSTALL_MOD_PATH=$(DESTDIR) INSTALL_MOD_DIR=$(MDIR) \
		-C $(LINUX_SRC) M=$(PWD) modules_install
	depmod -a
	#three lines commented for dkms arch linux package: it autoinstalls the module
	install -m 0755 -o root -g root  rtsx_pci.ko $(DESTDIR)/lib/modules/$(shell uname -r)/kernel/drivers/mfd/
	#install -m 0755 -o root -g root tools/rtbt $(DESTDIR)/usr/bin/

	
