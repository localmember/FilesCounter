Name:           filescounter
Version:        0.0.1
Release:        1%{?dist}
Summary:        A simple script to count files in specified directory
BuildArch:      noarch

License:        GPL
Source0:        .SOURCES/%{name}-%{version}.tar.gz

Requires:       bash

%description
A demo RPM build

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp ~/%{name}.sh $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/%{name}.sh

%changelog
* Mon Nov 04 2024 localmember 
- First version
