Summary:	cmus is a small and fast text mode music player
Summary(hu.UTF-8):	cmus egy kicsi és gyors szöveges zenelejátszó
Name:		cmus
Version:	2.2.0
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://mirror.greaterscope.net/cmus/%{name}-%{version}.tar.bz2
# Source0-md5:	7a9895ecfc10cd16577c73051436962f
URL:		http://cmus.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libao-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mpeg4ip-devel
BuildRequires:	ncurses-devel
BuildRequires:	sed > 4.0
BuildRequires:	wavpack-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cmus is a small and fast text mode music player

%description -l pl.UTF-8
cmus egy kicsi és gyors szöveges zenelejátszó


# input plugins

%package aac
Summary:	aac plugin for cmus
Summary(hu.UTF-8):	aac plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description aac
aac plugin for cmus

%description aac -l hu.UTF-8
aac plugin cmus-hoz


%package ffmpeg
Summary:	ffmpeg plugin for cmus
Summary(hu.UTF-8):	ffmpeg plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description ffmpeg
ffmpeg plugin for cmus

%description ffmpeg -l hu.UTF-8
ffmpeg plugin cmus-hoz


%package flac
Summary:	flac plugin for cmus
Summary(hu.UTF-8):	flac plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description flac
flac plugin for cmus

%description flac -l hu.UTF-8
flac plugin cmus-hoz


%package mad
Summary:	mad plugin for cmus
Summary(hu.UTF-8):	mad plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description mad
mad plugin for cmus

%description mad -l hu.UTF-8
mad plugin cmus-hoz


%package modplug
Summary:	modplug plugin for cmus
Summary(hu.UTF-8):	modplug plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description modplug
modplug plugin for cmus

%description modplug -l hu.UTF-8
modplug plugin cmus-hoz


%package mp4
Summary:	mp4 plugin for cmus
Summary(hu.UTF-8):	mp4 plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description mp4
mp4 plugin for cmus

%description mp4 -l hu.UTF-8
mp4 plugin cmus-hoz


%package vorbis
Summary:	vorbis plugin for cmus
Summary(hu.UTF-8):	vorbis plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description vorbis
vorbis plugin for cmus

%description vorbis -l hu.UTF-8
vorbis plugin cmus-hoz


%package wav
Summary:	wav plugin for cmus
Summary(hu.UTF-8):	wav plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description wav
wav plugin for cmus

%description wav -l hu.UTF-8
wav plugin cmus-hoz


%package wavpack
Summary:	wavpack plugin for cmus
Summary(hu.UTF-8):	wavpack plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description wavpack
wavpack plugin for cmus

%description wavpack -l hu.UTF-8
wavpack plugin cmus-hoz


# output plugins

%package alsa
Summary:	alsa plugin for cmus
Summary(hu.UTF-8):	alsa plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-output

%description alsa
alsa plugin for cmus

%description alsa -l hu.UTF-8
alsa plugin cmus-hoz


%package arts
Summary:	arts plugin for cmus
Summary(hu.UTF-8):	arts plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-output

%description arts
arts plugin for cmus

%description arts -l hu.UTF-8
arts plugin cmus-hoz


%package libao
Summary:	libao plugin for cmus
Summary(hu.UTF-8):	libao plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-output

%description libao
libao plugin for cmus

%description libao -l hu.UTF-8
libao plugin cmus-hoz


%package oss
Summary:	oss plugin for cmus
Summary(hu.UTF-8):	oss plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-output

%description oss
oss plugin for cmus

%description oss -l hu.UTF-8
oss plugin cmus-hoz



%prep
%setup -q
%{__sed} -i "s|<curses.h>|<ncursesw/ncurses.h>|" command_mode.c keys.c options.c search_mode.c ui_curses.c
%{__sed} -r -i "s|<ffmpeg/(.*).h|<lib\1/\1.h|" ffmpeg.c

%build

./configure prefix=%{_prefix} libdir=%{_libdir} mandir=%{_mandir} bindir=%{_bindir}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_docdir}/cmus/* $RPM_BUILD_ROOT%{_docdir}/cmus-%{version}
rmdir $RPM_BUILD_ROOT%{_docdir}/cmus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS HACKING README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/cmus*

# input plugins
%files aac
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/aac.so

%files ffmpeg
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/ffmpeg.so

%files flac
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/flac.so

%files mad
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/mad.so

%files modplug
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/modplug.so

%files mp4
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/mp4.so

%files vorbis
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/vorbis.so

%files wav
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/wav.so

%files wavpack
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/wavpack.so

# output plugins
%files alsa
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/op
%{_libdir}/cmus/op/alsa.so

%files libao
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/op
%{_libdir}/cmus/op/ao.so

%files oss
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/op
%{_libdir}/cmus/op/oss.so
