%define build 3126

Name:          sublime-text
Version:       3.0.%{build}
Release:       1%{?dist}
Summary:       A Sophisticated Text Editor
Group:         Applications/Editors
License:       Proprietary
URL:           http://www.sublimetext.com/
Source0:       https://download.sublimetext.com/sublime_text_3_build_%{build}_x64.tar.bz2
ExclusiveArch: x86_64

BuildRequires: desktop-file-utils

%description
Sublime Text is a very extensible and customizable editor. It does many things out of the box, but if you spend some time tailoring it to your exact needs, it will give you superpowers.


%prep
%setup -n sublime_text_3


%install
mkdir -p %{buildroot}/usr/local/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications

cp ./Icon/48x48/sublime-text.png %{buildroot}%{_datadir}/pixmaps/

desktop-file-install                          \
--add-category="Office"                       \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
./sublime_text.desktop

sed -e "s@/opt/sublime_text/sublime_text@/usr/local/%{name}/sublime_text@g" -i %{buildroot}%{_datadir}/applications/sublime_text.desktop

cp -afr ./* %{buildroot}/usr/local/%{name}

cat >sublime-text <<EOF
#!/usr/bin/sh
/usr/local/%{name}/sublime_text \$@ &

EOF

mv ./sublime-text %{buildroot}%{_bindir}/


%files
/usr/local/%{name}
%attr(755, root, root) %{_bindir}/sublime-text
%{_datadir}/pixmaps/sublime-text.png
%{_datadir}/applications/sublime_text.desktop

%changelog
* Wed Feb 22 2017 Tomas Tomecek <ttomecek@redhat.com> - 3.0.3126-1
- 3126 build

* Sun Jun 07 2015 Tomas Tomecek <ttomecek@redhat.com> - 3.0.3083-2
- 3083 build

* Wed Jan 15 2014 Tomas Tomecek <ttomecek@redhat.com> - 3.0.3059-1
- initial release
