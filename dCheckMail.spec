%include	/usr/lib/rpm/macros.perl

Summary:	dCheckMail - mbox mail folder checker
Summary(pl):	dCheckMail - sprawdzacz folderów pocztowych mbox
Name:		dCheckMail
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dCheckMail scans through given mail-folder files and dirs, and prints nice summary about unread messages.

%prep
%setup  -q

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT/etc/ds
install etc/%{name}.ini $RPM_BUILD_ROOT/etc/ds

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/depesz
%{_mandir}/man3/*
%{_sysconfdir}/ds
