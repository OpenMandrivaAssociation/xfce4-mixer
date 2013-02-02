%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Volume control for the Xfce
Name:		xfce4-mixer
Version:	4.10.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.9.1
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	xfconf-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.9.1
BuildRequires:	pkgconfig(unique-1.0) >= 1.1
Requires:	xfce4-panel >= 4.7.0
Suggests:	task-pulseaudio
Suggests:	gstreamer0.10-pulse

%description
The Mixer is a volume control application for the Xfce Desktop Environment.
It provides both a volume control plugin for the Xfce Panel and a standalone 
mixer application.

It supports all audio systems supported by the GStreamer project.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc ChangeLog AUTHORS NEWS README
%{_bindir}/*
%{_datadir}/applications/xfce*
%{_datadir}/xfce4/panel/plugins/
%{_libdir}/xfce4/panel/plugins/
%{_datadir}/%{name}
%{_datadir}/pixmaps/xfce4-mixer/*.png
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 4.8.0-3
+ Revision: 791508
- Rebuild

* Thu Apr 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-2
+ Revision: 789490
- rebuild

* Sun Feb 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 640555
- update to new version 4.8.0
- drop patch 0
- adjust buildrequires

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-7
+ Revision: 633051
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-6mdv2011.0
+ Revision: 579648
- adjust buildrequires
- rebuild for new xfce 4.7.0

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-5mdv2010.1
+ Revision: 543295
- rebuild for mdv 2010.1

* Thu Jul 02 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-4mdv2010.0
+ Revision: 391388
- add suggests on gstreamer0.10-pulse

* Sat May 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-3mdv2010.0
+ Revision: 381366
- Patch0: fix panel plugin volume adjustment

* Sat May 16 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.0
+ Revision: 376389
- suggests on task-pulseaudio

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368575
- update to new version 4.6.1

* Sun Apr 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-3mdv2009.1
+ Revision: 364239
- provide better description
- drop old patches
- Patch3: various critical fixes from upstream svn

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349208
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345709
- New upstream release

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333999
- update to new version 4.5.99.1

* Thu Jan 15 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-2mdv2009.1
+ Revision: 330027
- bump tag, build system is hungry

* Wed Jan 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329514
- update to new version 4.5.93

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303575
- fix file list
- add full path for the Source0
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294974
- Xfce4.6 beta1 is landing on cooker
- drop all patches
- tune up buildrequires
- fix file list

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-6mdv2009.0
+ Revision: 262363
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-5mdv2009.0
+ Revision: 256876
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-3mdv2008.1
+ Revision: 145792
- update volume hotkeys patch

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.2-2mdv2008.1
+ Revision: 116030
- Add two patches for fixing some bugs

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new license policy
    - do not package COPYING and INSTALL, add NEWS instead

* Sun Nov 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 110065
- disable parallel build
- new version 4.4.2
- use parallel make
- fix file list
- use upstream tarball name as a real name
- use upstream name

  + Jérôme Soyer <saispo@mandriva.org>
    - New release 4.4.2

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-4mdv2008.0
+ Revision: 71239
- remove X-MandrivaLinux from desktop file

* Mon Jun 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-3mdv2008.0
+ Revision: 35072
- use dirty hack for parallel build
- add patch 0 (multimedia keys)

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 32844
- s/imagemagick/ImageMagick
- correct requires
- use macros in %%post and %%postun
- compile with alsa support

* Wed Apr 25 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 18151
- Disable parallel build
- Push new release 4.4.1
- New release 4.4.1

