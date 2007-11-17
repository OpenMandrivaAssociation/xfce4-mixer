%define oname 		xfce4-mixer
%define iconname  	%{oname}.png

Summary:	Volume control for the Xfce
Name:		xfce-mixer
Version:	4.4.1
Release:	%mkrel 4
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	xfce4-mixer-%{version}.tar.bz2
Patch0:		01_volume_hotkeys.patch
Requires:	xfce-panel >= %{version}
BuildRequires:	xfce-panel-devel >= %{version}
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	imagemagick
BuildRequires:	xfce-mcs-manager-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	libalsa-devel
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfce-mixer is the volume control for Xfce. It includes
a sound mixer.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1

%build
%configure2_5x \
	--with-sound=alsa \
	--enable-final \
	--disable-static
# (tpg) don't use macro because parallel build fails
# use dirty hacks :)
%(echo %make|perl -pe 's/-j\d+/-j1/g')

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{32x32,16x16}/apps
convert settings/%{oname}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{iconname}
convert settings/%{oname}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{iconname}

desktop-file-install \
--remove-category="X-FACE" \
--add-category="Mixer" \
--add-category="Audio" \
--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{oname}

%clean
rm -rf %{buildroot}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor
 
%files -f %{oname}.lang
%defattr(-,root,root)
%doc README ChangeLog NOTES INSTALL COPYING AUTHORS
%{_bindir}/*
%{_datadir}/applications/xfce*
%{_iconsdir}/hicolor/*/apps/%{iconname}
%{_datadir}/xfce4/panel-plugins/
%{_libdir}/xfce4/panel-plugins/
%{_libdir}/xfce4/mcs-plugins/
%{_libdir}/xfce4/modules/*
