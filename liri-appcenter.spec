%define major 0
%define libsoftware %mklibname liriSoftware %{major}
%define libvibesettings %mklibname VibeSettings %{major}
%define devname %mklibname -d VibeCore

Summary:        A collection of core classes used throughout Liri
Name:           liri-appcenter
Version:        0.1.0
Release:        1
License:        LGPLv3
Url:            https://github.com/lirios/
source0:	https://github.com/lirios/appcenter/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  cmake(Vibe)
BuildRequires:  qt5-devel
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickTest)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(qt5xdg)
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(flatpak)

%description
A collection of core classes used throughout Liri

%package -n     %{libsoftware}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libsoftware}
Library for %{name}

%package -n     %{devname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libsoftware} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{devname}
A collection of core classes used throughout Liri
Development files

%prep
%setup -q
%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/liri-appcenter
%{_bindir}/liri-update-notifier
%{_libdir}/qml/Liri/Software/*.so
%{_datadir}/applications/io.liri.AppCenter.desktop
%{_datadir}/appdata/io.liri.AppCenter.appdata.xml
%{_libdir}/qml/Liri/Software/qmldir

%files -n %{libsoftware}
%{_libdir}/libLiriSoftware.so.%{major}*

%files -n %{devname}
%{_libdir}/libLiriSoftware.so
%{_includedir}/Liri/software/*.h
%{_libdir}/cmake/Liri/*.cmake
%{_includedir}/Liri/Software/
