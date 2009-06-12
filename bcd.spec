%define name bcd
%define version 0.1
%define release %mkrel 1

Summary: Tool to build Mandriva ISO
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Configuration/Packaging
Url: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/build_system/bcd
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: perl-File-Copy sudo urpmi
BuildArch: noarch


%description
Create Mandriva ISO
- configuration file is now in XML format
- use of genhdlist2 with file-deps
- support the add of isolinux entry
- change the theme on all.rdz files
- just need an input and an exclude file
- write media.cfg
- use custom rpmsrate of compssusers.pl
- all sub-media supported (updates, testing...)
- iso HEADER
- md5 in a file
- create a product.id file
- create a VERSION file


%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make install PREFIX=$RPM_BUILD_ROOT


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README bcd.xml exclude input
%{_bindir}/bcd
%{perl_vendorlib}/bcd

