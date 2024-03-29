Summary:	dCheckMail - mbox mail folder checker
Summary(pl.UTF-8):	dCheckMail - sprawdzacz folderów pocztowych mbox
Name:		dCheckMail
Version:	1.0
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	383689aa86c8484ea14491265770cf40
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Config-IniFiles
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dCheckMail scans through given mail-folder files and dirs, and prints
nice summary about unread messages.

%description -l pl.UTF-8
dCheckMail przeszukuje podane pliki oraz katalogi ze skrzynkami
pocztowymi i wyświetla podsumowanie dotyczące nieprzeczytanych
wiadomości.

%prep
%setup  -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ds
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install etc/%{name}.ini $RPM_BUILD_ROOT%{_sysconfdir}/ds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/depesz
%{_mandir}/man3/*
%{_sysconfdir}/ds
