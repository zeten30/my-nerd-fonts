Name:           my-nerd-fonts
Version:        2019.10
Release:        1%{?dist}
Summary:        Selection of NerdFonts patched fonts

License:        MIT License
URL:            https://github.com/ryanoasis/nerd-fonts/releases/download/v2.0.0/*.zip
Source0:        my-nerd-fonts.tgz

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Nerd Fonts patches developer targeted fonts with a high number of glyphs (icons). 
Specifically to add a high number of extra glyphs from popular ‘iconic fonts’ such as Font Awesome, Devicons, Octicons, and others.


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
* Wed Oct 23 2019 Milan Zink <zeten30@gmail.com> - 2019.10.1
- added Terminus font

* Fri Feb 15 2019 Milan Zink <zeten30@gmail.com> - 2019.08.1
- initial release
