%bcond_with	pdf

Summary:	Tool to build Mandriva ISO
Name:		bcd
Version:	3.7
Release:	1
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/build_system/bcd
Requires:	perl-File-Copy-Recursive sudo urpmi perl-Parallel-ForkManager
Requires:	cdrkit-genisoimage cdrkit-isotools syslinux
Requires:	gfxboot mandriva-gfxboot-theme drakxtools-backend rpmcheck rpmtools
%if %{with pdf}
Buildrequires:	perl-LaTeX-Driver perl-Class-Accessor texlive-collection-fontsextra
%endif
BuildArch:	noarch


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
%if %{with pdf}
%make pdf
%endif

%install
%make install PREFIX=$RPM_BUILD_ROOT

%files
%doc README *.xml lists create_dual.sh
%if %{with pdf}
%doc doc/*.pdf
%endif
%{_bindir}/bcd
%{_bindir}/*.pl
%{perl_vendorlib}/BCD
%{perl_vendorlib}/%{name}.pod
%{_mandir}/man1/*
