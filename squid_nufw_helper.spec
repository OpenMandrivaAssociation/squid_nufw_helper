Summary:	NuFW SSO module for Squid
Name:		squid_nufw_helper
Version:	1.1.3
Release:	%mkrel 6
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
BuildRequires:	readline-devel
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




%changelog
* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-6mdv2011.0
+ Revision: 645893
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-5mdv2011.0
+ Revision: 627289
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-4mdv2011.0
+ Revision: 626563
- rebuilt against mysql-5.5.8 libs

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-2mdv2011.0
+ Revision: 614969
- the mass rebuild of 2010.1 packages

* Sun Mar 07 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.1.3-1mdv2010.1
+ Revision: 515328
- New 1.1.3
  P0 rediff

* Thu Feb 18 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-0.rc2.5mdv2010.1
+ Revision: 507511
- rebuild

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-0.rc2.4mdv2010.0
+ Revision: 445228
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - use lowercase mysql-devel

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-0.rc2.3mdv2009.1
+ Revision: 311354
- fix the postgresql patch
- rebuilt against mysql-5.1.30 libs

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-0.rc2.2mdv2008.1
+ Revision: 140851
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 16 2007 Michael Scherer <misc@mandriva.org> 1.0.0-0.rc2.2mdv2007.1
+ Revision: 144947
- Rebuild for new postgresql

  + Jérôme Soyer <saispo@mandriva.org>
    - Import squid_nufw_helper

* Sat Jun 17 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-0.rc2.1mdv2007.0
- initial Mandriva package

