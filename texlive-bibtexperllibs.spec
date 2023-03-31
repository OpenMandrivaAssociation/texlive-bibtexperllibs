Name:		texlive-bibtexperllibs
Version:	57137
Release:	2
Summary:	BibTeX Perl Libraries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibtexperllibs
License:	gpl1 artistic pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexperllibs.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexperllibs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides BibTeX related Perl libraries by Gerhard
Gossen, repacked by Boris Veytsman, for TeX Live and other
TDS-compliant distributions. The libraries are written in pure
Perl, so should work out of the box on any architecture. They
have been packaged here mostly for Boris Veytsman's BibTeX
suite, but can be used in any other Perl script.

%prep
%autosetup -p1 -c -a2

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/support/bibtexperllibs
%{_texmfdistdir}/scripts/bibtexperllibs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
