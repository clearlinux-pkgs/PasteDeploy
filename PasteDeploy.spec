#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PasteDeploy
Version  : 1.5.2
Release  : 49
URL      : http://pypi.debian.net/PasteDeploy/PasteDeploy-1.5.2.tar.gz
Source0  : http://pypi.debian.net/PasteDeploy/PasteDeploy-1.5.2.tar.gz
Summary  : Load, configure, and compose WSGI applications and servers
Group    : Development/Tools
License  : MIT
Requires: PasteDeploy-license = %{version}-%{release}
Requires: PasteDeploy-python = %{version}-%{release}
Requires: PasteDeploy-python3 = %{version}-%{release}
Requires: Paste
BuildRequires : Paste
BuildRequires : buildreq-distutils3
BuildRequires : nose

%description
URIs; these URIs can refer to Python Eggs for INI-style configuration

%package license
Summary: license components for the PasteDeploy package.
Group: Default

%description license
license components for the PasteDeploy package.


%package python
Summary: python components for the PasteDeploy package.
Group: Default
Requires: PasteDeploy-python3 = %{version}-%{release}
Provides: pastedeploy-python

%description python
python components for the PasteDeploy package.


%package python3
Summary: python3 components for the PasteDeploy package.
Group: Default
Requires: python3-core
Provides: pypi(pastedeploy)
Requires: pypi(setuptools)

%description python3
python3 components for the PasteDeploy package.


%prep
%setup -q -n PasteDeploy-1.5.2
cd %{_builddir}/PasteDeploy-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603397832
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PasteDeploy
cp %{_builddir}/PasteDeploy-1.5.2/docs/license.txt %{buildroot}/usr/share/package-licenses/PasteDeploy/391729571488896efa70494919f96aab67116ad1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.*/site-packages/paste/deploy/paster_templates/paste_deploy/+package+/sampleapp.py_tmpl
rm -f %{buildroot}/usr/lib/python3.*/site-packages/paste/deploy/paster_templates/paste_deploy/+package+/wsgiapp.py_tmpl

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PasteDeploy/391729571488896efa70494919f96aab67116ad1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
