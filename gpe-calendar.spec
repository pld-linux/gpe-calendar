Summary:	GPE calendar
Summary(pl.UTF-8):	Kalendarz GPE
Name:		gpe-calendar
Version:	0.72
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	b10a91ce3fb39b87656fc5c5510b68d6
URL:		http://gpe.linuxtogo.org/projects/GPE-calendar.shtml
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libeventdb-devel
BuildRequires:	libgpepimc-devel
BuildRequires:	libgpevtype-devel
BuildRequires:	libgpewidget-devel
BuildRequires:	libmimedir-devel
BuildRequires:	libschedule-devel
BuildRequires:	libxsettings-client-devel
BuildRequires:	pkgconfig
BuildRequires:  sed >= 4.0
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define gpename %(echo %{name} | sed -e 's/gpe-//')

%description
GPE calendar, for embedded devices.

%description -l pl.UTF-8
Kalendarz GPE dla urządzeń wbudowanych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/application-registry/%{name}.applications
%{_desktopdir}/%{name}.desktop
%dir %{_datadir}/gpe/pixmaps/default/%{gpename}
%{_datadir}/gpe/pixmaps/default/%{gpename}/*.png
%{_pixmapsdir}/%{name}.png
