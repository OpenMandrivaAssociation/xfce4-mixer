%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Volume control for the Xfce
Name:		xfce4-mixer
Version:	4.10.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.9.1
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	xfconf-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libalsa-devel
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	pkgconfig(unique-1.0)
Requires:	xfce4-panel >= 4.7.0
Suggests:	task-pulseaudio
Suggests:	gstreamer0.10-pulse
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils
Obsoletes:	xfce-mixer

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
%doc TODO ChangeLog AUTHORS NEWS HACKING
%{_bindir}/*
%{_datadir}/applications/xfce*
%{_datadir}/xfce4/panel-plugins/
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/%{name}
%{_datadir}/pixmaps/xfce4-mixer/*.png
