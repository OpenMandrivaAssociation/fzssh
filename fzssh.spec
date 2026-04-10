
Summary:	fzssh is a SSH/SFTP library based on libfilezilla
Name:		fzssh
Version:	1.1.7
Release:	1
Group:		Networking/File transfer
License:	AGPL3
Url:		https://filezilla-project.org/
Source0:	https://dl1.cdn.filezilla-project.org/fzssh/fzssh-%{version}.tar.xz

BuildRequires:  pkgconfig(gmp)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:  pkgconfig(nettle)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libfilezilla)
BuildRequires:  pkgconfig(libargon2)

%description
The client-side fzzsh library, comprised of the libfzzsh, libfzssh-crypt,
and libfzssh-client compopnents, and their build scripts and tests, is
free software: You can redistribute it and/or modify it under the terms of
the GNU Affero General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version, see the accompanying agpl3.txt for the full terms.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
