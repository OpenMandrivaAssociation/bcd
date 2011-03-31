%define name bcd
%define version 3.5
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
Requires: perl-File-Copy-Recursive sudo urpmi perl-Parallel-ForkManager
requires: cdrkit-genisoimage cdrkit-isotools syslinux
requires: gfxboot mandriva-gfxboot-theme drakxtools-backend rpmcheck
Buildrequires:	perl-LaTeX-Driver perl-Class-Accessor
BuildArch: noarch


%description
Create Mandriva ISO
- configuration file is now in XML format
- use of genhdlist2 with file-deps
- support the add of isolinux entry
- change the theme on all.rdz files
- just need an input and an exclude file per media
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
%make

%install
rm -rf %{buildroot}
%make pdf
%make install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README *.xml lists create_dual.sh doc/*.pdf
%{_bindir}/bcd
%{_bindir}/*.pl
%{perl_vendorlib}/BCD
%{perl_vendorlib}/%name.pod
%{_mandir}/man1/*
