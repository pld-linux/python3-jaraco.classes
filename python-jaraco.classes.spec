#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Utility functions for Python class constructs
Summary(pl.UTF-8):	Funkcje narzędziowe do konstrukcji klas pythonowych
Name:		python-jaraco.classes
# keep 2.x here for python2 support
Version:	2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jaraco.classes/
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.classes/jaraco.classes-%{version}.tar.gz
# Source0-md5:	63d4f5a2df2625ec3979c9633da1505e
URL:		https://pypi.org/project/jaraco.classes/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:34.4
BuildRequires:	python-setuptools_scm >= 1.15
%if %{with tests}
BuildRequires:	python-pytest >= 3.5
#BuildRequires:	python-pytest-checkdocs
BuildRequires:	python-pytest-flake8
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 1:34.4
BuildRequires:	python3-setuptools_scm >= 1.15
%if %{with tests}
BuildRequires:	python3-pytest >= 3.5
#BuildRequires:	python3-pytest-checkdocs
BuildRequires:	python3-pytest-flake8
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-jaraco.packaging >= 3.2
BuildRequires:	python-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-jaraco
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility functions for Python class constructs.

%description -l pl.UTF-8
Funkcje narzędziowe do konstrukcji klas pythonowych.

%package -n python3-jaraco.classes
Summary:	Utility functions for Python class constructs
Summary(pl.UTF-8):	Funkcje narzędziowe do konstrukcji klas pythonowych
Group:		Libraries/Python
Requires:	python3-jaraco
Requires:	python3-modules >= 1:3.2

%description -n python3-jaraco.classes
Utility functions for Python class constructs.

%description -n python3-jaraco.classes -l pl.UTF-8
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
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_flake8 \
%{__python} -m pytest jaraco
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_flake8 \
%{__python3} -m pytest jaraco
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

# packaged in python-jaraco.spec
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/jaraco/__init__.py*
%endif

%if %{with python3}
%py3_install

# packaged in python3-jaraco.spec
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/jaraco/__init__.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/jaraco/__pycache__/__init__.*.py*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/jaraco/classes
%{py_sitescriptdir}/jaraco.classes-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jaraco.classes
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/jaraco/classes
%{py3_sitescriptdir}/jaraco.classes-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
