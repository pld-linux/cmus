#
# Conditional build:
%bcond_with	arts	# aRts support
%bcond_with	ffmpeg	# FFmpeg support (outdated)

Summary:	cmus - a small and fast text mode music player
Summary(hu.UTF-8):	cmus egy kicsi és gyors szöveges zenelejátszó
Summary(pl.UTF-8):	cmus - mały i szybki odtwarzacz muzyki w trybie tekstowym
Name:		cmus
Version:	2.5.0
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	https://downloads.sourceforge.net/project/cmus/%{name}-v%{version}.tar.bz2
# Source0-md5:	9af16d324060447996ed25e1a9c1c7d8
Patch0:		%{name}-libcdio.patch
Patch1:		%{name}-libmodplug.patch
URL:		https://cmus.sourceforge.net/
BuildRequires:	alsa-lib-devel >= 1.0.11
%if %{with arts}
BuildRequires:	artsc-devel
%endif
BuildRequires:	faad2-devel
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	flac-devel
BuildRequires:	libao-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcue-devel >= 1.3
BuildRequires:	libdiscid-devel
BuildRequires:	libmad-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mp4v2-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.19
# TODO
#BuildRequires:	roaraudio-devel >= 0.4.5
BuildRequires:	sed >= 4.0
BuildRequires:	wavpack-devel
Suggests:	%{name}-input
Suggests:	%{name}-output
%if %{without ffmpeg}
Obsoletes:	cmus-input-ffmpeg < %{version}-%{release}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cmus is a small and fast text mode music player.

%description -l hu.UTF-8
cmus egy kicsi és gyors szöveges zenelejátszó.

%description -l pl.UTF-8
cmus to mały i szybki odtwarzacz muzyki, działający w trybie
tekstowym.

# input plugins

%package input-aac
Summary:	aac input plugin for cmus
Summary(hu.UTF-8):	aac plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa aac dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-aac
aac input plugin for cmus.

%description input-aac -l hu.UTF-8
aac plugin cmus-hoz.

%description input-aac -l pl.UTF-8
Wtyczka wejściowa aac dla odtwarzacza cmus.

%package input-cdio
Summary:	cdio input plugin for cmus
Summary(hu.UTF-8):	cdio plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa cdio dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-cdio
cdio input plugin for cmus.

%description input-cdio -l hu.UTF-8
cdio plugin cmus-hoz.

%description input-cdio -l pl.UTF-8
Wtyczka wejściowa cdio dla odtwarzacza cmus.

%package input-cue
Summary:	cue input plugin for cmus
Summary(hu.UTF-8):	cue plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa cue dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-cue
cue input plugin for cmus.

%description input-cue -l hu.UTF-8
cue plugin cmus-hoz.

%description input-cue -l pl.UTF-8
Wtyczka wejściowa cue dla odtwarzacza cmus.

%package input-ffmpeg
Summary:	ffmpeg input plugin for cmus
Summary(hu.UTF-8):	ffmpeg plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa ffmpeg dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-ffmpeg
ffmpeg input plugin for cmus.

%description input-ffmpeg -l hu.UTF-8
ffmpeg plugin cmus-hoz.

%description input-ffmpeg -l pl.UTF-8
Wtyczka wejściowa ffmpeg dla odtwarzacza cmus.

%package input-flac
Summary:	flac input plugin for cmus
Summary(hu.UTF-8):	flac plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa flac dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-flac
flac input plugin for cmus.

%description input-flac -l hu.UTF-8
flac plugin cmus-hoz.

%description input-flac -l pl.UTF-8
Wtyczka wejściowa flac dla odtwarzacza cmus.

%package input-mad
Summary:	mad input plugin for cmus
Summary(hu.UTF-8):	mad plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa mad dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-mad
mad input plugin for cmus.

%description input-mad -l hu.UTF-8
mad plugin cmus-hoz.

%description input-mad -l pl.UTF-8
Wtyczka wejściowa mad dla odtwarzacza cmus.

%package input-modplug
Summary:	modplug input plugin for cmus
Summary(hu.UTF-8):	modplug plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa modplug dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-modplug
modplug input plugin for cmus.

%description input-modplug -l hu.UTF-8
modplug plugin cmus-hoz.

%description input-modplug -l pl.UTF-8
Wtyczka wejściowa modplug dla odtwarzacza cmus.

%package input-mp4
Summary:	mp4 input plugin for cmus
Summary(hu.UTF-8):	mp4 plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa mp4 dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-mp4
mp4 input plugin for cmus.

%description input-mp4 -l hu.UTF-8
mp4 plugin cmus-hoz.

%description input-mp4 -l pl.UTF-8
Wtyczka wejściowa mp4 dla odtwarzacza cmus.

%package input-mpc
Summary:	mpc input plugin for cmus
Summary(hu.UTF-8):	mpc plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa mpc dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-mpc
mpc input plugin for cmus.

%description input-mpc -l hu.UTF-8
mpc plugin cmus-hoz.

%description input-mpc -l pl.UTF-8
Wtyczka wejściowa mpc dla odtwarzacza cmus.

%package input-vorbis
Summary:	vorbis input plugin for cmus
Summary(hu.UTF-8):	vorbis plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa vorbis dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-vorbis
vorbis input plugin for cmus.

%description input-vorbis -l hu.UTF-8
vorbis plugin cmus-hoz.

%description input-vorbis -l pl.UTF-8
Wtyczka wejściowa vorbis dla odtwarzacza cmus.

%package input-wav
Summary:	wav input plugin for cmus
Summary(hu.UTF-8):	wav plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa wav dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input

%description input-wav
wav input plugin for cmus.

%description input-wav -l hu.UTF-8
wav plugin cmus-hoz.

%description input-wav -l pl.UTF-8
Wtyczka wejściowa wav dla odtwarzacza cmus.

%package input-wavpack
Summary:	wavpack input plugin for cmus
Summary(hu.UTF-8):	wavpack plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa wavpack dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-wavpack
wavpack input plugin for cmus.

%description input-wavpack -l hu.UTF-8
wavpack plugin cmus-hoz.

%description input-wavpack -l pl.UTF-8
Wtyczka wejściowa wavpack dla odtwarzacza cmus.

# output plugins

%package output-alsa
Summary:	alsa output plugin for cmus
Summary(hu.UTF-8):	alsa plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa alsa dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-output

%description output-alsa
alsa output plugin for cmus.

%description output-alsa -l hu.UTF-8
alsa plugin cmus-hoz.

%package output-arts
Summary:	arts output plugin for cmus
Summary(hu.UTF-8):	arts plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa arts dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-output

%description output-arts
arts output plugin for cmus.

%description output-arts -l hu.UTF-8
arts plugin cmus-hoz.

%description output-arts -l pl.UTF-8
Wtyczka wyjściowa arts dla odtwarzacza cmus.

%package output-libao
Summary:	libao output plugin for cmus
Summary(hu.UTF-8):	libao plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa libao dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-output

%description output-libao
libao output plugin for cmus.

%description output-libao -l hu.UTF-8
libao plugin cmus-hoz.

%description output-libao -l pl.UTF-8
Wtyczka wyjściowa libao dla odtwarzacza cmus.

%package output-oss
Summary:	oss output plugin for cmus
Summary(hu.UTF-8):	oss plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa oss dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-output

%description output-oss
oss output plugin for cmus.

%description output-oss -l hu.UTF-8
oss plugin cmus-hoz.

%description output-oss -l pl.UTF-8
Wtyczka wyjściowa oss dla odtwarzacza cmus.

%package output-pulse
Summary:	pulse output plugin for cmus
Summary(hu.UTF-8):	pulse plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa pulse dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-output

%description output-pulse
pulse output plugin for cmus.

%description output-pulse -l hu.UTF-8
pulse plugin cmus-hoz.

%description output-pulse -l pl.UTF-8
Wtyczka wyjściowa pulse dla odtwarzacza cmus.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1
%patch1 -p1

%{__sed} -i "s|<curses.h>|<ncursesw/ncurses.h>|" command_mode.c keys.c options.c search_mode.c ui_curses.c

%build
./configure \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
%if %{without arts}
	CONFIG_ARTS=n \
%endif
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	mandir=%{_mandir} \
	bindir=%{_bindir} \
	datadir=%{_datadir}/%{name} \
	exampledir=%{_examplesdir}/%{name}-%{version}

%{__make} \
	V=2

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/cmus
%attr(755,root,root) %{_bindir}/cmus-remote
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%dir %{_libdir}/cmus/op
%{_datadir}/%{name}
%{_mandir}/man1/cmus.1*
%{_mandir}/man1/cmus-remote.1*
%{_mandir}/man7/cmus-tutorial.7*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/%{name}-status-display

# input plugins
%files input-aac
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/aac.so

%files input-cdio
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/cdio.so

%files input-cue
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/cue.so

%if %{with ffmpeg}
%files input-ffmpeg
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/ffmpeg.so
%endif

%files input-flac
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/flac.so

%files input-mad
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/mad.so

%files input-modplug
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/modplug.so

%files input-mp4
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/mp4.so

%files input-mpc
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/mpc.so

%files input-vorbis
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/vorbis.so

%files input-wav
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/wav.so

%files input-wavpack
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/wavpack.so

# output plugins
%files output-alsa
%defattr(644,root,root,755)
%{_libdir}/cmus/op/alsa.so

%files output-libao
%defattr(644,root,root,755)
%{_libdir}/cmus/op/ao.so

%if %{with arts}
%files output-arts
%defattr(644,root,root,755)
%{_libdir}/cmus/op/arts.so
%endif

%files output-oss
%defattr(644,root,root,755)
%{_libdir}/cmus/op/oss.so

%files output-pulse
%defattr(644,root,root,755)
%{_libdir}/cmus/op/pulse.so
