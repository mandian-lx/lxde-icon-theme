Summary:	LXDE icon theme
Name:		lxde-icon-theme
Version:	0.0.1
Release:	3
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		http://www.lxde.org
Source0:	http://freefr.dl.sourceforge.net/project/lxde/LXDE%20Icon%20Theme/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildArch:	noarch
%rename		nuoveXT2-icon-theme

%description
This package contains nuoveXT2 icon theme for LXDE.

%prep
%setup -q

%build
%configure2_5x

%install
%makeinstall_std

touch %buildroot%_iconsdir/nuoveXT2/icon-theme.cache

%post
%update_icon_cache nuoveXT2

%postun
%clean_icon_cache nuoveXT2

%files
%dir %{_iconsdir}/nuoveXT2
%{_iconsdir}/nuoveXT2/*/*/*
%{_iconsdir}/nuoveXT2/extra/*
%{_iconsdir}/nuoveXT2/index.theme
%ghost %{_iconsdir}/nuoveXT2/icon-theme.cache
