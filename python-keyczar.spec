Name:           python-keyczar
Version:        0.71c
Release:        %mkrel 1
Summary:        Toolkit for safe and simple cryptography

Group:          Development/Python
License:        ASL 2.0
URL:            http://www.keyczar.org/
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pycrypto%{?_isa}
BuildRequires:  python-pyasn1


%description
Keyczar is an open source cryptographic toolkit designed to make it easier and
safer for developers to use cryptography in their applications. Keyczar
supports authentication and encryption with both symmetric and asymmetric keys.


%prep
%setup -q
rm -rf python_keyczar.egg-info

%build
%{__python} setup.py build

%check
cd tests/keyczar_tests
PYTHONPATH=$PYTHONPATH:../../src/ ./alltests.py

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}/usr/bin/keyczart

%files
%doc README LICENSE doc/pycrypt.pdf
%{python_sitelib}/keyczar/
%{python_sitelib}/python_keyczar-*.egg-info




%changelog
* Mon Nov 11 2013 philippem <philippem> 0.71c-1.mga4
+ Revision: 550494
- imported package python-keyczar

