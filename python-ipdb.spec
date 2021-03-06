%define module	ipdb
%define	rel		1
%if %mdkversion < 201100
%else
%endif

Summary:	IPython-enabled pdb
Name:		python-%{module}
Version:	0.8
Release:	2
Source0:	https://pypi.python.org/packages/source/i/ipdb/ipdb-%{version}.zip
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
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc COPYING.txt HISTORY.txt README.rst
%{_bindir}/%{module}
%{py_puresitedir}/%{module}*


%changelog
* Fri Jul 13 2012 Lev Givon <lev@mandriva.org> 0.7-1
+ Revision: 809214
- Update to 0.7.

* Tue Oct 25 2011 Lev Givon <lev@mandriva.org> 0.6.1-1
+ Revision: 707172
- Update to 0.6.1.

* Thu Sep 01 2011 Lev Givon <lev@mandriva.org> 0.6-1
+ Revision: 697704
- Update to 0.6.

* Fri Aug 05 2011 Lev Givon <lev@mandriva.org> 0.5-1
+ Revision: 693333
- Update to 0.5.

* Mon Jun 13 2011 Lev Givon <lev@mandriva.org> 0.4-1
+ Revision: 684946
- Update to 0.4.

* Wed Mar 09 2011 Lev Givon <lev@mandriva.org> 0.3-1
+ Revision: 642989
- import python-ipdb



