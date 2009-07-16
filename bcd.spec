%define name bcd
%define version 0.6
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
Requires: perl-File-Copy-Recursive sudo urpmi
requires: cdrkit-genisoimage cdrkit-isotools syslinux
requires: gfxboot mandriva-gfxboot-theme drakxtools-backend
BuildArch: noarch


%description
Create Mandriva ISO
- configuration file is now in XML format
- use of genhdlist2 with file-deps
- support the add of isolinux entry
- change the theme on all.rdz files
- just need an input and an exclude file
- write media.cfg
- use input or exclude list for each media
- use custom rpmsrate of compssusers.pl
- all sub-media supported (updates, testing...)
- iso HEADER
- suggests option per media
- md5 in a file
- create a product.id file
- create a VERSION file
- support rpmsrate CAT


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
%doc README *.xml lists 
%{_bindir}/bcd
%{perl_vendorlib}/BCD
%{_mandir}/man1/*
