Summary:	NuFW SSO module for Squid
Name:		squid_nufw_helper
Version:	1.1.3
Release:	%mkrel 1
Group:		System/Servers
License:	GPL
URL:		http://www.inl.fr/squid-nufw-helper.html
Source0:	http://www.nufw.org/attachments/download/7/squid-nufw-helper-%{version}.tar.bz2
Patch0:		squid_nufw_helper-1.1.3-postgresql.diff
Patch1:		squid_nufw_helper-1.1.3-configure.diff
BuildRequires:	mysql-devel
BuildRequires:	pq-devel
BuildRequires:	libxslt-devel
BuildRequires:	pam-devel
Requires:	squid
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
squid-nufw-helper is the authentication SSO module for Squid, working with a
NuFW firewall. It allows for transparent (Single Sign On) authentication of
users on a Squid proxy, even if the proxy is a "transparent" one.

%prep

%setup -q -n squid-nufw-helper-%{version}
%patch0 -p0
%patch1 -p0

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
%doc README ChangeLog squid_nufw_helper.conf
%attr(0755,root,root) %{_sbindir}/squid_nufw_helper-postgresql
%attr(0755,root,root) %{_sbindir}/squid_nufw_helper-mysql


