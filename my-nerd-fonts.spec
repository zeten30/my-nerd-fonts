Name:           my-nerd-fonts
Version:        2024.1
Release:        1%{?dist}
Summary:        Selection of NerdFonts patched fonts

License:        MIT License
URL:            https://github.com/ryanoasis/nerd-fonts/releases/
Source0:        my-nerd-fonts.tgz

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Nerd Fonts patches developer targeted fonts with a high number of glyphs (icons).
Specifically to add a high number of extra glyphs from popular 'iconic fonts' such as Font Awesome, Devicons, Octicons, and others.


%prep
%setup -q -n my-nerd-fonts


%build
# Nothing to build

%install
%{__install} -d -m755 %{buildroot}%{_datadir}/fonts/nerd/
%{__cp} -pr ./* %{buildroot}%{_datadir}/fonts/nerd/


%files
%defattr(-,root,root)
%{_datadir}/fonts/nerd/


%post
/usr/bin/fc-cache %{_datadir}/fonts/nerd/


%changelog
* Wed Jan 3 2024 Milan Zink <zeten30@gmail.com> - 2024.01.1
- latest upstream sync

* Tue Sep 7 2021 Milan Zink <zeten30@gmail.com> - 2023.06.1
- removed RobotoMono font
- latest upstream sync

* Tue Sep 7 2021 Milan Zink <zeten30@gmail.com> - 2021.09.3
- removed Lekton font

* Wed Apr 28 2021 Milan Zink <zeten30@gmail.com> - 2021.04.1
- added Lekton font

* Fri Mar 13 2020 Milan Zink <zeten30@gmail.com> - 2020.10.2
- removed unused fonts

* Fri Mar 13 2020 Milan Zink <zeten30@gmail.com> - 2020.03.1
- 2.1 upstream release

* Wed Oct 23 2019 Milan Zink <zeten30@gmail.com> - 2019.10.1
- added Terminus font

* Fri Feb 15 2019 Milan Zink <zeten30@gmail.com> - 2019.08.1
- initial release
