%global octpkg lssa

Summary:	Spectral decompositions of irregularly-spaced time serie with Octave
Name:		octave-%{octpkg}
Version:	0.1.4
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://sourceforge.net/p/octave/lssa/ci/59af0bcd5cafce29162db3dfc42dcf326f56d8be/
#Patch0:		%{name}-0.1.2-fastlscomplex.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/

BuildRequires:	octave-devel >= 3.6.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A package implementing tools to compute spectral decompositions of
irregularly-spaced time series.  Currently includes functions based off the
Lomb-Scargle periodogram and Adolf Mathias' implementation for R and C (see
URLs). 

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

