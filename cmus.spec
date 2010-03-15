Summary:	cmus is a small and fast text mode music player
Summary(hu.UTF-8):	cmus egy kicsi és gyors szöveges zenelejátszó
Name:		cmus
Version:	2.3.1
Release:	0.2
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/project/cmus/%{name}-v%{version}.tar.bz2
# Source0-md5:	1b77942c61dd7ddb63d4daf2a42ae58d
URL:		http://cmus.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libao-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mpeg4ip-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkg-config
BuildRequires:	sed > 4.0
BuildRequires:	wavpack-devel
Suggests:	%{name}-input
Suggests:	%{name}-output
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cmus is a small and fast text mode music player

%description -l pl.UTF-8
cmus egy kicsi és gyors szöveges zenelejátszó


# input plugins

%package input-aac
Summary:	aac plugin for cmus
Summary(hu.UTF-8):	aac plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-aac
aac plugin for cmus

%description input-aac -l hu.UTF-8
aac plugin cmus-hoz

%package input-ffmpeg
Summary:	ffmpeg plugin for cmus
Summary(hu.UTF-8):	ffmpeg plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-ffmpeg
ffmpeg plugin for cmus

%description input-ffmpeg -l hu.UTF-8
ffmpeg plugin cmus-hoz

%package input-flac
Summary:	flac plugin for cmus
Summary(hu.UTF-8):	flac plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-flac
flac plugin for cmus

%description input-flac -l hu.UTF-8
flac plugin cmus-hoz

%package input-mad
Summary:	mad plugin for cmus
Summary(hu.UTF-8):	mad plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-mad
mad plugin for cmus

%description input-mad -l hu.UTF-8
mad plugin cmus-hoz

%package input-modplug
Summary:	modplug plugin for cmus
Summary(hu.UTF-8):	modplug plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-modplug
modplug plugin for cmus

%description input-modplug -l hu.UTF-8
modplug plugin cmus-hoz

%package input-mp4
Summary:	mp4 plugin for cmus
Summary(hu.UTF-8):	mp4 plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-mp4
mp4 plugin for cmus

%description input-mp4 -l hu.UTF-8
mp4 plugin cmus-hoz

%package input-vorbis
Summary:	vorbis plugin for cmus
Summary(hu.UTF-8):	vorbis plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-vorbis
vorbis plugin for cmus

%description input-vorbis -l hu.UTF-8
vorbis plugin cmus-hoz

%package input-wav
Summary:	wav plugin for cmus
Summary(hu.UTF-8):	wav plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-wav
wav plugin for cmus

%description input-wav -l hu.UTF-8
wav plugin cmus-hoz

%package input-wavpack
Summary:	wavpack plugin for cmus
Summary(hu.UTF-8):	wavpack plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-input

%description input-wavpack
wavpack plugin for cmus

%description input-wavpack -l hu.UTF-8
wavpack plugin cmus-hoz


# output plugins

%package output-alsa
Summary:	alsa plugin for cmus
Summary(hu.UTF-8):	alsa plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-output

%description output-alsa
alsa plugin for cmus

%description output-alsa -l hu.UTF-8
alsa plugin cmus-hoz

%package output-arts
Summary:	arts plugin for cmus
Summary(hu.UTF-8):	arts plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-output

%description output-arts
arts plugin for cmus

%description output-arts -l hu.UTF-8
arts plugin cmus-hoz

%package output-libao
Summary:	libao plugin for cmus
Summary(hu.UTF-8):	libao plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-output

%description output-libao
libao plugin for cmus

%description output-libao -l hu.UTF-8
libao plugin cmus-hoz

%package output-oss
Summary:	oss plugin for cmus
Summary(hu.UTF-8):	oss plugin cmus-hoz
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	%{name}-output

%description output-oss
oss plugin for cmus

%description output-oss -l hu.UTF-8
oss plugin cmus-hoz

%prep
%setup -q -n %{name}-v%{version}
%{__sed} -i "s|<curses.h>|<ncursesw/ncurses.h>|" command_mode.c keys.c options.c search_mode.c ui_curses.c
%{__sed} -r -i "s|<ffmpeg/(.*).h|<lib\1/\1.h|" ffmpeg.c

%build

./configure prefix=%{_prefix} \
	libdir=%{_libdir} \
	mandir=%{_mandir} \
	bindir=%{_bindir} \
	datadir=%{_datadir}/%{name} \
	exampledir=%{_examplesdir}/%{name}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install cmus-status-display $RPM_BUILD_ROOT%{_datadir}/cmus

# mv $RPM_BUILD_ROOT%{_docdir}/cmus/* $RPM_BUILD_ROOT%{_docdir}/cmus-%{version}
# rmdir $RPM_BUILD_ROOT%{_docdir}/cmus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%dir %{_libdir}/cmus/op
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/cmus*
%{_mandir}/man7/cmus*

# input plugins
%files input-aac
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/aac.so

%files input-ffmpeg
%defattr(644,root,root,755)
%{_libdir}/cmus/ip/ffmpeg.so

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

%files output-arts
%defattr(644,root,root,755)
%{_libdir}/cmus/op/arts.so

%files output-oss
%defattr(644,root,root,755)
%{_libdir}/cmus/op/oss.so
