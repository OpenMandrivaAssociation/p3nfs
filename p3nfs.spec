%define name    p3nfs
%define version 5.19
%define release %mkrel 4

%define summary Utility to access Symbian based (Psion/Nokia/Sony-Ericsson/etc) mobile devices

Summary:	%{summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		http://www.koeniglich.de/p3nfs.html
Source0:	%{name}-%{version}.tar.bz2
Patch0:		p3nfs_no_client.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
p3nfs is a Symbian (Psion/Nokia/Sony-Ericsson/etc) to UNIX/Linux 
communication program. It allows you to mount the file systems of the 
phone/PDA on your UNIX machine. This means that you see all the 
filesystems of the Phone/PDA as a filesystem on your UNIX machine, 
and you can copy/backup/edit any file on the Phone/PDA with your 
preferred tools on the UNIX machine.

In order to operate correctly, you need to install a p3nfs client
on the mobile device. Client applications for the various 
supported mobile devices can be found in %{_docdir}/%{name}-%{version}.

%prep
%setup -q
%patch0

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall DESTDIR=${RPM_BUILD_ROOT}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}{-%{version},}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%doc doc/*
%{_bindir}/*
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 5.19-4mdv2010.0
+ Revision: 430227
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 5.19-3mdv2009.0
+ Revision: 254947
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 5.19-1mdv2008.1
+ Revision: 134699
- fix build
- kill re-definition of %%buildroot on Pixel's request
- import p3nfs


* Sat Dec 18 2005 Udo Rader <udo.rader@bestsolution.at> 5.19-1mdk
- initial release on Mandriva
