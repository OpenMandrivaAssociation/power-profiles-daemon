Summary:	Makes power profiles handling available over D-Bus
Name:		power-profiles-daemon
Version:	0.21
Release:	1
Group:		System/Tools
License:	GPLv3+
URL:		https://gitlab.freedesktop.org/upower/power-profiles-daemon
Source0:	https://gitlab.freedesktop.org/upower/power-profiles-daemon/-/archive/%{version}/power-profiles-daemon-%{version}.tar.bz2
BuildRequires:	meson
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	systemd
BuildRequires:	umockdev
BuildRequires:	python%{pyver}dist(python-dbusmock)
BuildRequires:	python%{pyver}dist(argparse-manpage)
BuildRequires:	python%{pyver}dist(shtab)
BuildRequires:	systemd-rpm-macros

%description
%{summary}.

%package docs
Summary:	Documentation for %{name}
BuildArch:	noarch

%description docs
This package contains the documentation for %{name}.

%prep
%autosetup -p1

%build
%meson -Dgtk_doc=false
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_localstatedir}/lib/power-profiles-daemon

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/powerprofilesctl
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_datadir}/bash-completion/completions/powerprofilesctl
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf
%{_datadir}/polkit-1/actions/power-profiles-daemon.policy
%{_localstatedir}/lib/power-profiles-daemon
%{_mandir}/man1/powerprofilesctl.1*
