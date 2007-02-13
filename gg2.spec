#
# Conditional build: 
%bcond_without	arts		# without aRts sound support
%bcond_without	esd		# without EsounD sound support
%bcond_without	dbus		# without DBUS support
%bcond_without	gtkspell	# without gtkspell support
%bcond_without	xosd		# without xosd support
%bcond_with	perl		# with perl support
#
Summary:	GNU Gadu 2 - free talking
Summary(es.UTF-8):	GNU Gadu 2 - charlar libremente
Summary(pl.UTF-8):	GNU Gadu 2 - wolne gadanie
Name:		gg2
Version:	2.3.0
Release:	1
Epoch:		3
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/ggadu/%{name}-%{version}.tar.bz2
# Source0-md5:	dbe6c0f85c9dbb115ee1911d8abbea33
URL:		http://www.gnugadu.org/
Patch0:		%{name}-desktop.patch
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_gtkspell:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.33}
%{?with_esd:BuildRequires:	esound-devel >= 0.2.7}
BuildRequires:	gettext-devel >= 0.11.0
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.4.0
%{?with_gtkspell:BuildRequires:	gtkspell-devel}
BuildRequires:	libtlen-devel
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 0.17.1
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	pkgconfig
%{?with_xosd:BuildRequires:	xosd-devel >= 2.0.0}
BuildRequires:	xorg-lib-libXScrnSaver-devel
%if %{with perl}
BuildRequires:	perl-devel
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
%endif
Requires:	gg2-ui
Obsoletes:	gg-common
Obsoletes:	gg-kde
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gadu-Gadu, Tlen.pl and others instant messenger client with
GTK+2 GUI on GNU/GPL.

%description -l es.UTF-8
Un cliente para Gadu-Gadu, Tlen.pl y otros protocolos con un GUI de
GTK+2, bajo la licencia GNU/GPL.

%description -l pl.UTF-8
Klient Gadu-Gadu, Tlen.pl oraz innych protokołów z GUI pod GTK+2 na
licencji GNU/GPL.

%package devel
Summary:	Headers for libgg2_core library to develop plugins
Summary(es.UTF-8):	Cabeceras para la biblioteca libgg2_core para desarrollar plugins
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgg2_core potrzebne do rozwijania wtyczek
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel
Requires:	perl-devel

%description devel
This package contains header files for libgg2_core library, needed to
develop plugins for GNU Gadu 2.

%description devel -l es.UTF-8
Este paquete contiene los ficheros de cabeceras de la biblioteca
libgg2_core necesarios para desarrollar plugins para GNU Gadu 2.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libgg2_core, potrzebne
do rozwijania wtyczek do GNU Gadu 2.

%package plugin-gui-gtk+2
Summary:	GTK+2 GUI plugin
Summary(es.UTF-8):	Plugin de GUI en GTK+2
Summary(pl.UTF-8):	Wtyczka z GUI w GTK+2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-ui
Provides:	gg2-gui-gtk+2 = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-gui-gtk+2
Obsoletes:	gg-gnome

%description plugin-gui-gtk+2
GTK+2 GUI plugin for GNU Gadu 2.

%description plugin-gui-gtk+2 -l es.UTF-8
Un plugin con un GUI en GTK+2 para GNU Gadu 2.

%description plugin-gui-gtk+2 -l pl.UTF-8
Wtyczka z GUI w GTK+2 do GNU Gadu 2.

%package emoticons
Summary:	Emoticons
Summary(es.UTF-8):	Emoticons
Summary(pl.UTF-8):	Emotikony
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description emoticons
Emotions icons and description files.

%description emoticons -l es.UTF-8
Iconas de emociones y sus ficheros de descripción.

%description emoticons -l pl.UTF-8
Zestaw ikon z emotikonami, oraz plikiem konfiguracyjnym.

%package plugin-gadu-gadu
Summary:	Gadu-Gadu plugin
Summary(es.UTF-8):	Plugin de Gadu-Gadu
Summary(pl.UTF-8):	Wtyczka protokołu Gadu-Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-gadu-gadu = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-gadu-gadu

%description plugin-gadu-gadu
Gadu-Gadu protocol plugin.

%description plugin-gadu-gadu -l es.UTF-8
Un plugin para el protocolo Gadu-Gadu.

%description plugin-gadu-gadu -l pl.UTF-8
Wtyczka protokołu Gadu-Gadu.

%package plugin-tlen
Summary:	Tlen.pl plugin
Summary(es.UTF-8):	Plugin de Tlen.pl
Summary(pl.UTF-8):	Wtyczka protokołu Tlen.pl
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-tlen = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-tlen

%description plugin-tlen
Tlen.pl protocol plugin.

%description plugin-tlen -l es.UTF-8
Un plugin para el protocolo Tlen.pl.

%description plugin-tlen -l pl.UTF-8
Wtyczka protokołu Tlen.pl.

%package plugin-jabber
Summary:	Jabber.org plugin
Summary(es.UTF-8):	Plugin de Jabber.org
Summary(pl.UTF-8):	Wtyczka protokołu Jabber
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	loudmouth >= 0.16-4
Provides:	gg2-jabber = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-jabber

%description plugin-jabber
Jabber protocol plugin.

%description plugin-jabber -l es.UTF-8
Un plugin para el protocolo Jabber.

%description plugin-jabber -l pl.UTF-8
Wtyczka protokołu Jabber.

%package plugin-sound-esd
Summary:	Sound support with ESD
Summary(es.UTF-8):	Soporte de sonido a través de ESD
Summary(pl.UTF-8):	Obsługa dźwięku poprzez ESD
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-sound-esd = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-sound-esd

%description plugin-sound-esd
Sound support with ESD.

%description plugin-sound-esd -l es.UTF-8
Soporte de sonido a través de ESD.

%description plugin-sound-esd -l pl.UTF-8
Obsługa dźwięku poprzez ESD.

%package plugin-sound-oss
Summary:	OSS sound support
Summary(es.UTF-8):	Soporte de sonido a través de OSS
Summary(pl.UTF-8):	Obsługa dźwięku OSS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound-oss = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sound-oss

%description plugin-sound-oss
OSS sound support.

%description plugin-sound-oss -l es.UTF-8
Soporte de sonido a través de OSS.

%description plugin-sound-oss -l pl.UTF-8
Obsługa dźwięku OSS.

%package plugin-sound-external
Summary:	Sound support with external player
Summary(es.UTF-8):	Soporte de sonido vía un reproductor externo
Summary(pl.UTF-8):	Obsługa dźwięku przez zewnętrzny program
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-sound-external = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-sound-external

%description plugin-sound-external
Sound support with external player.

%description plugin-sound-external -l es.UTF-8
Soporte de sonido a través de un reproductor externo.

%description plugin-sound-external -l pl.UTF-8
Obsługa dźwięku przez zewnętrzny program.

%package plugin-sound-aRts
Summary:	Sound support with aRts
Summary(es.UTF-8):	Soporte de sonido a través de aRts
Summary(pl.UTF-8):	Obsługa dźwięku poprzez aRts
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-sound-aRts = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-sound-aRts

%description plugin-sound-aRts
Sound support with aRts.

%description plugin-sound-aRts -l es.UTF-8
Soporte de sonido a través de aRts.

%description plugin-sound-aRts -l pl.UTF-8
Obsługa dźwięku poprzez aRts.

%package plugin-xosd
Summary:	Support for X On Screen Display
Summary(es.UTF-8):	Soporte para plasmar mensajes sobre el fondo de X
Summary(pl.UTF-8):	Wyświetlanie komunikatów na ekranie X
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-xosd = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-xosd

%description plugin-xosd
Support for X On Screen Display.

%description plugin-xosd -l es.UTF-8
Soporte para plasmar mensajes sobre el fondo (XOSD).

%description plugin-xosd -l pl.UTF-8
Wyświetlanie komunikatów na ekranie X.

%package plugin-docklet-system-tray
Summary:	Support for Window Managers notification areas
Summary(es.UTF-8):	Soporte para áreas de notificación de los Manejantes de Ventanas
Summary(pl.UTF-8):	Obsługa obszarów powiadomień w różnych zarządcach okien
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-docklet-system-tray = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-docklet-system-tray
Obsoletes:	gg2-docklet

%description plugin-docklet-system-tray
Support for Window Managers notification areas (GNOME, KDE).

%description plugin-docklet-system-tray -l es.UTF-8
Soporte para áreas de notificación de los Manejantes de Ventanas
(GNOME, KDE).

%description plugin-docklet-system-tray -l pl.UTF-8
Obsługa obszarów powiadomień w różnych zarządcach okien (GNOME, KDE).

%package plugin-docklet-dockapp
Summary:	Support for WindowMaker-style dockapp
Summary(es.UTF-8):	Soporte de dockapp estilo WindowMaker
Summary(pl.UTF-8):	Obsługa dokowalnego apletu zgodnego z WindowMakerem
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-docklet-dockapp = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-docklet-dockapp
Obsoletes:	gg2-docklet
Obsoletes:	gg-gnome-applet
Obsoletes:	gg-wm-applet

%description plugin-docklet-dockapp
Support for WindowMaker-style dockapp.

%description plugin-docklet-dockapp -l es.UTF-8
Suporte de dockapp estilo WindowMaker.

%description plugin-docklet-dockapp -l pl.UTF-8
Obsługa dokowalnego apletu zgodnego z WindowMakerem.

%package plugin-sms
Summary:	SMS Gateway
Summary(es.UTF-8):	Puerta SMS
Summary(pl.UTF-8):	Bramka SMS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-sms = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-sms

%description plugin-sms
Send SMS to cellular phones via web gateways.

%description plugin-sms -l es.UTF-8
Manda mensajes SMS a móviles vía puertas del Web.

%description plugin-sms -l pl.UTF-8
Wtyczka wysyłająca wiadomości SMS na telefony komórkowe przez bramki
WWW.

%package plugin-history-external
Summary:	Allow to view GNU Gadu chat history
Summary(pl.UTF-8):	Przeglądanie historii rozmów GNU Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2
Provides:	gg2-history-external = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-history-external

%description plugin-history-external
Allow to view GNU Gadu chat history.

%description plugin-history-external -l pl.UTF-8
Wtyczka pozwalająca przeglądać historię rozmów GNU Gadu.

%package plugin-update
Summary:	Check for new GNU Gadu newer version
Summary(es.UTF-8):	Verifica si hay versiones nuevas de GNU Gadu
Summary(pl.UTF-8):	Sprawdzanie dostępności nowszej wersji GNU Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-update = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-update

%description plugin-update
Check for new GNU Gadu newer version.

%description plugin-update -l es.UTF-8
Verifica si hay nuevas versiones de GNU Gadu.

%description plugin-update -l pl.UTF-8
Wtyczka sprawdzająca, czy jest dostępna nowsza wersja GNU Gadu.

%package plugin-dbus
Summary:	Allow to communicate using D-BUS message bus
Summary(pl.UTF-8):	Komunikacja za pomocą magistrali D-BUS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-dbus
This plugin allows to communicate using D-BUS interface.

%description plugin-dbus -l pl.UTF-8
Wtyczka pozwala na komunikację za pomocą magistrali D-BUS.

%package plugin-auto-away
Summary:	Auto-Away Plugin
Summary(pl.UTF-8):	Wtyczka automatycznego stany zajętości
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-auto-away
Auto-Away Plugin.

%description plugin-auto-away -l pl.UTF-8
Wtyczka automatycznego stany zajętości.

%package plugin-ignore
Summary:	Allow to create list of ignored contacts
Summary(pl.UTF-8):	Wtyczka pozwalająca stworzyć listę kontaktów ignorowanych
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-ignore
Allow to create list of ignored contacts.

%description plugin-ignore -l pl.UTF-8
Wtyczka pozwalająca stworzyć listę kontaktów ignorowanych.

%package themes
Summary:	Themes for GNU Gadu 2 GUI
Summary(es.UTF-8):	Temas para el GUI de GNU Gadu 2
Summary(pl.UTF-8):	Motywy graficzne dla GUI GNU Gadu 2
Group:		Applications/Communications
Requires:	%{name}-gui-gtk+2 = %{epoch}:%{version}-%{release}

%description themes
Themes for GNU Gadu 2 GUI.

%description themes -l es.UTF-8
Temas para el GUI de GNU Gadu 2.

%description themes -l pl.UTF-8
Motywy graficzne dla GUI GNU Gadu 2.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I src/plugins/gadu_gadu/libgadu/m4
%{__automake}
%{__autoconf}

%configure \
	%{!?debug:--disable-gdb} \
	%{!?debug:--disable-debug} \
 	--with-gui \
 	--with-gadu \
 	--with-tlen \
 	--with-jabber \
 	--with%{!?with_xosd:out}-xosd \
 	--with-sms \
 	--with-docklet_system_tray \
	--with-docklet_dockapp \
	--with%{!?with_esd:out}-esd \
	--with%{!?with_arts:out}-arts \
 	--with-oss \
 	--with-external \
 	--with-update \
	--with-history-external-viewer \
	--with-aaway \
	--with-ignore \
	--with-gghist \
	--with%{!?with_gtkspell:out}-gtkspell \
	--with%{!?with_dbus:out}-dbus \
	%{?with_dbus:--with-dbus-dir=%{_datadir}/dbus-1/services/} \
	--%{?with_perl:with}%{!?with_perl:without}-perl 

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

%files plugin-gui-gtk+2
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

%files plugin-gadu-gadu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libgadu_gadu_plugin.so

%files plugin-tlen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libtlen_plugin.so

%files plugin-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libjabber_plugin.so

%if %{with esd}
%files plugin-sound-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_esd_plugin.so
%endif

%files plugin-sound-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_oss_plugin.so

%files plugin-sound-external
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_external_plugin.so

%if %{with arts}
%files plugin-sound-aRts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsound_arts_plugin.so
%endif

%if %{with xosd}
%files plugin-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libxosd_plugin.so
%endif

%files plugin-docklet-system-tray
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdocklet_system_tray_plugin.so

%files plugin-docklet-dockapp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdocklet_dockapp_plugin.so

%files plugin-sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsms_plugin.so

%files plugin-history-external
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gghist
%attr(755,root,root) %{_libdir}/gg2/libhistory_external_plugin.so

%files plugin-update
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libupdate_plugin.so

%files plugin-auto-away
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libaaway_plugin.so

%files plugin-ignore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libignore_main_plugin.so

%if %{with dbus}
%files plugin-dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdbus_plugin.so
%{_datadir}/dbus-1/services/org.freedesktop.im.GG.service
%endif

%files themes
%defattr(644,root,root,755)
%dir %{_datadir}/gg2/themes
%{_datadir}/gg2/themes/*.theme
%dir %{_datadir}/gg2/pixmaps/icons
%dir %{_datadir}/gg2/pixmaps/icons/bubble
%dir %{_datadir}/gg2/pixmaps/icons/classic
%dir %{_datadir}/gg2/pixmaps/icons/modern
%dir %{_datadir}/gg2/pixmaps/icons/rozgwiazda
%dir %{_datadir}/gg2/pixmaps/icons/ghosts
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
