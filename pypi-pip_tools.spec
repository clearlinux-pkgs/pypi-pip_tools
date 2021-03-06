#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pip_tools
Version  : 6.6.2
Release  : 4
URL      : https://files.pythonhosted.org/packages/dc/21/af0d14ce1cbe9e2e88ccf73061251cc6a84d8d87650a3e75be040a0be4fe/pip-tools-6.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/21/af0d14ce1cbe9e2e88ccf73061251cc6a84d8d87650a3e75be040a0be4fe/pip-tools-6.6.2.tar.gz
Summary  : pip-tools keeps your pinned dependencies fresh.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pip_tools-bin = %{version}-%{release}
Requires: pypi-pip_tools-license = %{version}-%{release}
Requires: pypi-pip_tools-python = %{version}-%{release}
Requires: pypi-pip_tools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(pep517)
BuildRequires : pypi(pip)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
|jazzband| |pypi| |pyversions| |pre-commit| |buildstatus-gha| |codecov|
==================================
pip-tools = pip-compile + pip-sync
==================================

%package bin
Summary: bin components for the pypi-pip_tools package.
Group: Binaries
Requires: pypi-pip_tools-license = %{version}-%{release}

%description bin
bin components for the pypi-pip_tools package.


%package license
Summary: license components for the pypi-pip_tools package.
Group: Default

%description license
license components for the pypi-pip_tools package.


%package python
Summary: python components for the pypi-pip_tools package.
Group: Default
Requires: pypi-pip_tools-python3 = %{version}-%{release}

%description python
python components for the pypi-pip_tools package.


%package python3
Summary: python3 components for the pypi-pip_tools package.
Group: Default
Requires: python3-core
Provides: pypi(pip_tools)
Requires: pypi(click)
Requires: pypi(pep517)
Requires: pypi(pip)
Requires: pypi(setuptools)
Requires: pypi(wheel)

%description python3
python3 components for the pypi-pip_tools package.


%prep
%setup -q -n pip-tools-6.6.2
cd %{_builddir}/pip-tools-6.6.2
pushd ..
cp -a pip-tools-6.6.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394399
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pip_tools
cp %{_builddir}/pip-tools-6.6.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip_tools/167a842e1de543d0763a2c342978bd88b82045b0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pip-compile
/usr/bin/pip-sync

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pip_tools/167a842e1de543d0763a2c342978bd88b82045b0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
