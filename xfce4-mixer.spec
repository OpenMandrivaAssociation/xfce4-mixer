%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Volume control for the Xfce
Name:		xfce4-mixer
Version:	4.6.1
Release:	%mkrel 6
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		xfce4-mixer-4.6.1-fix_volume_adjustment.patch
BuildRequires:	xfce4-panel-devel >= 4.7.0
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	xfconf-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libalsa-devel
BuildRequires:	libxfcegui4-devel
Requires:	xfce4-panel >= 4.7.0
Suggests:	task-pulseaudio
Suggests:	gstreamer0.10-pulse
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes:	xfce-mixer
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The Mixer is a volume control application for the Xfce Desktop Environment.
It provides both a volume control plugin for the Xfce Panel and a standalone 
mixer application.

It supports all audio systems supported by the GStreamer project.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc TODO ChangeLog AUTHORS NEWS HACKING
%{_bindir}/*
%{_datadir}/applications/xfce*
%{_datadir}/xfce4/panel-plugins/
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/%{name}
%{_datadir}/pixmaps/xfce4-mixer/*.png
