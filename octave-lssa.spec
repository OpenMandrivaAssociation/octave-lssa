%global octpkg lssa

Summary:	Tools to compute spectral decompositions of irregularly-spaced time series
Name:		octave-lssa
Version:	0.1.4
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/lssa/
Source0:	https://downloads.sourceforge.net/octave/lssa-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.6.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Tools to compute spectral decompositions of irregularly-spaced time
series. Functions based on the Lomb-Scargle periodogram and Adolf

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

