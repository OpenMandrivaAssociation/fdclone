%define version  2.08
%define release  %mkrel 3
%define src_name FD

Name:           fdclone
Version:        %{version}
Release:        %{release}
Summary:        FD-clone file manager
Group:          File tools
License:        BSD-like
URL:            http://hp.vector.co.jp/authors/VA012337/soft/fd/
Source:         %{src_name}-%{version}.tar.bz2
Patch0:         fd-clone_change_config.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:	ncurses-devel

%description
FD-clone file manager.
FD is a famous file manager for MS-DOS.


%prep
%setup -q -n %{src_name}-%{version}
%patch0 -p0

%build
%make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_sysconfdir}/
install -d $RPM_BUILD_ROOT/%{_bindir}/

install -m 644 _fdrc        $RPM_BUILD_ROOT/%{_sysconfdir}/fd2rc
install -m 755 fd           $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 fd-unicd.tbl $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc FAQ FAQ.eng HISTORY HISTORY.eng LICENSES LICENSES.eng
%doc README README.eng TECHKNOW TECHKNOW.eng ToAdmin ToAdmin.eng
%config(noreplace) %{_sysconfdir}/fd2rc
%{_bindir}/fd*


