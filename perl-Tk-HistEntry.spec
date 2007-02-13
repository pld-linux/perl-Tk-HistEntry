#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	HistEntry
Summary:	Tk::HistEntry Perl module - entry widget with history capability
Summary(pl.UTF-8):	Moduł Perla Tk::HistEntry - widget wprowadzania z obsługą historii
Name:		perl-Tk-HistEntry
Version:	0.42
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ee4c3e5469d262cbd18062a4c26495f
BuildRequires:	perl-Tk
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::HistEntry defines entry widgets with history capabilities. The
widgets come in two flavours: HistEntry (Tk::HistEntry::Browse) with
associated browse entry and SimpleHistEntry (Tk::HistEntry::Simple) -
plain widget without browse entry. The user may browse with the Up and
Down keys through the history list. New history entries may be added
either manually by binding the Return key to historyAdd() or
automatically by setting the -command option.

%description -l pl.UTF-8
Klasa Tk::HistEntry definiuje podstawowe widgety do wprowadzania
tekstu z obsługą historii. Widgety są dostępne w dwóch rodzajach:
HistEntry (Tk::HistEntry::Browse) z powiązanym przeglądaniem oraz
SimpleHistEntry (Tk::HistEntry::Simple) bez przeglądania. Użytkownik
może przeglądać listę historii klawiszami Góra i Dół. Nowe elementy
historii mogą być dodawane ręcznie przez podpięcie klawisza Return do
historyAdd() lub automatycznie przez ustawienie opcji -command.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Tk/*.pm
%{_mandir}/man3/*
