Summary:	Subversion to Git conversion script
Name:		agito
# no version known
Version:	0.1
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	https://github.com/fragglet/agito/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	410cd5e31be46ae1c0725ffae2c44074
URL:		https://github.com/fragglet/agito
BuildRequires:	sed >= 4.0
Requires:	git-core
Requires:	subversion
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Agito is (yet another) Subversion to Git conversion script.

It is designed to do a better job of translating history than git-svn,
which has some subtleties in the way it works that cause it to
construct branch histories that are suboptimal in certain corner case
scenarios. Agito was created to convert the history of Chocolate Doom,
which exhibits some of these corner cases. For more information on how
Agito is different to git-svn, see DESIGN.

%prep
%setup -qc
mv agito-*/* .

%{__sed} -i -e '1s,^#!.*python,#!%{__python},' %{name}.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS DESIGN example.cfg
%attr(755,root,root) %{_bindir}/agito
