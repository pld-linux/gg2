
%define		snap 20021204

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
#BuildRequires:	arts-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	glib2-devel  >= 2.0.1
BuildRequires:	gtk+2-devel  >= 2.0.1
BuildRequires:	libgadu-devel >= 20021123
BuildRequires:	libtlen-devel
BuildRequires:	libtool
BuildRequires:	xosd-devel   >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Gadu-Gadu and Tlen.pl and any other instant messanger client with
GTK+2 GUI on GNU/GPL.

%description -l pl
Klient Gadu-Gadu i Tlen.pl oraz innych protoko³ów z GUI pod GTK+2 na
licencji GNU/GPL.

%package gui-gtk+2
Summary:	GTK+2 GUI plugin
Summary(pl):	Wtyczka z GUI w GTK+2
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description gui-gtk+2
GTK+2 GUI plugin for GNU Gadu 2.

%description gui-gtk+2 -l pl
Wtyczka z GUI w GTK+2 do GNU Gadu 2.

%package emoticons
Summary:	Emoticons
Summary(pl):	Emotikony
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description emoticons
Emotions icons and description files.

%description emoticons -l pl
Zestaw ikon z emotikonami, oraz plikiem konfiguracyjnym.

%package gadu-gadu
Summary:	Gadu-Gadu plugin
Summary(pl):	Wtyczka protoko³u Gadu-Gadu
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description gadu-gadu
Gadu-Gadu protocol plugin.

%description gadu-gadu -l pl
Wtyczka protoko³u Gadu-Gadu.

%package tlen
Summary:	Tlen.pl plugin
Summary(pl):	Wtyczka protoko³u Tlen.pl
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description tlen
Tlen.pl protocol plugin.

%description tlen -l pl
Wtyczka protoko³u Tlen.pl.

%package sound-esd
Summary:	Sound support with ESD
Summary(pl):	Obs³uga d¼wiêku poprzez ESD
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description sound-esd
Sound support with ESD.

%description sound-esd -l pl
Obs³uga d¼wiêku poprzez ESD.

%package sound-oss
Summary:	OSS sound support
Summary(pl):	Obs³uga d¼wiêku OSS
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description sound-oss
OSS sound support.

%description sound-oss -l pl
Obs³uga d¼wiêku OSS.

#%package sound-aRts
#Summary:	Sound support with aRts
#Summary(pl):	Obs³uga d¼wiêku poprzez aRts
#Group:		Applications/Communications
#Requires:	%{name} = %{version}

#%description sound-aRts
#Sound support with aRts.

#%description sound-aRts -l pl
#Obs³uga d¼wiêku poprzez aRts.

%package xosd
Summary:	Support for X On Screen Display
Summary(pl):	Wy¶wietlanie komunikatów na ekranie X
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description xosd
Support for X On Screen Display.

%description xosd -l pl
Wy¶wietlanie komunikatów na ekranie X.

%package docklet
Summary:	Support for Window Managers docklets
Summary(pl):	Obs³uga dokletów w ró¿nych zarz±dcach okien
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description docklet
Support for Window Managers docklets (GNOME, KDE)

%description docklet -l pl
Obs³uga dokletów w ró¿nych zarz±dcach okien (GNOME, KDE)

%prep
%setup -q -n %{name}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}

%configure \
	--disable-gdb \
	--disable-debug \
	--with-gtk2-gui \
	--with-gadu-gadu \
	--with-tlen \
	--with-xosd \
	--with-docklet \
	--with-esd \
	--with-oss
#	--with-arts

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gg2
%dir %{_libdir}/gg2

%files gui-gtk+2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libGUI_plugin.so
%dir %{_datadir}/gg2
%dir %{_datadir}/gg2/pixmaps
%{_datadir}/gg2/pixmaps/*xpm
%{_datadir}/gg2/pixmaps/*png
%{_datadir}/gg2/pixmaps/*gif

%files emoticons
%attr(755,root,root) %{_datadir}/gg2/pixmaps/emoticons

%files gadu-gadu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libgadu_gadu_plugin.so

%files tlen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libtlen_plugin.so

%files sound-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_esd_plugin.so

%files sound-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_oss_plugin.so

%files xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libxosd_plugin.so

%files docklet
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdocklet_plugin.so
