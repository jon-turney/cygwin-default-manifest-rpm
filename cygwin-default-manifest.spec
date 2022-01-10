%{?cygwin_package_header}

Name:      cygwin-default-manifest
Version:   6.4
Release:   4%{?dist}
Summary:   Default application manifests for Cygwin toolchains

Group:     Development/Libraries
License:   Copyright only
URL:       http://cygwin.com/
BuildArch: noarch

# use get-sources.sh to download from cvs tag
Source0:   windows-default-manifest-%{version}.tar.xz

BuildRequires: autoconf automake
BuildRequires: cygwin32-filesystem
BuildRequires: cygwin32-binutils
BuildRequires: cygwin32-gcc
BuildRequires: cygwin64-filesystem
BuildRequires: cygwin64-binutils
BuildRequires: cygwin64-gcc
BuildRequires: make


%description
This package provides a default application manifest for those applications
without their own.  This manifest avoids UAC installer detection of programs
with certain names, and declares the application compatible with all current
versions of Windows.  Since Windows 8.1 and Windows Server 2012 R2,
applications without compatibility manifests are treated as compatible with
the oldest supported version of Windows (e.g. Vista).

%package -n cygwin32-default-manifest
Summary:   Default application manifests for Cygwin32 toolchain
Group:     Development/Libraries

%description -n cygwin32-default-manifest
%{description}

%package -n cygwin64-default-manifest
Summary:   Default application manifests for Cygwin64 toolchain
Group:     Development/Libraries

%description -n cygwin64-default-manifest
%{description}


%prep
%setup -q -n windows-default-manifest-%{version}
autoreconf -fiv


%build
%cygwin_configure
%cygwin_make %{?_smp_mflags}


%install
%cygwin_make install DESTDIR=$RPM_BUILD_ROOT


%files -n cygwin32-default-manifest
%doc COPYING README
%{cygwin32_libdir}/default-manifest.o

%files -n cygwin64-default-manifest
%doc COPYING README
%{cygwin64_libdir}/default-manifest.o


%changelog
* Mon Jan 10 2022 Yaakov Selkowitz <yselkowi@redhat.com> - 6.4-4
- rebuilt

* Wed Nov 15 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 6.4-3
- rebuilt

* Mon Feb 22 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 6.4-2
- rebuilt

* Sun Nov 02 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 6.4-1
- Version bump

* Fri Jun 27 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 6.3-1
- Initial release
