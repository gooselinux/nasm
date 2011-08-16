# -*- coding: utf-8 -*-
Summary: A portable x86 assembler which uses Intel-like syntax
Name: nasm
Version: 2.07
Release: 7%{?dist}
# The entire source code is BSD except misc/proc32.ash which is LGPLv2+, and test/tmap.nas is GPLv2+
License: BSD and LGPLv2+ and GPLv2+
Group: Development/Languages
URL: http://www.nasm.us/
Source0: http://www.nasm.us/pub/nasm/releasebuilds/2.07/%{name}-%{version}.tar.bz2
Source1: http://www.nasm.us/pub/nasm/releasebuilds/2.07/%{name}-%{version}-xdoc.tar.bz2
BuildRequires: perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%package doc
Summary: Documentation for NASM
Group: Development/Languages
BuildRequires: ghostscript, texinfo

%package rdoff
Summary: Tools for the RDOFF binary format, sometimes used with NASM
Group: Development/Tools

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%description doc
This package contains documentation for the Netwide Assembler (NASM),
in HTML, info, PostScript, and text formats.

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%prep
%setup -q
tar xjf %{SOURCE1} --strip-components 1

%build
%configure
make everything
gzip -9f doc/nasmdoc.{ps,txt}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make INSTALLROOT=$RPM_BUILD_ROOT install install_rdf
install -d $RPM_BUILD_ROOT/%{_infodir}
install -t $RPM_BUILD_ROOT/%{_infodir} doc/info/*

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
if [ -e %{_infodir}/nasm.info.gz ]; then
  /sbin/install-info %{_infodir}/nasm.info.gz  %{_infodir}/dir || :
fi

%preun
if [ $1 = 0 -a -e %{_infodir}/nasm.info.gz ]; then
  /sbin/install-info --delete %{_infodir}/nasm.info.gz %{_infodir}/dir || :
fi

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES README TODO LICENSE
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_mandir}/*/*
%{_infodir}/nasm.info*.gz

%files doc
%defattr(-,root,root)
%doc doc/html doc/nasmdoc.txt.gz doc/nasmdoc.ps.gz

%files rdoff
%defattr(-,root,root)
%{_bindir}/ldrdf
%{_bindir}/rdf2bin
%{_bindir}/rdf2ihx
%{_bindir}/rdf2com
%{_bindir}/rdfdump
%{_bindir}/rdflib
%{_bindir}/rdx
%{_bindir}/rdf2ith
%{_bindir}/rdf2srec

%changelog
* Thu Feb 25 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 2.07-7
- add LICENSE to %%doc

* Thu Feb 25 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 2.07-6
- fix license

* Fri Jan 8 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 2.07-5
- fix license. LGPLv2+ to BSD

* Tue Jan 5 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 2.07-4
- fix Url and Sources{0,1}

* Thu Aug 20 2009 Zdenek Prikryl <zprikryl@redhat.com> - 2.07-3
- Don't complain if installing with --excludedocs (#515944)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Adam Tkac <atkac redhat com> - 2.07-1
- update to 2.07

* Wed Jul 10 2009 Zdenek Prikryl <zprikryl@redhat.com> - 2.06-1
- updated to 2.06

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 12 2008 Zdenek Prikryl <zprikryl@redhat.com> - 2.05.01-1
- updated to 2.05.01

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.03.01-2
- fix license tag

* Thu Jun 19 2008 Petr Machata <pmachata@redhat.com> - 2.03.01-1
- rebase to a new stable upstream version 2.03.01

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.01-2
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 Petr Machata <pmachata@redhat.com> - 2.01-1
- rebase to a new stable upstream version 2.01

* Wed Feb  7 2007 Petr Machata <pmachata@redhat.com> - 0.98.39-5
- tidy up the specfile per rpmlint comments
- use utf-8 and fix national characters in contributor's names
- port bogus elf patch to new nasm version and turn it on again

* Thu Jan 25 2007 Petr Machata <pmachata@redhat.com> - 0.98.39-4
- Ville Skyttä: patch for non-failing %%post, %%preun
- Resolves: #223714

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.98.39-3.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.98.39-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.98.39-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Apr  4 2005 Jeremy Katz <katzj@redhat.com> - 0.98.39-3
- pdf docs are duplication of html, txt and postscript

* Fri Apr 01 2005 Jindrich Novy <jnovy@redhat.com> 0.98.39-2
- fix yet another vsprintf buffer overflow (#152963)

* Thu Mar 31 2005 Jindrich Novy <jnovy@redhat.com> 0.98.39-1
- update to 0.98.39
- add BuildRequires ghostscript, texinfo to doc subpackage (#110584)
- generate also PDF documentation for nasm (#88431)
- new release fixes CAN-2004-1287 (#143052)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Sep 26 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 0.98.38 and specfile cleanup

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Dec 17 2002 Phil Knirsch <pknirsch@redhat.com> 0.98.35-2
- Removed ExclusiveArch tag.
- Fixed typo in homepage URL.

* Wed Dec 11 2002 Thomas Woerner <twoerner@redhat.com> 0.98.35-1
- new version 0.98.35
- nasm has new homepage (#77323)

* Fri Nov 29 2002 Tim Powers <timp@redhat.com> 0.98.34-2
- fix %%doc list
- remove unpackaged files from the buildroot

* Mon Sep 16 2002 Jeremy Katz <katzj@redhat.com> 0.98.34-1hammer
- add x86_64 to ExclusiveArch list

* Tue Jul 23 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.98.34-1
- 0.98.34

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.98.32-1
- 0.98.32
- Various doc files have changed names/been removed/added
- New download location (after the license change, it's at sourceforge)
- The new version is LGPL
- Only build on x86 (#65255)

* Tue Feb 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.98.22-2
- Rebuild

* Mon Jan 21 2002 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to 0.98.22 to fix bogus code generation in SDL
- Fix spec file, handle RPM_OPT_FLAGS

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Aug  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Updated patch from H.J. Lu for bogus elf generation (#45986,
  verified by reporter) 

* Thu Apr 26 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Updated patch for bogus elf generation from hjl@gnu.org

* Tue Feb 13 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add patch from H.J. Lu to avoid creating bogus elf objects (#27489)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 13 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rewrote almost everything. The old specfile was bad, bad, bad.
  Really Bad.

* Tue Apr 04 2000 Erik Troan <ewt@redhat.com>
- moved to distribution (syslinux needs it)
- gzipped man pages

* Thu Dec 02 1999 Preston Brown <pbrown@redhat.com>
- adopted from one of the best .spec files I have seen in a long time. :)
