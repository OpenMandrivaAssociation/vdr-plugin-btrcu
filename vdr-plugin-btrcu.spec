%define plugin	btrcu

Summary:	VDR plugin: Controls VDR through a Bluetooth mobile phone
Name:		vdr-plugin-%plugin
Version:	0.0.1
Release:	22
Group:		Video
License:	GPL
URL:		http://www.k13zoo.de/vdr/
Source:		http://www.k13zoo.de/vdr/vdr-%plugin-%{version}.tar.gz
Patch1:		btrcu-0.0.1-gcc4.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows using a bluetooth mobile phone to act as remote.

%prep
%setup -q -n %plugin-%{version}
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

%files -f %plugin.vdr
%doc README HISTORY
%config(noreplace) %{vdr_plugin_cfgdir}/btrcu.sh




