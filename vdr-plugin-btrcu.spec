
%define plugin	btrcu
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define rel	19

Summary:	VDR plugin: Controls VDR through a Bluetooth mobile phone
Name:		%name
Version:	%version
Release:	%rel
Group:		Video
License:	GPL
URL:		http://www.k13zoo.de/vdr/
Source:		http://www.k13zoo.de/vdr/vdr-%plugin-%version.tar.bz2
Patch1:		btrcu-0.0.1-gcc4.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows using a bluetooth mobile phone to act as remote.

%prep
%setup -q -n %plugin-%version
%patch1 -p1 -b .gcc4
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# BtRCU device (default is /dev/rfcomm0)
var=BTRCU_DEV
param=--device=BTRCU_DEV
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -D -m755 btrcu.sh.example %{buildroot}%{vdr_plugin_cfgdir}/btrcu.sh

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{vdr_plugin_cfgdir}/btrcu.sh




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1-18mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1-17mdv2009.1
+ Revision: 359293
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-16mdv2009.0
+ Revision: 197905
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-15mdv2009.0
+ Revision: 197636
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-14mdv2008.1
+ Revision: 145042
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-13mdv2008.1
+ Revision: 144992
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-12mdv2008.1
+ Revision: 103068
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-11mdv2008.0
+ Revision: 49974
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-10mdv2008.0
+ Revision: 42061
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-9mdv2008.0
+ Revision: 22715
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-8mdv2007.0
+ Revision: 90896
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-7mdv2007.1
+ Revision: 73960
- rebuild for new vdr
- Import vdr-plugin-btrcu

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-2mdv2007.0
- use _ prefix for system path macros

* Fri Jun 16 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-1mdv2007.0
- initial Mandriva release

