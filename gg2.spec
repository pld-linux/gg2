
%define		snap 20021123

Summary:	GNU Gadu 2 - free talking
Summary(pl):	GNU Gadu 2 - wolne gadanie
Name:		gg2
Version:	%{snap}
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.hakore.com/~krzak/gg2/%{name}-%{snap}.tar.bz2
URL:		http://gadu.gnu.pl/
BuildRequires:	automake
BuildRequires:	libtool
Requires:	glib2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Gadu-Gadu and Tlen.pl and any other instant messanger client with
GTK+2 GUI on GNU/GPL

%description -l pl
Klient Gadu-Gadu i Tlen.pl oraz innych protokolow z GUI w GTK+2 na
licencji GNU/GPL

%package gui-gtk+2
Summary:	GTK+2 GUI plugin
Summary(pl):	GTK+2 GUI plugin
Group:		Applications/Communications
BuildRequires:	gtk+2-devel
Requires:	gtk+2
Requires:	%{name} = %{version}

%description gui-gtk+2
GTK+2 GUI plugin

%description gui-gtk+2 -l pl
GTK+2 GUI plugin



%package gadu-gadu
Summary:	Gadu-Gadu plugin
Summary(pl):	Gadu-Gadu plugin
Group:		Applications/Communications
BuildRequires:	libgadu-devel
Requires:	libgadu
Requires:	%{name} = %{version}

%description gadu-gadu
Gadu-Gadu protocol plugin

%description -l pl
Plugin protokolu Gadu-Gadu



%package tlen
Summary:	Tlen.pl plugin
Summary(pl):	Tlen.pl plugin
Group:		Applications/Communications
BuildRequires:	libtlen-devel
Requires:	libtlen
Requires:	%{name} = %{version}

%description tlen
Tlen.pl protocol plugin

%description tlen -l pl
Plugin protokolu Tlen.pl


%package sound-esd
Summary:	Sound support with ESD
Summary(pl):	Obsluga dzwieku z ESD
Group:		Applications/Communications
BuildRequires:	esound-devel
Requires:	esound
Requires:	%{name} = %{version}

%description sound-esd
Sound support with ESD

%description sound-esd -l pl
Obsluga dzwieku z ESD


#%package sound-aRts
#Summary:	Sound support with aRts
#Summary(pl):	Obsluga dzwieku z aRts
#Group:		Applications/Communications
#BuildRequires:	arts-devel
#Requires:	arts
#Requires:	%{name} = %{version}

#%description sound-aRts
#Sound support with aRts

#%description sound-aRts -l pl
#Obsluga dzwieku z aRts


%package xosd
Summary:	Support for X On Screen Display
Summary(pl):	Wyswietlanie komunikatow na ekranie
Group:		Applications/Communications
BuildRequires:	xosd-devel
Requires:	xosd
Requires:	%{name} = %{version}

%description xosd
Support for X On Screen Display

%description xosd -l pl
Wyswietlanie komunikatow na ekranie


%package docklet
Summary:	Support for Window Managers docklets
Summary(pl):	Obsluga dockletow w roznych menadzerach okien
Group:		Applications/Communications
Requires:	XFree86-libs
Requires:	%{name} = %{version}

%description docklet
Support for Window Managers docklets

%description docklet -l pl
Obsluga dockletow w roznych menadzerach okien


%prep
%setup -q -n %{name}


%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}

%configure \
	--with-gtk2-gui \
	--with-gadu-gadu \
	--with-tlen \
	--with-xosd \
	--with-docklet \
	--with-esd
#	--with-arts

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gg2
%attr(755,root,root) %{_datadir}/gg2/pixmaps/*xpm
%attr(755,root,root) %{_datadir}/gg2/pixmaps/*png

%files gui-gtk+2
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/gg2/libGUI_plugin.so
%attr(755,root,root) %{_datadir}/gg2/pixmaps/emoticons/*

%files gadu-gadu
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/gg2/libgadu_gadu_plugin.so

%files tlen
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/gg2/libtlen_plugin.so

%files sound-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/gg2/libsound_esd_plugin.so

%files xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/gg2/libxosd_plugin.so
