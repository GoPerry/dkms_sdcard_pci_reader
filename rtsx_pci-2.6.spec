%{!?kversion: %define kversion %(uname -r)}

%define kmod_name rtsx_pci
%define module  rtsx_pci
%global dkms_name  rtsx_pci


Name:		rtsx_pci
Version:        v2.6
Release:        1%{?dist}
Summary:        Realtek PCI Interface Card Reader

Group:         System Environment/Kernel
License:       GPL
URL:           http://www.dell.com
Source0:       %{name}-%{version}.tar.gz
Source1:       dkms.conf
BuildArch:      noarch


BuildRequires:  gcc,tar
ExclusiveOS:    linux
Requires:       dkms 
Requires:       gcc, make, perl
Requires:       kernel-devel
Provides:       %{module}-kmod = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}/%{release}-root/

%description
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
This package contains the dkms kernel modules required to emulate
several interfaces provided by the Solaris kernel.


%prep
echo "pre start+++++++++++++++++++++++++++++++++++++++++++++++++++++"
pwd
rm -rf %{module}-%{version}
mkdir %{module}-%{version}
#%setup -q -n %{module}-%{version}
cd %{module}-%{version}
tar xzvf $RPM_SOURCE_DIR/%{module}-%{version}.tar.gz
echo "pre end+++++++++++++++++++++++++++++++++++++++++++++++++++++"

#mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

#pwd
#cp -rf %{name}-%{version}  /usr/src/
#cd %{buildroot}/%{_usrsrc}/%{dkms_name}-%{version}/
pwd 



#%build
#make %{?_smp_mflags}


%install
echo "install start+++++++++++++++++++++++++++++++++++++++++++++++++++++"
if [ "$RPM_BUILD_ROOT != /" ];then
	rm -rf $RPM_BUILD_ROOT
fi
mkdir -p $RPM_BUILD_ROOT/usr/src/%{module}-%{version}/
install -m 644 $RPM_SOURCE_DIR/%{module}-%{version}/dkms.conf   $RPM_BUILD_ROOT/usr/src/%{module}-%{version}
install -m 644 $RPM_SOURCE_DIR/%{module}-%{version}/*  $RPM_BUILD_ROOT/usr/src/%{module}-%{version}
#cd ${RPM_BUILD_DIR}
#cp -rf %{name}-%{version}/    %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
#cp -rf %{name}-%{version}  /usr/src/
#cd %{dkms_name}-%{version}/
pwd
#%make_install
#make  DESTDIR=$RPM_BUILD_ROOT install
echo "install end+++++++++++++++++++++++++++++++++++++++++++++++++++++"



%clean
#dkms remove  %{dkms_name}/%{version}  --all
if [ "$RPM_BUILD_ROOT != /" ];then
	rm -rf $RPM_BUILD_ROOT
fi

%post
dkms add -m %{name} -v %{version}  
dkms build -m %{name} -v %{version}  
dkms install -m %{name} -v %{version}  

%preun
dkms remove  -m %{name} -v %{version}  --all


%files
%defattr(0777,root,root,-)
%attr(0755,root,root)/usr/src/%{module}-%{version}


%changelog

