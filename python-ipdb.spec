%define module	ipdb
%define name	python-%{module}
%define version 0.3
%define release %mkrel 1

Summary:	IPython-enhanced pdb
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	GPL
Group:		Development/Python
Url:		https://github.com/gotcha/ipdb
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	ipython
BuildRequires:	python

%description
ipdb provides access to IPython features from within pdb.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README.rst HISTORY.txt
