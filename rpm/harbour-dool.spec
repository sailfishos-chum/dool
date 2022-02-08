# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-dool

# >> macros
# << macros
%define upstream_name dool
%define upstream_commit 02b1c69

Summary:    Pluggable real-time performance monitoring tool
Version:    0.9.10
Release:    2
Group:      Applications/System
License:    GPLv2
BuildArch:  noarch
URL:        https://github.com/scottchiefbaker/dool/
Source0:    %{name}-%{version}.tar.gz
Source100:  harbour-dool.yaml
Patch0:     PR1.patch
Patch1:     PR2.patch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3-rpm-macros
Provides:   dstat = %{version}
Provides:   harbour-dstat = %{version}
Obsoletes:   dstat < %{version}
Obsoletes:   harbour-dstat < %{version}

%description
Dool is a Python3 compatible clone of Dstat.
After Dag Wieers ceased development of Dstat scottchiefbaker forked the
project to continue development. Dool is a Python 2.x and 3.x compatible
version of Dstat with a couple minor bug fixes.

The Description for original dstat follows:

Dstat is a versatile replacement for vmstat, iostat, netstat and ifstat.
Dstat overcomes some of their limitations and adds some extra features,
more counters and flexibility. Dstat is handy for monitoring systems
during performance tuning tests, benchmarks or troubleshooting.

Dstat allows you to view all of your system resources in real-time, you
can eg. compare disk utilization in combination with interrupts from your
IDE controller, or compare the network bandwidth numbers directly
with the disk throughput (in the same interval).

Dstat gives you detailed selective information in columns and clearly
indicates in what magnitude and unit the output is displayed. Less
confusion, less mistakes. And most importantly, it makes it very easy
to write plugins to collect your own counters and extend in ways you
never expected.

%if "%{?vendor}" == "chum"
PackageName: dool (a.k.a. dstat)
DeveloperName: nephros
Type: console-application
Categories:
  - Utility
Screenshots:
  - https://gitlab.com/nephros/harbour-dstat/-/raw/master/screenshot.png
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# PR1.patch
%patch0 -p1
# PR2.patch
%patch1 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
sed -i -e "s@/usr/share/dool/@%{_datadir}/%{name}/plugins/@" dool
install -Dp -m0755 dool %{buildroot}/%{_bindir}/dool
install -d  -m0755 %{buildroot}/%{_datadir}/dool/
install -Dp -m0755 dool %{buildroot}/%{_datadir}/%{name}/dool.py
install -d  -m0755 %{buildroot}/%{_datadir}/%{name}/plugins/
install -Dp -m0644 plugins/dool_*.py %{buildroot}/%{_datadir}/%{name}/plugins/
# << install pre

# >> install post
# fix shebangs for python3:
find %{buildroot}%{_bindir} -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +
find %{buildroot}%{_datadir} -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

pushd %{buildroot}/%{_bindir}
ln -s dool dstat
popd
# << install post

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/dool
%{_bindir}/dstat
%{_datadir}/%{name}/
# >> files
# << files
