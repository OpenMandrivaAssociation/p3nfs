Summary:	Utility to access Symbian based (Psion/Nokia/Sony-Ericsson/etc) mobile devices
Name:		p3nfs
Version:	5.19
Release:	5
License:	GPLv2+
Group:		Networking/Other
Url:		http://www.koeniglich.de/p3nfs.html
Source0:	%{name}-%{version}.tar.bz2
Patch0:		p3nfs_no_client.patch.bz2

%description
p3nfs is a Symbian (Psion/Nokia/Sony-Ericsson/etc) to UNIX/Linux
communication program. It allows you to mount the file systems of the
phone/PDA on your UNIX machine. This means that you see all the
filesystems of the Phone/PDA as a filesystem on your UNIX machine,
and you can copy/backup/edit any file on the Phone/PDA with your
preferred tools on the UNIX machine.

In order to operate correctly, you need to install a p3nfs client
on the mobile device.

%files
%doc README
%doc doc/*
%{_bindir}/*
%{_mandir}/*/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0

%build
%configure2_5x
%make CFLAGS="%{optflags} -I."

%install
%makeinstall_std

rm -rf %{buildroot}%{_defaultdocdir}/%{name}-%{version}

