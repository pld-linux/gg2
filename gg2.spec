
%define		snap 20021123

Summary:	GNU Gadu - free talking for GTK+2
Summary(pl):	GNU Gadu - wolne gadanie dla GTK+2
Name:		gg2
Version:	0
Release:	0.%{snap}
License:	GPL
Group:		Applications/Communications
#No source for now, only snapshots
Source0:	%{name}-%{snap}.tar.bz2
URL:		http://gadu.gnu.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtlen
BuildRequires:	libgadu
BuildRequires:	gnome-panel-devel
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
Gadu-Gadu and Tlen.pl GTK+2 client released on GNU/GPL.

%description -l pl
Klient Gadu-Gadu i Tlen.pl dla GTK+2 na licencji GNU/GPL.

%prep
%setup -q -n %{name}-%{snap}

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-docklet 
	--with-esd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
