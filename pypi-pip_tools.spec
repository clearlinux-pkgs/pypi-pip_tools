#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pip_tools
Version  : 6.12.3
Release  : 13
URL      : https://files.pythonhosted.org/packages/47/66/836cddfee7c1ee35385b8eb3af6ef735f5e7130918e72ad05a44b535e2a1/pip-tools-6.12.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/66/836cddfee7c1ee35385b8eb3af6ef735f5e7130918e72ad05a44b535e2a1/pip-tools-6.12.3.tar.gz
Summary  : pip-tools keeps your pinned dependencies fresh.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pip_tools-bin = %{version}-%{release}
Requires: pypi-pip_tools-license = %{version}-%{release}
Requires: pypi-pip_tools-python = %{version}-%{release}
Requires: pypi-pip_tools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: pypi(build)
Requires: pypi(click)
Requires: pypi(pip)
Requires: pypi(setuptools)
Requires: pypi(wheel)

%description python3
python3 components for the pypi-pip_tools package.


%prep
%setup -q -n pip-tools-6.12.3
cd %{_builddir}/pip-tools-6.12.3
pushd ..
cp -a pip-tools-6.12.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680641423
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pip_tools
cp %{_builddir}/pip-tools-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip_tools/167a842e1de543d0763a2c342978bd88b82045b0 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
