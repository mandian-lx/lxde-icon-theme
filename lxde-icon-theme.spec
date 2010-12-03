Summary: LXDE icon theme
Name: lxde-icon-theme
Version: 0.0.1
Release: %mkrel 2
License: LGPLv2+
Group: Graphical desktop/Other
URL: http://www.lxde.org
Source: http://freefr.dl.sourceforge.net/project/lxde/LXDE%20Icon%20Theme/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Provides: nuoveXT2-icon-theme = %{version}-%{release}
Obsoletes: nuoveXT2-icon-theme < 0.5.0

%description
This package contains nuoveXT2 icon theme for LXDE.

%prep
%setup -q

%build
%configure2_5x

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

touch %buildroot%_iconsdir/nuoveXT2/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache nuoveXT2

%postun
%clean_icon_cache nuoveXT2

%files
%defattr(-,root,root,-)
%dir %_iconsdir/nuoveXT2
%_iconsdir/nuoveXT2/*/*/*
%_iconsdir/nuoveXT2/extra/*
%_iconsdir/nuoveXT2/index.theme
%ghost %_iconsdir/nuoveXT2/icon-theme.cache
