#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Utility functions for Python class constructs
Summary(pl.UTF-8):	Funkcje narzędziowe do konstrukcji klas pythonowych
Name:		python3-jaraco.classes
Version:	3.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jaraco.classes/
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.classes/jaraco.classes-%{version}.tar.gz
# Source0-md5:	994fb3f2ce9bb538ca6e8abf6ebbdf9c
URL:		https://pypi.org/project/jaraco.classes/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools >= 1:56
BuildRequires:	python3-setuptools_scm >= 3.4.1
%if %{with tests}
BuildRequires:	python3-pytest >= 6
#BuildRequires:	python3-pytest-checkdocs >= 2.4
#BuildRequires:	python3-pytest-cov
#BuildRequires:	python3-pytest-mypy
#BuildRequires:	python3-pytest-enabler >= 2.2
#BuildRequires:	python3-pytest-ruff >= 0.2.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-furo
BuildRequires:	python3-jaraco.packaging >= 9.3
BuildRequires:	python3-jaraco.tidelift >= 1.4
BuildRequires:	python3-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-3 >= 3.5
%endif
Requires:	python3-jaraco
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility functions for Python class constructs.

%description -l pl.UTF-8
Funkcje narzędziowe do konstrukcji klas pythonowych.

%package apidocs
Summary:	API documentation for Python jaraco.classes module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona jaraco.classes
Group:		Documentation

%description apidocs
API documentation for Python jaraco.classes module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona jaraco.classes.

%prep
%setup -q -n jaraco.classes-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest jaraco
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst SECURITY.md
%{py3_sitescriptdir}/jaraco/classes
%{py3_sitescriptdir}/jaraco_classes-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
