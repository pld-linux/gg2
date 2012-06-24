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
Summary(es):	GNU Gadu 2 - charlar libremente
Summary(pl):	GNU Gadu 2 - wolne gadanie
Name:		gg2
Version:	2.2.8
Release:	2
Epoch:		3
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/ggadu/%{name}-%{version}.tar.gz
# Source0-md5:	d2d81ba30b54748d453e662d911ab227
URL:		http://www.gnugadu.org/
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-dbus.patch
Patch2:		%{name}-orange.patch
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

%description -l es
Un cliente para Gadu-Gadu, Tlen.pl y otros protocolos con un GUI de
GTK+2, bajo la licencia GNU/GPL.

%description -l pl
Klient Gadu-Gadu, Tlen.pl oraz innych protoko��w z GUI pod GTK+2 na
licencji GNU/GPL.

%package devel
Summary:	Headers for libgg2_core library to develop plugins
Summary(es):	Cabeceras para la biblioteca libgg2_core para desarrollar plugins
Summary(pl):	Pliki nag��wkowe biblioteki libgg2_core potrzebne do rozwijania wtyczek
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
Ten pakiet zawiera pliki nag��wkowe biblioteki libgg2_core, potrzebne
do rozwijania wtyczek do GNU Gadu 2.

%package plugin-gui-gtk+2
Summary:	GTK+2 GUI plugin
Summary(es):	Plugin de GUI en GTK+2
Summary(pl):	Wtyczka z GUI w GTK+2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-ui
Provides:	gg2-gui-gtk+2 = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-gui-gtk+2
Obsoletes:	gg-gnome

%description plugin-gui-gtk+2
GTK+2 GUI plugin for GNU Gadu 2.

%description plugin-gui-gtk+2 -l es
Un plugin con un GUI en GTK+2 para GNU Gadu 2.

%description plugin-gui-gtk+2 -l pl
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
Iconas de emociones y sus ficheros de descripci�n.

%description emoticons -l pl
Zestaw ikon z emotikonami, oraz plikiem konfiguracyjnym.

%package plugin-gadu-gadu
Summary:	Gadu-Gadu plugin
Summary(es):	Plugin de Gadu-Gadu
Summary(pl):	Wtyczka protoko�u Gadu-Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-gadu-gadu = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-gadu-gadu

%description plugin-gadu-gadu
Gadu-Gadu protocol plugin.

%description plugin-gadu-gadu -l es
Un plugin para el protocolo Gadu-Gadu.

%description plugin-gadu-gadu -l pl
Wtyczka protoko�u Gadu-Gadu.

%package plugin-tlen
Summary:	Tlen.pl plugin
Summary(es):	Plugin de Tlen.pl
Summary(pl):	Wtyczka protoko�u Tlen.pl
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-tlen = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-tlen

%description plugin-tlen
Tlen.pl protocol plugin.

%description plugin-tlen -l es
Un plugin para el protocolo Tlen.pl.

%description plugin-tlen -l pl
Wtyczka protoko�u Tlen.pl.

%package plugin-jabber
Summary:	Jabber.org plugin
Summary(es):	Plugin de Jabber.org
Summary(pl):	Wtyczka protoko�u Jabber
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	loudmouth >= 0.16-4
Provides:	gg2-jabber = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-jabber

%description plugin-jabber
Jabber protocol plugin.

%description plugin-jabber -l es
Un plugin para el protocolo Jabber.

%description plugin-jabber -l pl
Wtyczka protoko�u Jabber.

%package plugin-sound-esd
Summary:	Sound support with ESD
Summary(es):	Soporte de sonido a trav�s de ESD
Summary(pl):	Obs�uga d�wi�ku poprzez ESD
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-sound-esd = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-sound-esd

%description plugin-sound-esd
Sound support with ESD.

%description plugin-sound-esd -l es
Soporte de sonido a trav�s de ESD.

%description plugin-sound-esd -l pl
Obs�uga d�wi�ku poprzez ESD.

%package plugin-sound-oss
Summary:	OSS sound support
Summary(es):	Soporte de sonido a trav�s de OSS
Summary(pl):	Obs�uga d�wi�ku OSS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound-oss = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sound-oss

%description plugin-sound-oss
OSS sound support.

%description plugin-sound-oss -l es
Soporte de sonido a trav�s de OSS.

%description plugin-sound-oss -l pl
Obs�uga d�wi�ku OSS.

%package plugin-sound-external
Summary:	Sound support with external player
Summary(es):	Soporte de sonido v�a un reproductor externo
Summary(pl):	Obs�uga d�wi�ku przez zewn�trzny program
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-sound-external = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-sound-external

%description plugin-sound-external
Sound support with external player.

%description plugin-sound-external -l es
Soporte de sonido a trav�s de un reproductor externo.

%description plugin-sound-external -l pl
Obs�uga d�wi�ku przez zewn�trzny program.

%package plugin-sound-aRts
Summary:	Sound support with aRts
Summary(es):	Soporte de sonido a trav�s de aRts
Summary(pl):	Obs�uga d�wi�ku poprzez aRts
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-sound-aRts = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-sound-aRts

%description plugin-sound-aRts
Sound support with aRts.

%description plugin-sound-aRts -l es
Soporte de sonido a trav�s de aRts.

%description plugin-sound-aRts -l pl
Obs�uga d�wi�ku poprzez aRts.

%package plugin-xosd
Summary:	Support for X On Screen Display
Summary(es):	Soporte para plasmar mensajes sobre el fondo de X
Summary(pl):	Wy�wietlanie komunikat�w na ekranie X
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-xosd = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-xosd

%description plugin-xosd
Support for X On Screen Display.

%description plugin-xosd -l es
Soporte para plasmar mensajes sobre el fondo (XOSD).

%description plugin-xosd -l pl
Wy�wietlanie komunikat�w na ekranie X.

%package plugin-docklet-system-tray
Summary:	Support for Window Managers notification areas
Summary(es):	Soporte para �reas de notificaci�n de los Manejantes de Ventanas
Summary(pl):	Obs�uga obszar�w powiadomie� w r�nych zarz�dcach okien
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-docklet-system-tray = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-docklet-system-tray
Obsoletes:	gg2-docklet

%description plugin-docklet-system-tray
Support for Window Managers notification areas (GNOME, KDE).

%description plugin-docklet-system-tray -l es
Soporte para �reas de notificaci�n de los Manejantes de Ventanas
(GNOME, KDE).

%description plugin-docklet-system-tray -l pl
Obs�uga obszar�w powiadomie� w r�nych zarz�dcach okien (GNOME, KDE).

%package plugin-docklet-dockapp
Summary:	Support for WindowMaker-style dockapp
Summary(es):	Soporte de dockapp estilo WindowMaker
Summary(pl):	Obs�uga dokowalnego apletu zgodnego z WindowMakerem
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-docklet-dockapp = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-docklet-dockapp
Obsoletes:	gg2-docklet
Obsoletes:	gg-gnome-applet
Obsoletes:	gg-wm-applet

%description plugin-docklet-dockapp
Support for WindowMaker-style dockapp.

%description plugin-docklet-dockapp -l es
Suporte de dockapp estilo WindowMaker.

%description plugin-docklet-dockapp -l pl
Obs�uga dokowalnego apletu zgodnego z WindowMakerem.

%package plugin-sms
Summary:	SMS Gateway
Summary(es):	Puerta SMS
Summary(pl):	Bramka SMS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-sms = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-sms

%description plugin-sms
Send SMS to cellular phones via web gateways.

%description plugin-sms -l es
Manda mensajes SMS a m�viles v�a puertas del Web.

%description plugin-sms -l pl
Wtyczka wysy�aj�ca wiadomo�ci SMS na telefony kom�rkowe przez bramki
WWW.

%package plugin-history-external
Summary:	Allow to view GNU Gadu chat history
Summary(pl):	Przegl�danie historii rozm�w GNU Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2
Provides:	gg2-history-external = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-history-external

%description plugin-history-external
Allow to view GNU Gadu chat history.

%description plugin-history-external -l pl
Wtyczka pozwalaj�ca przegl�da� histori� rozm�w GNU Gadu.

%package plugin-update
Summary:	Check for new GNU Gadu newer version
Summary(es):	Verifica si hay versiones nuevas de GNU Gadu
Summary(pl):	Sprawdzanie dost�pno�ci nowszej wersji GNU Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gg2-update = %{epoch}:%{version}-%{release}
Obsoletes:	gg2-update

%description plugin-update
Check for new GNU Gadu newer version.

%description plugin-update -l es
Verifica si hay nuevas versiones de GNU Gadu.

%description plugin-update -l pl
Wtyczka sprawdzaj�ca, czy jest dost�pna nowsza wersja GNU Gadu.

%package plugin-dbus
Summary:	Allow to communicate using D-BUS message bus
Summary(pl):	Komunikacja za pomoc� magistrali D-BUS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-dbus
This plugin allows to communicate using D-BUS interface.

%description plugin-dbus -l pl
Wtyczka pozwala na komunikacj� za pomoc� magistrali D-BUS.

%package plugin-auto-away
Summary:	Auto-Away Plugin
Summary(pl):	Wtyczka automatycznego stany zaj�to�ci
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-auto-away
Auto-Away Plugin.

%description plugin-auto-away -l pl
Wtyczka automatycznego stany zaj�to�ci.

%package plugin-ignore
Summary:	Allow to create list of ignored contacts
Summary(pl):	Wtyczka pozwalaj�ca stworzy� list� kontakt�w ignorowanych
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-ignore
Allow to create list of ignored contacts.

%description plugin-ignore -l pl
Wtyczka pozwalaj�ca stworzy� list� kontakt�w ignorowanych.

%package themes
Summary:	Themes for GNU Gadu 2 GUI
Summary(es):	Temas para el GUI de GNU Gadu 2
Summary(pl):	Motywy graficzne dla GUI GNU Gadu 2
Group:		Applications/Communications
Requires:	%{name}-gui-gtk+2 = %{epoch}:%{version}-%{release}

%description themes
Themes for GNU Gadu 2 GUI.

%description themes -l es
Temas para el GUI de GNU Gadu 2.

%description themes -l pl
Motywy graficzne dla GUI GNU Gadu 2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
