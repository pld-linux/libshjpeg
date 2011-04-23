Summary:	Hardware-accelerated JPEG encoder/decoder library for SH Mobile
Summary(pl.UTF-8):	Biblioteka sprzętowo wspomaganego kodera/dekodera JPEG dla SH Mobile
Name:		libshjpeg
Version:	1.3.5
%define	gitver	3b78698
Release:	1
License:	LGPL v2+
Group:		Libraries
# trailing /%{name}-%{version}.tar.gz is a hack for df
Source0:	https://github.com/dhobsong/libshjpeg/tarball/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1e19ff8dc908d518114fe237750d327b
Patch0:		%{name}-pc.patch
URL:		http://github.com/dhobsong/libshjpeg
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	libuiomux-devel >= 1.5.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
Requires:	libuiomux >= 1.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hardware-accelerated JPEG encoder/decoder library for SH Mobile.

%description -l pl.UTF-8
Biblioteka sprzętowo wspomaganego kodera/dekodera JPEG dla SH Mobile.

%package devel
Summary:	Header files for libshjpeg library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libshjpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libuiomux-devel >= 1.5.0

%description devel
Header files for libshjpeg library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libshjpeg.

%package static
Summary:	Static libshjpeg library
Summary(pl.UTF-8):	Statyczna biblioteka libshjpeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libshjpeg library.

%description static -l pl.UTF-8
Statyczna biblioteka libshjpeg.

%package apidocs
Summary:	libshjpeg API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libshjpeg
Group:		Documentation

%description apidocs
API and internal documentation for libshjpeg library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libshjpeg.

%prep
%setup -q -n dhobsong-%{name}-%{gitver}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig (with pc patch)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libshjpeg.la
# tests not packaged
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{libjpeg,shjpeg}test \
	$RPM_BUILD_ROOT%{_mandir}/man1/{libjpegtest,shjpegtest,shjpegshow}.1
# HTML packaged in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libshjpeg

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/v2mjpeg
%attr(755,root,root) %{_libdir}/libshjpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libshjpeg.so.1
%{_mandir}/man1/v2mjpeg.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libshjpeg.so
%{_includedir}/shjpeg
%{_pkgconfigdir}/shjpeg.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libshjpeg.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/libshjpeg/html/*
