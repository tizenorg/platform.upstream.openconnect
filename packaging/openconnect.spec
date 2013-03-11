Name:           openconnect
Version:        4.99
Release:        0
License:        LGPL-2.1+
Summary:        Open client for Cisco AnyConnect VPN
Url:            http://www.infradead.org/openconnect.html
Group:          Networking/Security
Source0:        ftp://ftp.infradead.org/pub/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vpnc
Requires:       vpnc

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.  AnyConnect is supported by the ASA5500 Series,
by IOS 12.4(9)T or later on Cisco SR500, 870, 880, 1800, 2800, 3800,
7200 Series and Cisco 7301 Routers, and probably others.

%package devel
Summary:        Development files and headers for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}
Recommends:     pkg-config

%description devel
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.  AnyConnect is supported by the ASA5500 Series,
by IOS 12.4(9)T or later on Cisco SR500, 870, 880, 1800, 2800, 3800,
7200 Series and Cisco 7301 Routers, and probably others.

This packages provides development files and headers needed to build
packages against openconnect


%prep
%setup -q

%build
%autogen 
%configure --docdir=%{_docdir}/%{name}/ --disable-nls
make

%install
%make_install

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%license COPYING.LGPL 
%{_libdir}/libopenconnect.so.*
%{_mandir}/man8/*
%{_sbindir}/openconnect

%files devel
%defattr(-,root,root)
%{_includedir}/openconnect.h
%{_libdir}/libopenconnect.so
%{_libdir}/pkgconfig/openconnect.pc
%{_docdir}/%{name}/

%docs_package


%changelog
