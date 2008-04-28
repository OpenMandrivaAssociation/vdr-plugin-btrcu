
%define plugin	btrcu
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define rel	16

Summary:	VDR plugin: Controls VDR through a Bluetooth mobile phone
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.k13zoo.de/vdr/
Source:		http://www.k13zoo.de/vdr/vdr-%plugin-%version.tar.bz2
Patch1:		btrcu-0.0.1-gcc4.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}
%vdr_plugin_install

install -D -m755 btrcu.sh.example %{buildroot}%{_vdr_plugin_cfgdir}/btrcu.sh

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{_vdr_plugin_cfgdir}/btrcu.sh


