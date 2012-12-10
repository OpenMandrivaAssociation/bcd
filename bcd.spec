%bcond_with	pdf

Summary:	Tool to build Mandriva ISO
Name:		bcd
Version:	3.7
Release:	2
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/build_system/bcd
Requires:	perl-File-Copy-Recursive sudo urpmi perl-Parallel-ForkManager
Requires:	cdrkit-genisoimage cdrkit-isotools syslinux
Requires:	gfxboot mandriva-gfxboot-theme drakxtools-backend rpmtools
Suggests:	rpmcheck smart
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


%changelog
* Fri Jun 08 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.7-2
+ Revision: 803637
- turn 'rpmcheck' dependency into a suggests
- add 'smart' to suggests

* Fri Jun 08 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.7-1
+ Revision: 803349
- disable build of pdf doc for now..
- new version:
  	o update configuration for Mandriva Linux 2012 Tech Prewview
  	o fix creation of $chroot_path/etc/profile.d/99info.sh as non-root
  	o add support for explicitly specifying rpmcheck or smartcheck
  	o fix isohybrid option
  	o speed up urpmi with '--fastunsafe'
- build pdf in %%build, not %%install
- add buildrequires on texlive-collection-fontsextra
- add version to license
- cleanups
- update to latest from svn

  + Antoine Ginies <aginies@mandriva.com>
    - add rpmtools requires

* Thu Mar 31 2011 Antoine Ginies <aginies@mandriva.com> 3.5-1
+ Revision: 649413
- release 3.5

* Thu May 27 2010 Antoine Ginies <aginies@mandriva.com> 3.4-1mdv2011.0
+ Revision: 546318
- add the new tarball
- release 3.4

* Tue May 18 2010 Antoine Ginies <aginies@mandriva.com> 3.3-1mdv2010.1
+ Revision: 545219
- release 3.3

* Tue May 18 2010 Antoine Ginies <aginies@mandriva.com> 3.2-1mdv2010.1
+ Revision: 545075
- release 3.2

* Wed Apr 28 2010 Antoine Ginies <aginies@mandriva.com> 3.1-1mdv2010.1
+ Revision: 540427
- release 3.1

* Wed Apr 07 2010 Antoine Ginies <aginies@mandriva.com> 3.0-1mdv2010.1
+ Revision: 532667
- sync from svn
- sync to latest release available in svn
- release 3.0
- add the new latex doc

* Tue Feb 23 2010 Antoine Ginies <aginies@mandriva.com> 2.0-3mdv2010.1
+ Revision: 510053
- update the doc, and use a forkmanager

* Tue Feb 23 2010 Antoine Ginies <aginies@mandriva.com> 2.0-2mdv2010.1
+ Revision: 510038
- use formanager to speed up the depencies process

* Fri Feb 12 2010 Antoine Ginies <aginies@mandriva.com> 2.0-1mdv2010.1
+ Revision: 504473
- release 2.0

* Thu Oct 29 2009 Antoine Ginies <aginies@mandriva.com> 1.1-1mdv2010.0
+ Revision: 460065
- release 1.1

* Thu Sep 10 2009 Antoine Ginies <aginies@mandriva.com> 1.0-1mdv2010.0
+ Revision: 436810
- new release

* Tue Aug 11 2009 Antoine Ginies <aginies@mandriva.com> 0.8-1mdv2010.0
+ Revision: 414793
- release 0.8

* Fri Aug 07 2009 Antoine Ginies <aginies@mandriva.com> 0.7-1mdv2010.0
+ Revision: 411084
- release 0.7

* Thu Jul 16 2009 Antoine Ginies <aginies@mandriva.com> 0.6-1mdv2010.0
+ Revision: 396561
- release 0.6

* Thu Jun 18 2009 Antoine Ginies <aginies@mandriva.com> 0.5-1mdv2010.0
+ Revision: 387232
- delete thie wrong release (bug in makefile)
- a new release
- adjust to release 0.5
- fix requires

* Sat Jun 13 2009 Antoine Ginies <aginies@mandriva.com> 0.3-1mdv2010.0
+ Revision: 385684
- remove old release
- release 0.3

* Fri Jun 12 2009 Antoine Ginies <aginies@mandriva.com> 0.2-1mdv2010.0
+ Revision: 385556
- new release 0.2

* Fri Jun 12 2009 Antoine Ginies <aginies@mandriva.com> 0.1-1mdv2010.0
+ Revision: 385494
- import bcd


