Summary:	Subversion variants of \Provides... macros
Summary(pl.UTF-8):	Warianty Subversion makr \Provides...
Name:		tex-latex-svn-prov
Version:	3.1862
Release:	1
License:	LaTeX Project Public License v1.3c+
Group:		Applications/Publishing
Source0:	http://mirrors.ctan.org/macros/latex/contrib/svn-prov.zip
# Source0-md5:	b90a889b1bb471039470820cf894af9d
URL:		https://sourceforge.net/projects/svn-prov/
BuildRequires:	/usr/bin/latex
BuildRequires:	rpmbuild(macros) >= 1.751
BuildRequires:	tex(ydoc)
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
# TODO: use generic
Requires:	texlive-latex
Provides:	tex(svn-prov) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package introduces Subversion variants of the standard LaTeX
macros \ProvidesPackage, \ProvidesClass and \ProvidesFile where the
file name and date is extracted from Subversion Id keywords. The file
name may also be given explicitly as an optional argument.

%description -l pl.UTF-8
Pakiet wprowadza warianty Subversion standardowych makr LaTeXa
\ProvidesPackage, \ProvidesClass oraz \ProvidesFile, gdzie nazwa pliku
i data są wyciągane ze słów kluczowych Subversion Id. Nazwę pliku
można także podać bezpośrednio jako opcjonalny argument.

%prep
%setup -q -n svn-prov

%build
latex svn-prov.ins

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{doc,tex}/latex/svn-prov

cp -p *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/svn-prov
cp -p *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/svn-prov

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
# XXX: move dir to texlive (or other base TeX distribution package)
%dir %{_datadir}/texmf/doc/latex
%doc %{_datadir}/texmf/doc/latex/svn-prov
%{_datadir}/texmf/tex/latex/svn-prov
