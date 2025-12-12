%define module	ipdb

Summary:	IPython-enabled pdb
Name:		python-%{module}
Version:	0.13.13
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/i/ipdb/ipdb-%{version}.tar.gz
License:	GPL
Group:		Development/Python
Url:		https://github.com/gotcha/ipdb
BuildArch:	noarch
Requires:	ipython >= 0.10
BuildRequires:	python-setuptools

%description
ipdb provides functions for accessing the IPython debugger's enhanced features
from within a Python program.

%prep
%autosetup -p1 -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
ln -s ipdb3 %{buildroot}%{_bindir}/ipdb

%files
%doc COPYING.txt HISTORY.txt README.rst
%{_bindir}/ipdb
%{_bindir}/ipdb3
%{py_puresitedir}/%{module}*
