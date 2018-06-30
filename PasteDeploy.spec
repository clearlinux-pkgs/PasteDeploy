#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PasteDeploy
Version  : 1.5.2
Release  : 31
URL      : http://pypi.debian.net/PasteDeploy/PasteDeploy-1.5.2.tar.gz
Source0  : http://pypi.debian.net/PasteDeploy/PasteDeploy-1.5.2.tar.gz
Summary  : Load, configure, and compose WSGI applications and servers
Group    : Development/Tools
License  : MIT
Requires: PasteDeploy-python3
Requires: PasteDeploy-python
Requires: Paste
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
URIs; these URIs can refer to Python Eggs for INI-style configuration

%package python
Summary: python components for the PasteDeploy package.
Group: Default
Requires: PasteDeploy-python3
Provides: pastedeploy-python

%description python
python components for the PasteDeploy package.


%package python3
Summary: python3 components for the PasteDeploy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the PasteDeploy package.


%prep
%setup -q -n PasteDeploy-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523296933
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.6/site-packages/paste/deploy/paster_templates/paste_deploy/+package+/sampleapp.py_tmpl
%exclude /usr/lib/python3.6/site-packages/paste/deploy/paster_templates/paste_deploy/+package+/wsgiapp.py_tmpl
/usr/lib/python3*/*
