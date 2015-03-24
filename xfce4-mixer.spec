%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Volume control for the Xfce
Name:		xfce4-mixer
Version:	4.11.0
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(keybinder)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
BuildRequires:	pkgconfig(unique-1.0) >= 1.1
Requires:	xfce4-panel >= 4.7.0
Suggests:	task-pulseaudio
#Suggests:	gstreamer0.10-pulse

%description
The Mixer is a volume control application for the Xfce Desktop Environment.
It provides both a volume control plugin for the Xfce Panel and a standalone 
mixer application.

It supports all audio systems supported by the GStreamer project.

%prep
%setup -q

%build
%configure

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
