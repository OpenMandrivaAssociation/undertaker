%define name    undertaker
%define version 1.0
%define release %mkrel 1

Name:           %{name}
Summary:	Software configuration variability verifier
Version:        %{version}
Release:        %{release}
Source0:	http://vamos.informatik.uni-erlangen.de/files/%{name}-%{version}.tar.gz
Patch0:		0001-Fixing-Makefile-to-use-LIBDIR.patch
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
%setup -n vamos
%patch0 -p1

%build
#configure
%make

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
%{_libdir}/%{name}/dumpconf
%{_libdir}/%{name}/rsf2model
%{_libdir}/%{name}/%{name}-scan-head

%files -n	%{name}-emacs
%defattr(-,root,root,-)
%{_datadir}/emacs/site-lisp/%{name}/%{name}.el