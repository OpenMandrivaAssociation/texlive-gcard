Name:		texlive-gcard
Version:	20170414
Release:	1
Summary:	Arrange text on a sheet to fold into a greeting card
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gcard
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gcard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gcard.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple means of producing greeting
cards. It arranges four panels onto a single sheet so that when
the sheet is folded twice the four panels are arranged as front
cover, inside left and right pages, and back cover. It uses the
textpos package for placement on the sheet and the graphicx
package for the necessary rotation. The four panels are set in
minipages for formatting by the user.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gcard
%doc %{_texmfdistdir}/doc/latex/gcard

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
