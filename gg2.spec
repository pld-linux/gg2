#
# Conditional build:
%bcond_with	arts
%bcond_without	perl
%bcond_without	esd
%bcond_without	gtkspell
#
Summary:	GNU Gadu 2 - free talking
Summary(es):	GNU Gadu 2 - charlar libremente
Summary(pl):	GNU Gadu 2 - wolne gadanie
Name:		gg2
Version:	2.0
Release:	1
Epoch:		3
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://osdn.dl.sourceforge.net/ggadu/%{name}-%{version}.tar.bz2
# Source0-md5:	7a9a1e49c289b24758e5a347136ec81a
URL:		http://www.gnugadu.org/
%{?with_arts:BuildRequires:	arts-devel}
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
%{?with_esd:BuildRequires:	esound-devel >= 0.2.7}
BuildRequires:	gettext-devel >= 0.11.0
BuildRequires:	glib2-devel  >= 2.2.0
BuildRequires:	gtk+2-devel  >= 2.2.0
BuildRequires:	libtlen-devel
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 0.15.1
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_perl:BuildRequires:	perl-devel}
%{?with_gtkspell:BuildRequires:	gtkspell-devel}
%{?with_gtkspell:BuildRequires:	aspell-devel}
BuildRequires:	pkgconfig
BuildRequires:	xosd-devel   >= 2.0.0
Requires:	gg2-ui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gadu-Gadu, Tlen.pl and others instant messanger client with
GTK+2 GUI on GNU/GPL.

%description -l es
Un cliente para Gadu-Gadu, Tlen.pl y otros protocolos con un GUI de
GTK+2, bajo la licencia GNU/GPL.

%description -l pl
Klient Gadu-Gadu, Tlen.pl oraz innych protoko³ów z GUI pod GTK+2 na
licencji GNU/GPL.

%package devel
Summary:	Headers for libgg2_core library to develop plugins
Summary(es):	Cabeceras para la biblioteca libgg2_core para desarrollar plugins
Summary(pl):	Pliki nag³ówkowe biblioteki libgg2_core potrzebne do rozwijania wtyczek
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel
Requires:	perl-devel

%description devel
This package contains header files for libgg2_core library, needed to
develop plugins for GNU Gadu 2.

%description devel -l es
Este paquete contiene los ficheros de cabeceras de la biblioteca
libgg2_core necesarios para desarrollar plugins para GNU Gadu 2.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki libgg2_core, potrzebne
do rozwijania wtyczek do GNU Gadu 2.

%package gui-gtk+2
Summary:	GTK+2 GUI plugin
Summary(es):	Plugin de GUI en GTK+2
Summary(pl):	Wtyczka z GUI w GTK+2
Group:		Applications/Communications
Provides:	gg2-ui
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gui-gtk+2
GTK+2 GUI plugin for GNU Gadu 2.

%description gui-gtk+2 -l es
Un plugin con un GUI en GTK+2 para GNU Gadu 2.

%description gui-gtk+2 -l pl
Wtyczka z GUI w GTK+2 do GNU Gadu 2.

%package emoticons
Summary:	Emoticons
Summary(es):	Emoticons
Summary(pl):	Emotikony
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description emoticons
Emotions icons and description files.

%description emoticons -l es
Iconas de emociones y sus ficheros de descripción.

%description emoticons -l pl
Zestaw ikon z emotikonami, oraz plikiem konfiguracyjnym.

%package gadu-gadu
Summary:	Gadu-Gadu plugin
Summary(es):	Plugin de Gadu-Gadu
Summary(pl):	Wtyczka protoko³u Gadu-Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gadu-gadu
Gadu-Gadu protocol plugin.

%description gadu-gadu -l es
Un plugin para el protocolo Gadu-Gadu.

%description gadu-gadu -l pl
Wtyczka protoko³u Gadu-Gadu.

%package tlen
Summary:	Tlen.pl plugin
Summary(es):	Plugin de Tlen.pl
Summary(pl):	Wtyczka protoko³u Tlen.pl
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tlen
Tlen.pl protocol plugin.

%description tlen -l es
Un plugin para el protocolo Tlen.pl.

%description tlen -l pl
Wtyczka protoko³u Tlen.pl.

%package jabber
Summary:	Jabber.org plugin
Summary(es):	Plugin de Jabber.org
Summary(pl):	Wtyczka protoko³u Jabber
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description jabber
Jabber protocol plugin.

%description jabber -l es
Un plugin para el protocolo Jabber.

%description jabber -l pl
Wtyczka protoko³u Jabber.

%package sound-esd
Summary:	Sound support with ESD
Summary(es):	Soporte de sonido a través de ESD
Summary(pl):	Obs³uga d¼wiêku poprzez ESD
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sound-esd
Sound support with ESD.

%description sound-esd -l es
Soporte de sonido a través de ESD.

%description sound-esd -l pl
Obs³uga d¼wiêku poprzez ESD.

%package sound-oss
Summary:	OSS sound support
Summary(es):	Soporte de sonido a través de OSS
Summary(pl):	Obs³uga d¼wiêku OSS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sound-oss
OSS sound support.

%description sound-oss -l es
Soporte de sonido a través de OSS.

%description sound-oss -l pl
Obs³uga d¼wiêku OSS.

%package sound-external
Summary:	Sound support with external player
Summary(es):	Soporte de sonido vía un reproductor externo
Summary(pl):	Obs³uga d¼wiêku przez zewnêtrzny program
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sound-external
Sound support with external player.

%description sound-external -l es
Soporte de sonido a través de un reproductor externo.

%description sound-external -l pl
Obs³uga d¼wiêku przez zewnêtrzny program.

%package sound-aRts
Summary:	Sound support with aRts
Summary(es):	Soporte de sonido a través de aRts
Summary(pl):	Obs³uga d¼wiêku poprzez aRts
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description sound-aRts
Sound support with aRts.

%description sound-aRts -l es
Soporte de sonido a través de aRts.

%description sound-aRts -l pl
Obs³uga d¼wiêku poprzez aRts.

%package xosd
Summary:	Support for X On Screen Display
Summary(es):	Soporte para plasmar mensajes sobre el fondo de X
Summary(pl):	Wy¶wietlanie komunikatów na ekranie X
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description xosd
Support for X On Screen Display.

%description xosd -l es
Soporte para plasmar mensajes sobre el fondo (XOSD).

%description xosd -l pl
Wy¶wietlanie komunikatów na ekranie X.

%package docklet-system-tray
Summary:	Support for Window Managers notification areas
Summary(es):	Soporte para áreas de notificación de los Manejantes de Ventanas
Summary(pl):	Obs³uga obszarów powiadomieñ w ró¿nych zarz±dcach okien
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-docklet

%description docklet-system-tray
Support for Window Managers notification areas (GNOME, KDE).

%description docklet-system-tray -l es
Soporte para áreas de notificación de los Manejantes de Ventanas
(GNOME, KDE).

%description docklet-system-tray -l pl
Obs³uga obszarów powiadomieñ w ró¿nych zarz±dcach okien (GNOME, KDE).

%package docklet-dockapp
Summary:	Support for WindowMaker-style dockapp
Summary(es):	Soporte de dockapp estilo WindowMaker
Summary(pl):	Obs³uga dokowalnego apletu zgodnego z WindowMakerem
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-docklet

%description docklet-dockapp
Support for WindowMaker-style dockapp.

%description docklet-dockapp -l es
Suporte de dockapp estilo WindowMaker.

%description docklet-dockapp -l pl
Obs³uga dokowalnego apletu zgodnego z WindowMakerem.

%package sms
Summary:	SMS Gateway
Summary(es):	Puerta SMS
Summary(pl):	Bramka SMS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sms
Send SMS to cellular phones via web gateways.

%description sms -l es
Manda mensajes SMS a móviles vía puertas del Web.

%description sms -l pl
Wtyczka wysy³aj±ca wiadomo¶ci SMS na telefony komórkowe przez bramki
WWW.

%package remote
Summary:	Remote access from other applications
Summary(es):	Acceso remoto desde otras aplicaciones
Summary(pl):	Dostêp do programu z innych aplikacji
Group:		Applications/Communications
Provides:	gg2-ui
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description remote
Make possible exchange data with other applications.

%description remote -l es
Permite intercambiar los datos con otras aplicaciones.

%description remote -l pl
Wtyczka umo¿liwiaj±ca wymianê informacji z innymi aplikacjami.

%package update
Summary:	Check for new GNU Gadu newer version
Summary(es):	Verifica si hay versiones nuevas de GNU Gadu
Summary(pl):	Sprawdza czy jest dostêpna nowsza wersja GNU Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description update
Check for new GNU Gadu newer version.

%description update -l es
Verifica si hay nuevas versiones de GNU Gadu.

%description update -l pl
Sprawdza czy jest dostêpna nowsza wersja GNU Gadu

%package themes
Summary:	Themes for GNU Gadu 2 GUI
Summary(es):	Temas para el GUI de GNU Gadu 2
Summary(pl):	Motywy graficzne dla GUI GNU Gadu 2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-gui-gtk+2

%description themes
Themes for GNU Gadu 2 GUI.

%description themes -l es
Temas para el GUI de GNU Gadu 2.

%description themes -l pl
Motywy graficzne dla GUI GNU Gadu 2.

%prep
%setup -q -n %{name}-%{version}

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}

%configure \
	%{!?debug:--disable-gdb} \
	%{!?debug:--disable-debug} \
 	--with-gui \
 	--with-gadu \
 	--with-tlen \
 	--with-jabber \
 	--with-xosd \
 	--with-sms \
 	--with-docklet_system_tray \
	--with-docklet_dockapp \
	--with%{!?with_esd:out}-esd \
 	--with-oss \
 	--with-external \
 	--with-update \
	--with%{!?with_arts:out}-arts \
	--with%{!?with_gtkspell:out}-gtkspell \
	--%{?with_perl:with}%{!?with_perl:without}-perl \
 	--with-remote

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install gg2.desktop $RPM_BUILD_ROOT%{_desktopdir}/gg2.desktop

%find_lang %{name} --all-name --with-gnome

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc A* C* N* R* T* contrib doc/*
%attr(755,root,root) %{_bindir}/gg2
%attr(755,root,root) %{_libdir}/libgg2_core.so.*.*.*
%dir %{_libdir}/gg2
%{_datadir}/%{name}/sounds

%files gui-gtk+2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libGUI_plugin.so
%dir %{_datadir}/gg2
%dir %{_datadir}/gg2/pixmaps
%{_datadir}/gg2/pixmaps/*.png
%{_datadir}/gg2/pixmaps/*.gif
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/gg2.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgg2_core.so
%{_libdir}/libgg2_core.la
%{_includedir}/gg2_core.h
%{_pkgconfigdir}/gg2_core.pc

%files emoticons
%defattr(644,root,root,755)
%{_datadir}/gg2/pixmaps/emoticons

%files gadu-gadu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libgadu_gadu_plugin.so

%files tlen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libtlen_plugin.so

%files jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libjabber_plugin.so

%if %{with esd}
%files sound-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_esd_plugin.so
%endif

%files sound-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_oss_plugin.so

%files sound-external
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_external_plugin.so

%if %{with arts}
%files sound-aRts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_arts_plugin.so
%endif

%files xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libxosd_plugin.so

%files docklet-system-tray
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdocklet_system_tray_plugin.so

%files docklet-dockapp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdocklet_dockapp_plugin.so

%files sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsms_plugin.so

%files remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libremote_plugin.so

%files update
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libupdate_plugin.so

%files themes
%defattr(644,root,root,755)
%dir %{_datadir}/gg2/themes
%{_datadir}/gg2/themes/*.theme
%dir %{_datadir}/gg2/pixmaps/icons
%dir %{_datadir}/gg2/pixmaps/icons/bubble
%dir %{_datadir}/gg2/pixmaps/icons/classic
%dir %{_datadir}/gg2/pixmaps/icons/modern
%dir %{_datadir}/gg2/pixmaps/icons/rozgwiazda
%{_datadir}/gg2/pixmaps/icons/bubble/*.png
%{_datadir}/gg2/pixmaps/icons/bubble/README
%{_datadir}/gg2/pixmaps/icons/classic/*.png
%{_datadir}/gg2/pixmaps/icons/classic/README
%{_datadir}/gg2/pixmaps/icons/modern/*.png
%{_datadir}/gg2/pixmaps/icons/modern/README
%{_datadir}/gg2/pixmaps/icons/rozgwiazda/*.png
%{_datadir}/gg2/pixmaps/icons/rozgwiazda/license.txt
%{_datadir}/gg2/pixmaps/icons/ghosts/*.png
%{_datadir}/gg2/pixmaps/icons/ghosts/README
%{_datadir}/gg2/pixmaps/icons/tlen-3d/README
%{_datadir}/gg2/pixmaps/icons/tlen-3d/*.png
