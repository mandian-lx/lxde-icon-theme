Summary:	LXDE icon theme
Name:		lxde-icon-theme
Version:	0.5.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		http://www.lxde.org
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildArch:	noarch

%rename		nuoveXT2-icon-theme

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

This package contains nuoveXT2 icon theme for LXDE.

%files
%dir %{_iconsdir}/nuoveXT2
%dir %{_iconsdir}/nuoveXT2/??*x*
%dir %{_iconsdir}/nuoveXT2/??*x*/*
%{_iconsdir}/nuoveXT2/??*x*/*/*
%dir %{_iconsdir}/nuoveXT2/extra
%{_iconsdir}/nuoveXT2/extra/*.png
#%{_iconsdir}/nuoveXT2/index.theme
%ghost %{_iconsdir}/nuoveXT2/icon-theme.cache

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

find -name .gitignore -delete

%build
%configure

%install
%makeinstall_std

touch %{buildroot}%{_iconsdir}/nuoveXT2/icon-theme.cache

%post
%update_icon_cache nuoveXT2

%postun
%clean_icon_cache nuoveXT2

%changelog
* Wed Oct 24 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5.0-1
+ Revision: 819662
- cosmetics
- new version
- cleanups

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-3
+ Revision: 666111
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-2mdv2011.0
+ Revision: 606441
- rebuild

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 0.0.1-1mdv2010.1
+ Revision: 476249
- import lxde-icon-theme


