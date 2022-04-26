#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-mpmath
Version  : 1.2.1
Release  : 28
URL      : https://files.pythonhosted.org/packages/95/ba/7384cb4db4ed474d4582944053549e02ec25da630810e4a23454bc9fa617/mpmath-1.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/95/ba/7384cb4db4ed474d4582944053549e02ec25da630810e4a23454bc9fa617/mpmath-1.2.1.tar.gz
Summary  : Python library for arbitrary-precision floating-point arithmetic
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-mpmath-license = %{version}-%{release}
Requires: pypi-mpmath-python = %{version}-%{release}
Requires: pypi-mpmath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
======
        
        |pypi version| |Build status| |Code coverage status| |Zenodo Badge|

%package license
Summary: license components for the pypi-mpmath package.
Group: Default

%description license
license components for the pypi-mpmath package.


%package python
Summary: python components for the pypi-mpmath package.
Group: Default
Requires: pypi-mpmath-python3 = %{version}-%{release}

%description python
python components for the pypi-mpmath package.


%package python3
Summary: python3 components for the pypi-mpmath package.
Group: Default
Requires: python3-core
Provides: pypi(mpmath)

%description python3
python3 components for the pypi-mpmath package.


%prep
%setup -q -n mpmath-1.2.1
cd %{_builddir}/mpmath-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651015519
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mpmath
cp %{_builddir}/mpmath-1.2.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mpmath/ab0d946b9b936d80fdfe187af6dd0fbce9906dd2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mpmath/ab0d946b9b936d80fdfe187af6dd0fbce9906dd2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
