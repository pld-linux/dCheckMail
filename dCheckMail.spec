%include	/usr/lib/rpm/macros.perl
Summary:	dCheckMail - mbox mail folder checker
Summary(pl):	dCheckMail - sprawdzacz folderów pocztowych mbox
Name:		dCheckMail
Version:	1.0
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dCheckMail scans through given mail-folder files and dirs, and prints
nice summary about unread messages.

%description -l pl
dCheckMail przeszukuje podane pliki oraz katalogi ze skrzynkami
pocztowymi i wy¶wietla podsumowanie dotycz±ce nieprzeczytanych
wiadomo¶ci.

%prep
%setup  -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT/etc/ds
install etc/%{name}.ini $RPM_BUILD_ROOT/etc/ds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/depesz
%{_mandir}/man3/*
%{_sysconfdir}/ds
