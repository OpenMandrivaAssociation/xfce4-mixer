%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Volume control for the Xfce
Name:		xfce4-mixer
Version:	4.20.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://www.xfce.org
Source0:	https://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:  meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:  pkgconfig(libxfce4panel-2.0)  
BuildRequires:  pkgconfig(gstreamer-1.0)  
BuildRequires:	pkgconfig(unique-1.0) >= 1.1
Requires:	xfce4-panel
Suggests:	task-pulseaudio
#Suggests:	gstreamer0.10-pulse

%description
The Mixer is a volume control application for the Xfce Desktop Environment.
It provides both a volume control plugin for the Xfce Panel and a standalone 
mixer application.

It supports all audio systems supported by the GStreamer project.

%prep
%autosetup -p1

%build
%meson

%meson_build

%install
%meson_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc ChangeLog AUTHORS NEWS README
%{_bindir}/*
%{_datadir}/applications/xfce*
%{_datadir}/xfce4/panel/plugins/
%{_libdir}/xfce4/panel/plugins/
#{_datadir}/pixmaps/xfce4-mixer/*.png
%{_datadir}/xfce4/mixer/icons/hicolor/16x16/status/audio-input-microphone-muted.png
%{_datadir}/xfce4/mixer/icons/hicolor/scalable/status/audio-input-microphone-muted.svg
%{_mandir}/man1/%{name}.1*
