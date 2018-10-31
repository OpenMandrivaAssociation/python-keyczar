Name:           python-keyczar
Version:        0.71c
Release:        3
Summary:        Toolkit for safe and simple cryptography

Group:          Development/Python
License:        ASL 2.0
URL:            http://www.keyczar.org/
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pycrypto%{?_isa}
BuildRequires:  python2-pyasn1


%description
Keyczar is an open source cryptographic toolkit designed to make it easier and
safer for developers to use cryptography in their applications. Keyczar
supports authentication and encryption with both symmetric and asymmetric keys.

%package -n python2-keyczar
Summary:        Toolkit for safe and simple cryptography
Group:          Development/Python

%description -n python2-keyczar
Keyczar is an open source cryptographic toolkit designed to make it easier and
safer for developers to use cryptography in their applications. Keyczar
supports authentication and encryption with both symmetric and asymmetric keys.

%prep
%setup -q
rm -rf python_keyczar.egg-info
# As of 0.71c, there is no python3 support yet

%build
python2 setup.py build

%check
cd tests/keyczar_tests
PYTHONPATH=$PYTHONPATH:../../src/ python2 ./alltests.py

%install
python2 setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}/usr/bin/keyczart

%files -n python2-keyczar
%doc README LICENSE doc/pycrypt.pdf
%{python2_sitelib}/keyczar/
%{python2_sitelib}/python_keyczar-*.egg-info
