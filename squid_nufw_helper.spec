Summary:	NuFW SSO module for Squid
Name:		squid_nufw_helper
Version:	1.0.0
Release:	%mkrel 0.rc2.3
Group:		System/Servers
License:	GPL
URL:		http://www.inl.fr/squid-nufw-helper.html
Source0:	http://www.inl.fr/IMG/gz/%{name}-%{version}-rc2.tar.bz2
Patch0:		squid_nufw_helper-1.0.0-rc2-postgresql.diff
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
Requires:	squid
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
squid-nufw-helper is the authentication SSO module for Squid, working with a
NuFW firewall. It allows for transparent (Single Sign On) authentication of
users on a Squid proxy, even if the proxy is a "transparent" one.

%prep

%setup -q -n %{name}-%{version}-rc2
%patch0 -p1

# cleanup
rm -rf autom4te.cache
rm -f squid_nufw_helper

%build

%configure2_5x
make clean
%make

mv squid_nufw_helper squid_nufw_helper-postgresql

%configure2_5x \
    --with-mysql
%make
mv squid_nufw_helper squid_nufw_helper-mysql

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}

install -m0755 squid_nufw_helper-postgresql %{buildroot}%{_sbindir}/
install -m0755 squid_nufw_helper-mysql %{buildroot}%{_sbindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog doc/* example.conf
%attr(0755,root,root) %{_sbindir}/squid_nufw_helper-postgresql
%attr(0755,root,root) %{_sbindir}/squid_nufw_helper-mysql


