#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Array
%define	pnam	Unique
Summary:	%{pdir}::%{pnam} perl module
Summary(cs):	Modul %{pdir}::%{pnam} pro Perl
Summary(da):	Perlmodul %{pdir}::%{pnam}
Summary(de):	%{pdir}::%{pnam} Perl Modul
Summary(es):	Módulo de Perl %{pdir}::%{pnam}
Summary(fr):	Module Perl %{pdir}::%{pnam}
Summary(it):	Modulo di Perl %{pdir}::%{pnam}
Summary(ja):	%{pdir}::%{pnam} Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	%{pdir}::%{pnam} ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul %{pdir}::%{pnam}
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Summary(pt_BR):	Módulo Perl %{pdir}::%{pnam}
Summary(pt):	Módulo de Perl %{pdir}::%{pnam}
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(sv):	%{pdir}::%{pnam} Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(zh_CN):	%{pdir}::%{pnam} Perl Ä£¿é
Name:		perl-%{pdir}-%{pnam}
Version:	0.03
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.005
%{!?_without_tests:BuildRequires:	perl-Tie-IxHash}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Array::Compare is a Perl module which allows you to compare two arrays.

%description -l pl
Array::Compare jest rozszerzeniem Perla, umo¿liwiaj±cym porównywanie
dwóch tablic

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*.3pm*
