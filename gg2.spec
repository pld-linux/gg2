#
# Conditional build: 
%bcond_without	arts
%bcond_without	perl
%bcond_without	esd
%bcond_without	gtkspell
%bcond_without	dbus
#
Summary:	GNU Gadu 2 - free talking
Summary(es):	GNU Gadu 2 - charlar libremente
Summary(pl):	GNU Gadu 2 - wolne gadanie
Name:		gg2
Version:	2.2.3
Release:	2
Epoch:		3
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://osdn.dl.sourceforge.net/sourceforge/ggadu/%{name}-%{version}.tar.gz
# Source0-md5:	5d38e161612307ea2a7a00f9453678e3
URL:		http://www.gnugadu.org/
Patch0:		%{name}-desktop.patch
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
%{?with_esd:BuildRequires:	esound-devel >= 0.2.7}
BuildRequires:	gettext-devel >= 0.11.0
BuildRequires:	glib2-devel  >= 2.2.0
BuildRequires:	gtk+2-devel  >= 2.4.0
BuildRequires:	libtlen-devel
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 0.17.1
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_dbus:BuildRequires:	dbus-libs >= 0.22}
%{?with_gtkspell:BuildRequires:	gtkspell-devel}
%{?with_gtkspell:BuildRequires:	aspell-devel}
BuildRequires:	pkgconfig
BuildRequires:	xosd-devel   >= 2.0.0
%if %{with perl}
BuildRequires:	perl-devel
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
%endif
Requires:	gg2-ui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gadu-Gadu, Tlen.pl and others instant messenger client with
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

%package plugin-gui-gtk+2
Summary:	GTK+2 GUI plugin
Summary(es):	Plugin de GUI en GTK+2
Summary(pl):	Wtyczka z GUI w GTK+2
Group:		Applications/Communications
Provides:	gg2-ui
Provides:	%{name}-gui-gtk+2 = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-gui-gtk+2
Requires:	%{name} = %{epoch}:%{version}-%{release}

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
Iconas de emociones y sus ficheros de descripción.

%description emoticons -l pl
Zestaw ikon z emotikonami, oraz plikiem konfiguracyjnym.

%package plugin-gadu-gadu
Summary:	Gadu-Gadu plugin
Summary(es):	Plugin de Gadu-Gadu
Summary(pl):	Wtyczka protoko³u Gadu-Gadu
Group:		Applications/Communications
Provides:	%{name}-gadu-gadu = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-gadu-gadu
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gadu-gadu
Gadu-Gadu protocol plugin.

%description plugin-gadu-gadu -l es
Un plugin para el protocolo Gadu-Gadu.

%description plugin-gadu-gadu -l pl
Wtyczka protoko³u Gadu-Gadu.

%package plugin-tlen
Summary:	Tlen.pl plugin
Summary(es):	Plugin de Tlen.pl
Summary(pl):	Wtyczka protoko³u Tlen.pl
Group:		Applications/Communications
Provides:	%{name}-tlen = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-tlen
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tlen
Tlen.pl protocol plugin.

%description plugin-tlen -l es
Un plugin para el protocolo Tlen.pl.

%description plugin-tlen -l pl
Wtyczka protoko³u Tlen.pl.

%package plugin-jabber
Summary:	Jabber.org plugin
Summary(es):	Plugin de Jabber.org
Summary(pl):	Wtyczka protoko³u Jabber
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	loudmouth >= 0.16-4
Provides:	%{name}-jabber = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-jabber

%description plugin-jabber
Jabber protocol plugin.

%description plugin-jabber -l es
Un plugin para el protocolo Jabber.

%description plugin-jabber -l pl
Wtyczka protoko³u Jabber.

%package plugin-sound-esd
Summary:	Sound support with ESD
Summary(es):	Soporte de sonido a través de ESD
Summary(pl):	Obs³uga d¼wiêku poprzez ESD
Group:		Applications/Communications
Provides:	%{name}-sound-esd = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sound-esd
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sound-esd
Sound support with ESD.

%description plugin-sound-esd -l es
Soporte de sonido a través de ESD.

%description plugin-sound-esd -l pl
Obs³uga d¼wiêku poprzez ESD.

%package plugin-sound-oss
Summary:	OSS sound support
Summary(es):	Soporte de sonido a través de OSS
Summary(pl):	Obs³uga d¼wiêku OSS
Group:		Applications/Communications
Provides:	%{name}-sound-oss = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sound-oss
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sound-oss
OSS sound support.

%description plugin-sound-oss -l es
Soporte de sonido a través de OSS.

%description plugin-sound-oss -l pl
Obs³uga d¼wiêku OSS.

%package plugin-sound-external
Summary:	Sound support with external player
Summary(es):	Soporte de sonido vía un reproductor externo
Summary(pl):	Obs³uga d¼wiêku przez zewnêtrzny program
Group:		Applications/Communications
Provides:	%{name}-sound-external = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sound-external
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sound-external
Sound support with external player.

%description plugin-sound-external -l es
Soporte de sonido a través de un reproductor externo.

%description plugin-sound-external -l pl
Obs³uga d¼wiêku przez zewnêtrzny program.

%package plugin-sound-aRts
Summary:	Sound support with aRts
Summary(es):	Soporte de sonido a través de aRts
Summary(pl):	Obs³uga d¼wiêku poprzez aRts
Group:		Applications/Communications
Provides:	%{name}-sound-aRts = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sound-aRts
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sound-aRts
Sound support with aRts.

%description plugin-sound-aRts -l es
Soporte de sonido a través de aRts.

%description plugin-sound-aRts -l pl
Obs³uga d¼wiêku poprzez aRts.

%package plugin-xosd
Summary:	Support for X On Screen Display
Summary(es):	Soporte para plasmar mensajes sobre el fondo de X
Summary(pl):	Wy¶wietlanie komunikatów na ekranie X
Group:		Applications/Communications
Provides:	%{name}-xosd = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-xosd
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xosd
Support for X On Screen Display.

%description plugin-xosd -l es
Soporte para plasmar mensajes sobre el fondo (XOSD).

%description plugin-xosd -l pl
Wy¶wietlanie komunikatów na ekranie X.

%package plugin-docklet-system-tray
Summary:	Support for Window Managers notification areas
Summary(es):	Soporte para áreas de notificación de los Manejantes de Ventanas
Summary(pl):	Obs³uga obszarów powiadomieñ w ró¿nych zarz±dcach okien
Group:		Applications/Communications
Provides:	%{name}-docklet-system-tray = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-docklet-system-tray
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-docklet

%description plugin-docklet-system-tray
Support for Window Managers notification areas (GNOME, KDE).

%description plugin-docklet-system-tray -l es
Soporte para áreas de notificación de los Manejantes de Ventanas
(GNOME, KDE).

%description plugin-docklet-system-tray -l pl
Obs³uga obszarów powiadomieñ w ró¿nych zarz±dcach okien (GNOME, KDE).

%package plugin-docklet-dockapp
Summary:	Support for WindowMaker-style dockapp
Summary(es):	Soporte de dockapp estilo WindowMaker
Summary(pl):	Obs³uga dokowalnego apletu zgodnego z WindowMakerem
Group:		Applications/Communications
Provides:	%{name}-docklet-dockapp = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-docklet-dockapp
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-docklet

%description plugin-docklet-dockapp
Support for WindowMaker-style dockapp.

%description plugin-docklet-dockapp -l es
Suporte de dockapp estilo WindowMaker.

%description plugin-docklet-dockapp -l pl
Obs³uga dokowalnego apletu zgodnego z WindowMakerem.

%package plugin-sms
Summary:	SMS Gateway
Summary(es):	Puerta SMS
Summary(pl):	Bramka SMS
Group:		Applications/Communications
Provides:	%{name}-sms = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sms
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sms
Send SMS to cellular phones via web gateways.

%description plugin-sms -l es
Manda mensajes SMS a móviles vía puertas del Web.

%description plugin-sms -l pl
Wtyczka wysy³aj±ca wiadomo¶ci SMS na telefony komórkowe przez bramki
WWW.

%package plugin-remote
Summary:	Remote access from other applications
Summary(es):	Acceso remoto desde otras aplicaciones
Summary(pl):	Dostêp do programu z innych aplikacji
Group:		Applications/Communications
Provides:	%{name}-remote = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-remote
#Provides:	gg2-ui
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-remote
Make possible exchange data with other applications.

%description plugin-remote -l es
Permite intercambiar los datos con otras aplicaciones.

%description plugin-remote -l pl
Wtyczka umo¿liwiaj±ca wymianê informacji z innymi aplikacjami.

%package plugin-history-external
Summary:	Allow to view GNU Gadu chat history
Summary(pl):	Przegl±danie historii rozmów GNU Gadu
Group:		Applications/Communications
Provides:	%{name}-history-external = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-history-external
Requires:	gtk+2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-history-external
Allow to view GNU Gadu chat history.

%description plugin-history-external -l pl
Wtyczka pozwalaj±ca przegl±daæ historiê rozmów GNU Gadu.

%package plugin-update
Summary:	Check for new GNU Gadu newer version
Summary(es):	Verifica si hay versiones nuevas de GNU Gadu
Summary(pl):	Sprawdzanie dostêpno¶ci nowszej wersji GNU Gadu
Group:		Applications/Communications
Provides:	%{name}-update = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-update
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-update
Check for new GNU Gadu newer version.

%description plugin-update -l es
Verifica si hay nuevas versiones de GNU Gadu.

%description plugin-update -l pl
Wtyczka sprawdzaj±ca, czy jest dostêpna nowsza wersja GNU Gadu.

%package plugin-dbus
Summary:	Allow to communicate using D-BUS message bus
Summary(pl):	Komunikacja za pomoc± magistrali D-BUS
Group:		Applications/Communications
Provides:	%{name}-update = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-update
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-dbus
This plugin allows to communicate using D-BUS interface.

%description plugin-dbus -l pl
Wtyczka pozwala na komunikacjê za pomoc± magistrali D-BUS.

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
 	--with-xosd \
 	--with-sms \
 	--with-docklet_system_tray \
	--with-docklet_dockapp \
	--with%{!?with_esd:out}-esd \
	--with%{!?with_arts:out}-arts \
 	--with-oss \
 	--with-external \
 	--with-update \
	--with-history-external-viewer \
	--with-gghist \
	--with%{!?with_gtkspell:out}-gtkspell \
	--with%{!?with_dbus:out}-dbus \
	%{?with_dbus:--with-dbus-dir=%{_datadir}/dbus-1.0/services/} \
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

%files plugin-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libxosd_plugin.so

%files plugin-docklet-system-tray
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdocklet_system_tray_plugin.so

%files plugin-docklet-dockapp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdocklet_dockapp_plugin.so

%files plugin-sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsms_plugin.so

%files plugin-remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libremote_plugin.so

%files plugin-history-external
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gghist
%attr(755,root,root) %{_libdir}/gg2/libhistory_external_plugin.so

%files plugin-update
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libupdate_plugin.so

%if %{with dbus}
%files plugin-dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdbus_plugin.so
%{_datadir}/dbus-1.0/services/org.freedesktop.im.GG.service
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
%dir %{_datadir}/gg2/pixmaps/icons/tlen-classic
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
%{_datadir}/gg2/pixmaps/icons/tlen-classic/*.png
