#
# Conditional build:
# _with_tests - perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	HistEntry
Summary:	Tk::HistEntry Perl module - entry widget with history capability
Summary(pl):	Modu³ Perla Tk::HistEntry - widget wprowadzania z obs³ug± historii
Name:		perl-Tk-HistEntry
Version:	0.41
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	055dc8efd39dfccc224bbb43bbb5c318
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Tk
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

%description -l pl
Klasa Tk::HistEntry definiuje podstawowe widgety do wprowadzania
tekstu z obs³ug± historii. Widgety s± dostêpne w dwóch rodzajach:
HistEntry (Tk::HistEntry::Browse) z powi±zanym przegl±daniem oraz
SimpleHistEntry (Tk::HistEntry::Simple) bez przegl±dania. U¿ytkownik
mo¿e przegl±daæ listê historii klawiszami Góra i Dó³. Nowe elementy
historii mog± byæ dodawane rêcznie przez podpiêcie klawisza Return do
historyAdd() lub automatycznie przez ustawienie opcji -command.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?_with_tests:%{__make} test}

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
