
%define		snap pre0

Summary:	GNU Gadu 2 - free talking
Summary(pl):	GNU Gadu 2 - wolne gadanie
Name:		gg2
Version:	%{snap}
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
#Source0:	http://www.hakore.com/~krzak/gg2/%{name}-%{snap}.tar.gz
Source0:	ftp://ftp.slackware.pl/gg/%{name}-2.0%{snap}.tar.gz
Source1:	%{name}.desktop
URL:		http://gadu.gnu.pl/
#BuildRequires:	arts-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	iksemel-devel >= 0.0.1
BuildRequires:	glib2-devel  >= 2.1.0
BuildRequires:	gtk+2-devel  >= 2.1.0
BuildRequires:	libgadu-devel >= 20030101
BuildRequires:	libtlen-devel
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	xosd-devel   >= 2.0.0
BuildRequires:  pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package jabber
Summary:	Jabber.org plugin
Summary(pl):	Wtyczka protoko³u Jabber
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description jabber
Jabber protocol plugin.

%description jabber -l pl
Wtyczka protoko³u Jabber.org.

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

%package themes
Summary:	Themes for GnuGadu 2 GUI
Summary(pl):	Tematy graficzne dla GUI GnuGadu 2
Group:		Applications/Communications
Requires:       %{name} = %{version}
Requires:	%{name}-gui-gtk+2

%description themes
Themes for GnuGadu 2 GUI

%description themes
Tematy graficzne dla GUI GnuGadu 2

%prep
%setup -q -n %{name}-2.0%{snap}

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
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
	--with-jabber \
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

install -d $RPM_BUILD_ROOT%{_datadir}/applications
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/
install $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps/online.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gg2
%dir %{_libdir}/gg2
%{_datadir}/%{name}/sounds

%files gui-gtk+2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libGUI_plugin.so
%dir %{_datadir}/gg2
%dir %{_datadir}/gg2/pixmaps
%{_datadir}/gg2/pixmaps/*xpm
%{_datadir}/gg2/pixmaps/*png
%{_datadir}/gg2/pixmaps/*gif

%{_pixmapsdir}/%{name}.xpm
%{_datadir}/applications/gg2.desktop

%files emoticons
%attr(755,root,root) %{_datadir}/gg2/pixmaps/emoticons

%files gadu-gadu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libgadu_gadu_plugin.so

%files tlen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libtlen_plugin.so

%files jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libjabber_plugin.so

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

%files themes
%defattr(644,root,root,755)
%dir %{_datadir}/gg2/themes
%{_datadir}/gg2/themes/*theme
%dir %{_datadir}/gg2/pixmaps/icons
%dir %{_datadir}/gg2/pixmaps/icons/bubble
%dir %{_datadir}/gg2/pixmaps/icons/classic
%dir %{_datadir}/gg2/pixmaps/icons/modern
%{_datadir}/gg2/pixmaps/icons/bubble/*.png
%{_datadir}/gg2/pixmaps/icons/classic/*.png
%{_datadir}/gg2/pixmaps/icons/modern/*.png
