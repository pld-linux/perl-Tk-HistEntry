%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	HistEntry
Summary:	Tk::HistEntry Perl module
Summary(pl):	Modu� Perla Tk::HistEntry
Name:		perl-Tk-HistEntry
Version:	0.41
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce3ef504ebcddf078f0a8c8eeb68a1b5
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::HTML Perl module.

%description -l pl
Modu� Perla Tk::HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/Tk/*.pm
%{_mandir}/man3/*
