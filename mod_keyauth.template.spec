Summary: DPM Apache httpd plugin for token based authorization.
Name: mod_keyauth
Version: @VERSION@
Release: @RELEASE@@RELEASE.SUFFIX@
License: GPL
Vendor: gLite
Group: grid/lcg
Requires: httpd >= 2.0
AutoReqProv: no
Prefix: /usr
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_builddir}/%{name}-root

%define debug_package %{nil}
%define _unpackaged_files_terminate_build  %{nil}

%description
 The mod_keyauth enables the creation and verification of authn/authz tokens.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./configure --prefix=%{prefix} ${EXTRA_CONFIGURE_OPTIONS}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
echo rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/%{_lib}/httpd/modules/libmod_keyauth.so.0.0.0
%{prefix}/%{_lib}/httpd/modules/libmod_keyauth.so.0
%{prefix}/%{_lib}/httpd/modules/libmod_keyauth.so

%changelog

