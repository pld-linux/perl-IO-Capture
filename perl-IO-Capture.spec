#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Capture
Summary:	IO::Capture - Abstract Base Class to build modules to capture output
Summary(pl.UTF-8):   IO::Capture - abstrakcyjna klasa bazowa dla modułów przechwytujących wyjście
Name:		perl-IO-Capture
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4760036d7fcf9f2cc34f2b2eefd511a4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IO::Capture module defines an abstract base class that can be used
to build modules that capture output being sent on a filehandle such as
STDOUT or STDERR.

%description -l pl.UTF-8
Moduł IO::Capture definiuje abstrakcyjną klasę bazową, która może być
używana do tworzenia modułów przechwytujących wyjście wysyłane przez
uchwyt pliku, taki jak STDOUT czy STDERR.

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
%doc BUGS Changes README
%{perl_vendorlib}/IO/*.pm
%{perl_vendorlib}/IO/Capture
%{_mandir}/man3/*
