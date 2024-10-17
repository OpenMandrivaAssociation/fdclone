%define debug_package %{nil}
%define version  2.08
%define release  3
%define src_name FD

Name:           fdclone
Version:        %{version}
Release:        %{release}
Summary:        FD-clone file manager
Group:          File tools
License:        BSD-like
URL:            https://hp.vector.co.jp/authors/VA012337/soft/fd/
Source:         %{src_name}-%{version}.tar.bz2
Patch0:         fd-clone_change_config.diff.bz2
BuildRequires:	pkgconfig(ncurses)

%description
FD-clone file manager.
FD is a famous file manager for MS-DOS.


%prep
%setup -q -n %{src_name}-%{version}
%patch0 -p0

%build
%make

%install
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/
install -d $RPM_BUILD_ROOT/%{_bindir}/

install -m 644 _fdrc        $RPM_BUILD_ROOT/%{_sysconfdir}/fd2rc
install -m 755 fd           $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 fd-unicd.tbl $RPM_BUILD_ROOT/%{_bindir}/


%files
%doc FAQ FAQ.eng HISTORY HISTORY.eng LICENSES LICENSES.eng
%doc README README.eng TECHKNOW TECHKNOW.eng ToAdmin ToAdmin.eng
%config(noreplace) %{_sysconfdir}/fd2rc
%{_bindir}/fd*


%changelog
* Mon Feb 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.08-3mdv2007.0
+ Revision: 122780
- rebuild in order to get the same extension on x86_64
- Import fdclone




* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.08-2mdk
- fix buildrequires

* Tue Jan 17 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 2.08-1mdk
- first spec for Mandriva Linux
- NOTE: run this program in UTF-8 please.
- config file was modified by taka-chan. thanks!
- (http://wiki.fedora.jp/?App%2Ffdclone2)
