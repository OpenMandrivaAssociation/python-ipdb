%define module	ipdb
%define name	python-%{module}
%define version 0.7
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	IPython-enabled pdb
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/i/%{module}/%{module}-%{version}.tar.gz
License:	GPL
Group:		Development/Python
Url:		https://github.com/gotcha/ipdb
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	ipython >= 0.10
BuildRequires:	python-setuptools

%description
ipdb provides functions for accessing the IPython debugger's enhanced features
from within a Python program.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING.txt HISTORY.txt README.rst
%_bindir/%{module}
%py_sitedir/%{module}*
