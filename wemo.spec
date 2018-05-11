Name: wemo
Version: 1.0.0
Release: 1%{?dist}
Summary: Belkin WeMo Light Switch Control
Group: System Environment/Base
License: Unknown
URL: https://github.com/mississaugalug/bash
Source0: wemo
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Bash script to control Belkin WeMo Light Switch.

%prep

%install
rm -rf %{buildroot}
%{__install} -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Fri May 11 2018 Ira W. Snyder <isnyder@lco.global> - 1.0.0-1
- Initial build.
