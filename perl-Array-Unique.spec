#
# Conditional build:
%bcond_without	tests	#do not perform "make test"
#
%define		pdir	Array
%define		pnam	Unique
Summary:	Array::Unique - tieable array that allows only unique values
Summary(pl.UTF-8):	Array::Unique - macierz pozwalająca jedynie na unikalne wartości
Name:		perl-Array-Unique
Version:	0.08
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Array/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3fc4333a97c360348b8c7d0b6b94e83
URL:		http://search.cpan.org/dist/Array-Unique/
%{?with_tests:BuildRequires:	perl-Tie-IxHash}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Array::Compare is a Perl module lets you create an array which will
allow only one occurence of any value. Attempt to put in an already
existing value has no effect.

%description -l pl.UTF-8
Array::Compare jest rozszerzeniem Perla umożliwiającym tworzenie
tablic akceptujących jedynie pojedyncze wystąpienia poszczególnych
wartości. Proba dopisania do tablicy istniejącej już w niej wartości
będzie ignorowana.

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
%doc Changes README
%{perl_vendorlib}/Array/Unique.pm
%{_mandir}/man3/*
