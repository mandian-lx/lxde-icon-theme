Summary: LXDE icon theme
Name: lxde-icon-theme
Version: 0.0.1
Release: %mkrel 3
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-3mdv2011.0
+ Revision: 666111
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-2mdv2011.0
+ Revision: 606441
- rebuild

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 0.0.1-1mdv2010.1
+ Revision: 476249
- import lxde-icon-theme


