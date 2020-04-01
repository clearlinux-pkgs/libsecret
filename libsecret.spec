#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsecret
Version  : 0.20.2
Release  : 19
URL      : https://download.gnome.org/sources/libsecret/0.20/libsecret-0.20.2.tar.xz
Source0  : https://download.gnome.org/sources/libsecret/0.20/libsecret-0.20.2.tar.xz
Summary  : GObject bindings for Secret Service API
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.1
Requires: libsecret-bin = %{version}-%{release}
Requires: libsecret-data = %{version}-%{release}
Requires: libsecret-lib = %{version}-%{release}
Requires: libsecret-license = %{version}-%{release}
Requires: libsecret-locales = %{version}-%{release}
Requires: libsecret-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gjs
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pygobject
BuildRequires : python3
BuildRequires : vala-dev

%description


%package bin
Summary: bin components for the libsecret package.
Group: Binaries
Requires: libsecret-data = %{version}-%{release}
Requires: libsecret-license = %{version}-%{release}

%description bin
bin components for the libsecret package.


%package data
Summary: data components for the libsecret package.
Group: Data

%description data
data components for the libsecret package.


%package dev
Summary: dev components for the libsecret package.
Group: Development
Requires: libsecret-lib = %{version}-%{release}
Requires: libsecret-bin = %{version}-%{release}
Requires: libsecret-data = %{version}-%{release}
Provides: libsecret-devel = %{version}-%{release}
Requires: libsecret = %{version}-%{release}

%description dev
dev components for the libsecret package.


%package doc
Summary: doc components for the libsecret package.
Group: Documentation
Requires: libsecret-man = %{version}-%{release}

%description doc
doc components for the libsecret package.


%package lib
Summary: lib components for the libsecret package.
Group: Libraries
Requires: libsecret-data = %{version}-%{release}
Requires: libsecret-license = %{version}-%{release}

%description lib
lib components for the libsecret package.


%package license
Summary: license components for the libsecret package.
Group: Default

%description license
license components for the libsecret package.


%package locales
Summary: locales components for the libsecret package.
Group: Default

%description locales
locales components for the libsecret package.


%package man
Summary: man components for the libsecret package.
Group: Default

%description man
man components for the libsecret package.


%prep
%setup -q -n libsecret-0.20.2
cd %{_builddir}/libsecret-0.20.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585773692
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1585773692
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libsecret
cp %{_builddir}/libsecret-0.20.2/COPYING %{buildroot}/usr/share/package-licenses/libsecret/7c7d178d9ce31b21a4869940a881b043b086f007
cp %{_builddir}/libsecret-0.20.2/COPYING.TESTS %{buildroot}/usr/share/package-licenses/libsecret/22e01c37d5bbe7f728acd042bb9d6972081bfb48
%make_install
%find_lang libsecret

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/secret-tool

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Secret-1.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libsecret-1.deps
/usr/share/vala/vapi/libsecret-1.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libsecret-1/libsecret/secret-attributes.h
/usr/include/libsecret-1/libsecret/secret-backend.h
/usr/include/libsecret-1/libsecret/secret-collection.h
/usr/include/libsecret-1/libsecret/secret-enum-types.h
/usr/include/libsecret-1/libsecret/secret-item.h
/usr/include/libsecret-1/libsecret/secret-password.h
/usr/include/libsecret-1/libsecret/secret-paths.h
/usr/include/libsecret-1/libsecret/secret-prompt.h
/usr/include/libsecret-1/libsecret/secret-retrievable.h
/usr/include/libsecret-1/libsecret/secret-schema.h
/usr/include/libsecret-1/libsecret/secret-schemas.h
/usr/include/libsecret-1/libsecret/secret-service.h
/usr/include/libsecret-1/libsecret/secret-types.h
/usr/include/libsecret-1/libsecret/secret-value.h
/usr/include/libsecret-1/libsecret/secret-version.h
/usr/include/libsecret-1/libsecret/secret.h
/usr/lib64/libsecret-1.so
/usr/lib64/pkgconfig/libsecret-1.pc
/usr/lib64/pkgconfig/libsecret-unstable.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libsecret-1/SecretCollection.html
/usr/share/gtk-doc/html/libsecret-1/SecretItem.html
/usr/share/gtk-doc/html/libsecret-1/SecretPrompt.html
/usr/share/gtk-doc/html/libsecret-1/SecretRetrievable.html
/usr/share/gtk-doc/html/libsecret-1/SecretService.html
/usr/share/gtk-doc/html/libsecret-1/SecretValue.html
/usr/share/gtk-doc/html/libsecret-1/annotation-glossary.html
/usr/share/gtk-doc/html/libsecret-1/c-examples.html
/usr/share/gtk-doc/html/libsecret-1/c-lookup-example.html
/usr/share/gtk-doc/html/libsecret-1/c-remove-example.html
/usr/share/gtk-doc/html/libsecret-1/c-store-example.html
/usr/share/gtk-doc/html/libsecret-1/complete.html
/usr/share/gtk-doc/html/libsecret-1/examples.html
/usr/share/gtk-doc/html/libsecret-1/home.png
/usr/share/gtk-doc/html/libsecret-1/index.html
/usr/share/gtk-doc/html/libsecret-1/js-examples.html
/usr/share/gtk-doc/html/libsecret-1/js-lookup-example.html
/usr/share/gtk-doc/html/libsecret-1/js-remove-example.html
/usr/share/gtk-doc/html/libsecret-1/js-store-example.html
/usr/share/gtk-doc/html/libsecret-1/left-insensitive.png
/usr/share/gtk-doc/html/libsecret-1/left.png
/usr/share/gtk-doc/html/libsecret-1/libsecret-1.devhelp2
/usr/share/gtk-doc/html/libsecret-1/libsecret-DBus-Path-Related-Functions.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-Password-storage.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-Secret-Attributes.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-SecretError.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-SecretSchema.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-Version-Information.html
/usr/share/gtk-doc/html/libsecret-1/migrating-api.html
/usr/share/gtk-doc/html/libsecret-1/migrating-introduction.html
/usr/share/gtk-doc/html/libsecret-1/migrating-items.html
/usr/share/gtk-doc/html/libsecret-1/migrating-keyrings.html
/usr/share/gtk-doc/html/libsecret-1/migrating-locking.html
/usr/share/gtk-doc/html/libsecret-1/migrating-memory.html
/usr/share/gtk-doc/html/libsecret-1/migrating-misc.html
/usr/share/gtk-doc/html/libsecret-1/migrating-removing.html
/usr/share/gtk-doc/html/libsecret-1/migrating-schemas.html
/usr/share/gtk-doc/html/libsecret-1/migrating-searching.html
/usr/share/gtk-doc/html/libsecret-1/migrating-storing.html
/usr/share/gtk-doc/html/libsecret-1/migrating.html
/usr/share/gtk-doc/html/libsecret-1/py-examples.html
/usr/share/gtk-doc/html/libsecret-1/py-lookup-example.html
/usr/share/gtk-doc/html/libsecret-1/py-remove-example.html
/usr/share/gtk-doc/html/libsecret-1/py-store-example.html
/usr/share/gtk-doc/html/libsecret-1/right-insensitive.png
/usr/share/gtk-doc/html/libsecret-1/right.png
/usr/share/gtk-doc/html/libsecret-1/simple.html
/usr/share/gtk-doc/html/libsecret-1/style.css
/usr/share/gtk-doc/html/libsecret-1/up-insensitive.png
/usr/share/gtk-doc/html/libsecret-1/up.png
/usr/share/gtk-doc/html/libsecret-1/using-c.html
/usr/share/gtk-doc/html/libsecret-1/using-js.html
/usr/share/gtk-doc/html/libsecret-1/using-python.html
/usr/share/gtk-doc/html/libsecret-1/using-vala.html
/usr/share/gtk-doc/html/libsecret-1/using.html
/usr/share/gtk-doc/html/libsecret-1/vala-examples.html
/usr/share/gtk-doc/html/libsecret-1/vala-lookup-example.html
/usr/share/gtk-doc/html/libsecret-1/vala-remove-example.html
/usr/share/gtk-doc/html/libsecret-1/vala-store-example.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsecret-1.so.0
/usr/lib64/libsecret-1.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsecret/22e01c37d5bbe7f728acd042bb9d6972081bfb48
/usr/share/package-licenses/libsecret/7c7d178d9ce31b21a4869940a881b043b086f007

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/secret-tool.1

%files locales -f libsecret.lang
%defattr(-,root,root,-)

