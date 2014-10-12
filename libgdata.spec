Summary:	GData access library
Name:		libgdata
Version:	0.16.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/0.16/%{name}-%{version}.tar.xz
# Source0-md5:	30200bd24c04fa85fd104c1d03129161
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcr-devel >= 3.14.0
BuildRequires:	gettext
BuildRequires:	glib-gio-devel >= 1:2.42.0
BuildRequires:	gnome-online-accounts-devel >= 3.14.0
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libgnome-keyring-devel >= 3.12.0
BuildRequires:	liboauth-devel
BuildRequires:	libsoup-devel >= 2.46.0
BuildRequires:	libtool
BuildRequires:	libuhttpmock-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgdata is a GLib-based library for accessing online service APIs
using the GData protocol - most notably, Google's services. It
provides APIs to access the common Google services, and has full
asynchronous support.

%package devel
Summary:	Support files necessary to compile applications with libgdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers, and support files necessary to compile applications using
libgdata.

%package apidocs
Summary:	libgdata API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgdata API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang gdata

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files -f gdata.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %ghost %{_libdir}/libgdata.so.??
%attr(755,root,root) %{_libdir}/libgdata.so.*.*.*
%{_libdir}/girepository-1.0/GData-0.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdata.so
%{_includedir}/libgdata
%{_pkgconfigdir}/libgdata.pc
%{_datadir}/gir-1.0/GData-0.0.gir
%{_datadir}/vala/vapi/libgdata.deps
%{_datadir}/vala/vapi/libgdata.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdata

