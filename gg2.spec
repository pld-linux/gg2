
%bcond_with	arts
%bcond_without	perl

%define		_snap	20030917
Summary:	GNU Gadu 2 - free talking
Summary(pl):	GNU Gadu 2 - wolne gadanie
Name:		gg2
Version:	2.0
Release:	2.%{_snap}.1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
#Source0:	http://dl.sourceforge.net/sourceforge/ggadu/%{name}-%{version}-%{_snap}.tar.gz
Source0:	%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	8026a52c6fa169a9f86603866870e09a
Source1:	%{name}.desktop
URL:		http://www.gadu.gnu.pl/
BuildRequires:	perl-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	loudmouth-devel >= 0.13.1
BuildRequires:	glib2-devel  >= 2.2.0
BuildRequires:	gtk+2-devel  >= 2.2.0
BuildRequires:	libgadu-devel >= 1.0
BuildRequires:	libtlen-devel
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	gettext-devel >= 0.11.0
BuildRequires:	xosd-devel   >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	fontconfig-devel
%{?with_arts:BuildRequires:	arts-devel}
%{?with_perl:BuildRequires:	perl-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gadu-Gadu, Tlen.pl and others instant messanger client with
GTK+2 GUI on GNU/GPL.

%description -l pl
Klient Gadu-Gadu, Tlen.pl oraz innych protoko��w z GUI pod GTK+2 na
licencji GNU/GPL.

%package devel
Summary:	Headers for libgg2_core library to develop plugins
Summary(pl):	Pliki nag��wkowe biblioteki libgg2_core potrzebne do rozwijania wtyczek
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}
Requires:	glib2-devel
Requires:	perl-devel

%description devel
This package contains header files for libgg2_core library, needed to
develop plugins for GNU Gadu 2.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe biblioteki libgg2_core, potrzebne
do rozwijania wtyczek do GNU Gadu 2.

%package gui-gtk+2
Summary:	GTK+2 GUI plugin
Summary(pl):	Wtyczka z GUI w GTK+2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description gui-gtk+2
GTK+2 GUI plugin for GNU Gadu 2.

%description gui-gtk+2 -l pl
Wtyczka z GUI w GTK+2 do GNU Gadu 2.

%package emoticons
Summary:	Emoticons
Summary(pl):	Emotikony
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description emoticons
Emotions icons and description files.

%description emoticons -l pl
Zestaw ikon z emotikonami, oraz plikiem konfiguracyjnym.

%package gadu-gadu
Summary:	Gadu-Gadu plugin
Summary(pl):	Wtyczka protoko�u Gadu-Gadu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description gadu-gadu
Gadu-Gadu protocol plugin.

%description gadu-gadu -l pl
Wtyczka protoko�u Gadu-Gadu.

%package tlen
Summary:	Tlen.pl plugin
Summary(pl):	Wtyczka protoko�u Tlen.pl
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description tlen
Tlen.pl protocol plugin.

%description tlen -l pl
Wtyczka protoko�u Tlen.pl.

%package jabber
Summary:	Jabber.org plugin
Summary(pl):	Wtyczka protoko�u Jabber
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description jabber
Jabber protocol plugin.

%description jabber -l pl
Wtyczka protoko�u Jabber.

%package sound-esd
Summary:	Sound support with ESD
Summary(pl):	Obs�uga d�wi�ku poprzez ESD
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description sound-esd
Sound support with ESD.

%description sound-esd -l pl
Obs�uga d�wi�ku poprzez ESD.

%package sound-oss
Summary:	OSS sound support
Summary(pl):	Obs�uga d�wi�ku OSS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description sound-oss
OSS sound support.

%description sound-oss -l pl
Obs�uga d�wi�ku OSS.

%package sound-external
Summary:	Sound support with external player
Summary(pl):	Obs�uga d�wi�ku przez zewn�trzny program
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description sound-external
Sound support with external player.

%description sound-external -l pl
Obs�uga d�wi�ku przez zewn�trzny program.

%if %{with arts}
%package sound-aRts
Summary:	Sound support with aRts
Summary(pl):	Obs�uga d�wi�ku poprzez aRts
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description sound-aRts
Sound support with aRts.

%description sound-aRts -l pl
Obs�uga d�wi�ku poprzez aRts.
%endif

%package xosd
Summary:	Support for X On Screen Display
Summary(pl):	Wy�wietlanie komunikat�w na ekranie X
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description xosd
Support for X On Screen Display.

%description xosd -l pl
Wy�wietlanie komunikat�w na ekranie X.

%package docklet
Summary:	Support for Window Managers docklets
Summary(pl):	Obs�uga doklet�w w r�nych zarz�dcach okien
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description docklet
Support for Window Managers docklets (GNOME, KDE).

%description docklet -l pl
Obs�uga doklet�w w r�nych zarz�dcach okien (GNOME, KDE).

%package sms
Summary:	SMS Gateway
Summary(pl):	Bramka SMS
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description sms
Send SMS to cellular phones via web gateways.

%description sms -l pl
Wtyczka wysy�aj�ca wiadomo�ci SMS na telefony kom�rkowe przez bramki WWW.

%package remote
Summary:	Remote access from other applications
Summary(pl):	Dost�p do programu z innych aplikacji
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}

%description remote
Make possible exchange data with other applications.

%description remote -l pl
Wtyczka umo�liwiaj�ca wymian� informacji z innymi aplikacjami.

%package themes
Summary:	Themes for GNU Gadu 2 GUI
Summary(pl):	Motywy graficzne dla GUI GNU Gadu 2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}
Requires:	%{name}-gui-gtk+2

%description themes
Themes for GNU Gadu 2 GUI.

%description themes -l pl
Motywy graficzne dla GUI GNU Gadu 2.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

%build
rm -f missing
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}

%configure \
	--disable-gdb \
	--disable-debug \
 	--with-gui \
 	--with-gadu \
 	--with-tlen \
 	--with-jabber \
 	--with-xosd \
 	--with-docklet \
 	--with-esd \
 	--with-oss \
 	--with-sms \
 	--with-external \
%if %{with arts}
	--with-arts \
%endif
%if %{with perl}
	--enable-perl \
%endif
 	--with-remote

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%find_lang %{name} --all-name --with-gnome

#Remove useless files
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

%files docklet
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libdocklet_plugin.so

%files sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libsms_plugin.so

%files remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libremote_plugin.so

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
