Name:           filescounter
Version:        1.0
Release:        1%{?dist}
Summary:        Simple bash script to count number of non-oneliner files in directory passed as argument

License:        GPLv3
URL:            http://github.com/localmember/filescounter
Source0:        %{name}.bash
BuildArch:      noarch

%description
Simple bash script to count number of non-oneliner files in directory passed as argument.

%prep

%build

%install

mkdir -p %{buildroot}/usr/local/bin
install -m 0755 %{_sourcedir}/%{name}.bash %{buildroot}/usr/local/bin/filescounter 

%files
/usr/local/bin/filescounter

%changelog
* Mon Dec 16 2024 localmember <localmember> - 1.0-1
- Initial package
