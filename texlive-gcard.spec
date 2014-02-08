# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gcard
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-gcard
Version:	20080819
Release:	3
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
%{_texmfdistdir}/tex/latex/gcard/gcard.sty
%doc %{_texmfdistdir}/doc/latex/gcard/README
%doc %{_texmfdistdir}/doc/latex/gcard/gcard.pdf
%doc %{_texmfdistdir}/doc/latex/gcard/gcardex.tex
%doc %{_texmfdistdir}/doc/latex/gcard/gcardminexample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080819-2
+ Revision: 752190
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080819-1
+ Revision: 718526
- texlive-gcard
- texlive-gcard
- texlive-gcard
- texlive-gcard

