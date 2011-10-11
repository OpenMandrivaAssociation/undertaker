%define name    undertaker
%define version 1.2
%define release 2

Name:           %{name}
Summary:	Software configuration variability verifier
Version:        %{version}
Release:        %{release}
Source0:	http://vamos.informatik.uni-erlangen.de/files/%{name}-%{version}.tar.gz
URL:            http://vamos.informatik.uni-erlangen.de/trac/undertaker
Group:          Development/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv3
BuildRequires:	check-devel
BuildRequires:	boost-devel
BuildRequires:	picosat-devel

%description
Topic of the project is variability of system software evoked by the
non-functional properties of operating-system functions, which emerges from
(a) different implementations of the same system function to make an
appearance of certain non-functional properties and
(b) the using level of those implementations in order to compensate for
effects of these properties.

With this project, the undertaker, we provide tools to examine and evaluate
CPP based source files. See
http://www4.informatik.uni-erlangen.de/Research/VAMOS/publications.shtml for
a list of publications. 

%package -n	%{name}-emacs
Group:		Development/Other
Summary:	Emacs mode for undertaker, a variability verifier

%description -n	%{name}-emacs
Emacs mode for the Undertaker analyzing tool.

%prep
%setup -q -n vamos-%{version}

%build
#configure
%make CXX="g++ %optflags -DBOOST_FILESYSTEM_VERSION=2"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std PREFIX=%{_prefix} LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/%{name}-kconfigdump
%{_bindir}/%{name}-linux-tree
%{_bindir}/%{name}-calc-coverage
%{_bindir}/rsf2model
%{_bindir}/zizler
%{_libdir}/%{name}/rsf2model
%{_libdir}/%{name}/dumpconf
%{_libdir}/%{name}/%{name}-scan-head
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}*.egg-info
%{_mandir}/man1/%{name}*

%files -n	%{name}-emacs
%defattr(-,root,root,-)
%{_datadir}/emacs/site-lisp/%{name}/%{name}.el
