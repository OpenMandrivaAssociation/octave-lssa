%define octpkg lssa

# fix debuginfo-without-sources
%define debug_package %{nil}

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Spectral decompositions of irregularly-spaced time serie with Octave
Name:		octave-%{octpkg}
Version:	0.1.2
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://sourceforge.net/p/octave/lssa/ci/59af0bcd5cafce29162db3dfc42dcf326f56d8be/
Patch0:		%{name}-0.1.2-fastlscomplex.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.6.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A package implementing tools to compute spectral decompositions of
irregularly-spaced time series.  Currently includes functions based off the
Lomb-Scargle periodogram and Adolf Mathias' implementation for R and C (see
URLs). 

This package is part of community Octave-Forge collection.

%prep
%setup -q -c %{octpkg}-%{version}
cp %SOURCE0 .

# Apply patch
pushd %{octpkg}
%patch0 -p1
popd

%build
%octave_pkg_build #-T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

