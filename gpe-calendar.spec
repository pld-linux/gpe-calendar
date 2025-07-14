Summary:	GPE calendar
Summary(pl.UTF-8):	Kalendarz GPE
Name:		gpe-calendar
Version:	0.90
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	e2834f77e3e9a476fd9a114411cdfa22
Patch0:		%{name}-link.patch
URL:		http://gpe.linuxtogo.org/projects/GPE-calendar.shtml
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	intltool >= 0.23
BuildRequires:	libeventdb-devel >= 0.90
BuildRequires:	libgpepimc-devel
BuildRequires:	libgpevtype-devel >= 0.50
BuildRequires:	libgpewidget-devel >= 0.109
BuildRequires:	libhandoff-devel
BuildRequires:	libmimedir-devel
BuildRequires:	libschedule-devel
BuildRequires:	libsoup-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	libxsettings-client-devel >= 0.16
BuildRequires:	pkgconfig
BuildRequires:	sqlite-devel
# optional: hildon-libs hildon-fm libosso
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE calendar, for embedded devices.

%description -l pl.UTF-8
Kalendarz GPE dla urządzeń wbudowanych.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
