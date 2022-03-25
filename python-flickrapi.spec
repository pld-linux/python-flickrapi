#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		flickrapi
%define		egg_name	flickrapi
%define		pypi_name	flickrapi
Summary:	Python module for interfacing with the Flickr API
Name:		python-%{pypi_name}
Version:	2.2.1
Release:	6
License:	Python
Group:		Libraries/Python
URL:		http://stuvel.eu/flickrapi
Source0:	https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	d901d6ccb4bb0e990e69d9f8762084a6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-requests
Requires:	python-requests-oauthlib
Requires:	python-requests-toolbelt
Requires:	python-six
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for interfacing with the Flickr API.

%package -n python3-%{module}
Summary:	Python module for interfacing with the Flickr API
Requires:	python3-requests
Requires:	python3-requests-oauthlib
Requires:	python3-requests-toolbelt
Requires:	python3-six

%description -n python3-%{module}
A Python module for interfacing with the Flickr API.

%prep
%setup -q -n %{module}-%{version}
rm -r %{module}.egg-info

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/*.txt
%endif

%if %{with python3}
%py3_install
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/*.txt
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc UPGRADING.txt LICENSE.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc UPGRADING.txt LICENSE.txt
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
