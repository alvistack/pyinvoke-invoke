# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-invoke
Epoch: 100
Version: 2.2.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Pythonic task execution
License: BSD-3-Clause
URL: https://github.com/pyinvoke/invoke/tags
Source0: %{name}_%{version}.orig.tar.gz
Patch0001: 0001-Fix-requirements.patch
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Invoke is a Python (2.7 and 3.4+) library for managing shell-oriented
subprocesses and organizing executable Python code into CLI-invokable
tasks.

%prep
%setup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .
%autopatch -p1

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-invoke
Summary: Pythonic task execution
Requires: python3
Requires: python3-fluidity-sm
Requires: python3-lexicon
Requires: python3-PyYAML
Provides: python3-invoke = %{epoch}:%{version}-%{release}
Provides: python3dist(invoke) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-invoke = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(invoke) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-invoke = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(invoke) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-invoke
Invoke is a Python (2.7 and 3.4+) library for managing shell-oriented
subprocesses and organizing executable Python code into CLI-invokable
tasks.

%files -n python%{python3_version_nodots}-invoke
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-invoke
Summary: Pythonic task execution
Requires: python3
Requires: python3-fluidity-sm
Requires: python3-lexicon
Requires: python3-pyyaml
Provides: python3-invoke = %{epoch}:%{version}-%{release}
Provides: python3dist(invoke) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-invoke = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(invoke) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-invoke = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(invoke) = %{epoch}:%{version}-%{release}

%description -n python3-invoke
Invoke is a Python (2.7 and 3.4+) library for managing shell-oriented
subprocesses and organizing executable Python code into CLI-invokable
tasks.

%files -n python3-invoke
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
