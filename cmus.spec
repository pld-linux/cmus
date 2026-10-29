# TODO libbass+bass.h, libayemu+ayemu.h
#
# Conditional build:
%bcond_with	arts	# aRts support
%bcond_without	ffmpeg	# FFmpeg support

Summary:	cmus - a small and fast text mode music player
Summary(hu.UTF-8):	cmus egy kicsi és gyors szöveges zenelejátszó
Summary(pl.UTF-8):	cmus - mały i szybki odtwarzacz muzyki w trybie tekstowym
Name:		cmus
Version:	2.13.0
Release:	1
License:	GPL v2+
Group:		Applications/Sound
#Source0Download: https://github.com/cmus/cmus/releases
Source0:	https://github.com/cmus/cmus/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0ea28009e3bb16f141b9f3ff6f0ea3fa
URL:		https://cmus.github.io/
BuildRequires:	alsa-lib-devel >= 1.0.11
%if %{with arts}
BuildRequires:	artsc-devel
%endif
BuildRequires:	faad2-devel
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	flac-devel
BuildRequires:	gcc >= 6:4.7
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libao-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libdiscid-devel
BuildRequires:	libmad-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libsamplerate-devel
# or tremor with CONFIG_TREMOR=y
BuildRequires:	libvorbis-devel
BuildRequires:	mp4v2-devel
BuildRequires:	ncurses-devel
BuildRequires:	opusfile-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.19
# TODO
#BuildRequires:	roaraudio-devel >= 0.4.5
BuildRequires:	sed >= 4.0
# or elogind-devel
BuildRequires:	systemd-devel
BuildRequires:	wavpack-devel >= 4.40
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
Summary:	AAC input plugin for cmus
Summary(hu.UTF-8):	AAC plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa AAC dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-aac
AAC input plugin for cmus.

%description input-aac -l hu.UTF-8
AAC plugin cmus-hoz.

%description input-aac -l pl.UTF-8
Wtyczka wejściowa AAC dla odtwarzacza cmus.

%package input-cdio
Summary:	cdio (CD Audio) input plugin for cmus
Summary(hu.UTF-8):	cdio (CD Audio) plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa cdio (CD Audio) dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-cdio
cdio (CD Audio) input plugin for cmus.

%description input-cdio -l hu.UTF-8
cdio (CD Audio) plugin cmus-hoz.

%description input-cdio -l pl.UTF-8
Wtyczka wejściowa cdio (CD Audio) dla odtwarzacza cmus.

%package input-cue
Summary:	CUE input plugin for cmus
Summary(hu.UTF-8):	CUE plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa CUE dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-cue
CUE input plugin for cmus.

%description input-cue -l hu.UTF-8
CUE plugin cmus-hoz.

%description input-cue -l pl.UTF-8
Wtyczka wejściowa CUE dla odtwarzacza cmus.

%package input-ffmpeg
Summary:	FFmpeg input plugin for cmus
Summary(hu.UTF-8):	FFmpeg plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa FFmpeg dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-ffmpeg
FFmpeg input plugin for cmus.

%description input-ffmpeg -l hu.UTF-8
FFmpeg plugin cmus-hoz.

%description input-ffmpeg -l pl.UTF-8
Wtyczka wejściowa FFmpeg dla odtwarzacza cmus.

%package input-flac
Summary:	FLAC input plugin for cmus
Summary(hu.UTF-8):	FLAC plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa FLAC dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-flac
FLAC input plugin for cmus.

%description input-flac -l hu.UTF-8
FLAC plugin cmus-hoz.

%description input-flac -l pl.UTF-8
Wtyczka wejściowa FLAC dla odtwarzacza cmus.

%package input-mad
Summary:	mad (MP3) input plugin for cmus
Summary(hu.UTF-8):	mad (MP3) plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa mad (MP3) dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-mad
mad (MP3) input plugin for cmus.

%description input-mad -l hu.UTF-8
mad (MP3) plugin cmus-hoz.

%description input-mad -l pl.UTF-8
Wtyczka wejściowa mad (MP3) dla odtwarzacza cmus.

%package input-modplug
Summary:	modplug input plugin for cmus
Summary(hu.UTF-8):	modplug plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa modplug dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-modplug
modplug input plugin for cmus.

%description input-modplug -l hu.UTF-8
modplug plugin cmus-hoz.

%description input-modplug -l pl.UTF-8
Wtyczka wejściowa modplug dla odtwarzacza cmus.

%package input-mp4
Summary:	MP4 input plugin for cmus
Summary(hu.UTF-8):	MP4 plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa MP4 dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-mp4
MP4 input plugin for cmus.

%description input-mp4 -l hu.UTF-8
MP4 plugin cmus-hoz.

%description input-mp4 -l pl.UTF-8
Wtyczka wejściowa MP4 dla odtwarzacza cmus.

%package input-mpc
Summary:	MPC (Musepack) input plugin for cmus
Summary(hu.UTF-8):	MPC (Musepack) plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa MPC (Musepack) dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-mpc
MPC (Musepack) input plugin for cmus.

%description input-mpc -l hu.UTF-8
MPC (Musepack) plugin cmus-hoz.

%description input-mpc -l pl.UTF-8
Wtyczka wejściowa MPC (Musepack) dla odtwarzacza cmus.

%package input-opus
Summary:	Opus input plugin for cmus
Summary(hu.UTF-8):	Opus plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa Opus dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-opus
Opus input plugin for cmus.

%description input-opus -l hu.UTF-8
Opus plugin cmus-hoz.

%description input-opus -l pl.UTF-8
Wtyczka wejściowa Opus dla odtwarzacza cmus.

%package input-vorbis
Summary:	Vorbis input plugin for cmus
Summary(hu.UTF-8):	Vorbis plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa Vorbis dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-vorbis
Vorbis input plugin for cmus.

%description input-vorbis -l hu.UTF-8
Vorbis plugin cmus-hoz.

%description input-vorbis -l pl.UTF-8
Wtyczka wejściowa Vorbis dla odtwarzacza cmus.

%package input-wav
Summary:	WAV input plugin for cmus
Summary(hu.UTF-8):	WAV plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa WAV dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-wav
WAV input plugin for cmus.

%description input-wav -l hu.UTF-8
WAV plugin cmus-hoz.

%description input-wav -l pl.UTF-8
Wtyczka wejściowa WAV dla odtwarzacza cmus.

%package input-wavpack
Summary:	WavPack input plugin for cmus
Summary(hu.UTF-8):	WavPack plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wejściowa WavPack dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description input-wavpack
WavPack input plugin for cmus.

%description input-wavpack -l hu.UTF-8
WavPack plugin cmus-hoz.

%description input-wavpack -l pl.UTF-8
Wtyczka wejściowa WavPack dla odtwarzacza cmus.

# output plugins

%package output-alsa
Summary:	ALSA output plugin for cmus
Summary(hu.UTF-8):	ALSA plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa ALSA dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-output = %{version}-%{release}

%description output-alsa
ALSA output plugin for cmus.

%description output-alsa -l hu.UTF-8
ALSA plugin cmus-hoz.

%description output-alsa -l pl.UTF-8
Wtyczka wyjściowa ALSA dla odtwarzacza cmus.

%package output-arts
Summary:	aRts output plugin for cmus
Summary(hu.UTF-8):	aRts plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa aRts dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-output = %{version}-%{release}

%description output-arts
aRts output plugin for cmus.

%description output-arts -l hu.UTF-8
aRts plugin cmus-hoz.

%description output-arts -l pl.UTF-8
Wtyczka wyjściowa aRts dla odtwarzacza cmus.

%package output-jack
Summary:	JACK output plugin for cmus
Summary(hu.UTF-8):	JACK plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa JACK dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-output = %{version}-%{release}

%description output-jack
JACK output plugin for cmus.

%description output-jack -l hu.UTF-8
JACK plugin cmus-hoz.

%description output-jack -l pl.UTF-8
Wtyczka wyjściowa JACK dla odtwarzacza cmus.

%package output-libao
Summary:	libao output plugin for cmus
Summary(hu.UTF-8):	libao plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa libao dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-output = %{version}-%{release}

%description output-libao
libao output plugin for cmus.

%description output-libao -l hu.UTF-8
libao plugin cmus-hoz.

%description output-libao -l pl.UTF-8
Wtyczka wyjściowa libao dla odtwarzacza cmus.

%package output-oss
Summary:	OSS output plugin for cmus
Summary(hu.UTF-8):	OSS plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa OSS dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-output = %{version}-%{release}

%description output-oss
OSS output plugin for cmus.

%description output-oss -l hu.UTF-8
OSS plugin cmus-hoz.

%description output-oss -l pl.UTF-8
Wtyczka wyjściowa OSS dla odtwarzacza cmus.

%package output-pulse
Summary:	PulseAudio output plugin for cmus
Summary(hu.UTF-8):	PulseAudio plugin cmus-hoz
Summary(pl.UTF-8):	Wtyczka wyjściowa PulseAudio dla odtwarzacza cmus
Group:		Applications/Sound
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-output = %{version}-%{release}

%description output-pulse
PulseAudio output plugin for cmus.

%description output-pulse -l hu.UTF-8
PulseAudio plugin cmus-hoz.

%description output-pulse -l pl.UTF-8
Wtyczka wyjściowa PulseAudio dla odtwarzacza cmus.

%prep
%setup -q

%{__sed} -i "s|<curses.h>|<ncursesw/ncurses.h>|" options.c ui_curses.c

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
%doc AUTHORS README.md
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

%files input-opus
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/opus.so

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

%files output-jack
%defattr(644,root,root,755)
%{_libdir}/cmus/op/jack.so

%files output-oss
%defattr(644,root,root,755)
%{_libdir}/cmus/op/oss.so

%files output-pulse
%defattr(644,root,root,755)
%{_libdir}/cmus/op/pulse.so
