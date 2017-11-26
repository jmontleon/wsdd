Name:		wsdd
Version:	1.0.0
Release:	1%{?dist}
Summary:	WS-Discovery daemon for Linux

License:        GPL	
Url:            https://raw.githubusercontent.com/tobiaswaldvogel/openwrt-addpack/master/wsdd/src/wsdd.c
Source0:        wsdd.c	
Source1:        wsdd
Source2:        wsdd.service

BuildRequires:	libuuid-devel

%description
%{summary}

%prep

%build
gcc -luuid %{SOURCE0} -o %{name}

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0755 %{name} %{buildroot}%{_bindir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_bindir}/%{name}
%config(noreplace)%{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service

%changelog

