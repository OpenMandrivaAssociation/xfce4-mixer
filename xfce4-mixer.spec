Summary:	Volume control for the Xfce
Name:		xfce4-mixer
Version:	4.4.2
Release:	%mkrel 5
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	xfce4-mixer-%{version}.tar.bz2
Patch0:		01_volume_hotkeys.patch
Patch1:         02_mixer-block-menu.patch
Patch2:         03_xfce4-mixer-panel-plugin_border.patch
Requires:	xfce4-panel >= %{version}
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	imagemagick
BuildRequires:	xfce-mcs-manager-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	libalsa-devel
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes:	xfce-mixer
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfce-mixer is the volume control for Xfce. It includes
a sound mixer.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
convert settings/%{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert settings/%{name}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

desktop-file-install \
	--remove-category="X-FACE" \
	--add-category="Mixer" \
	--add-category="Audio" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

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
%doc README ChangeLog NOTES AUTHORS NEWS
%{_bindir}/*
%{_datadir}/applications/xfce*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/xfce4/panel-plugins/
%{_libdir}/xfce4/panel-plugins/
%{_libdir}/xfce4/mcs-plugins/
%{_libdir}/xfce4/modules/*
