Summary:	Generic USB CCID (Chip/Smart Card Interface Devices) driver
Summary(pl):	Ogólny sterownik USB CCID (Chip/Smart Card Interface Devices)
Name:		pcsc-driver-ccid
Version:	0.9.2
Release:	1
License:	GPL
Group:		Libraries
#Source0Download: http://alioth.debian.org/project/showfiles.php?group_id=1225
Source0:	http://alioth.debian.org/download.php/755/ccid-%{version}.tar.gz
# Source0-md5:	9fe31ed0d51951507e8360cc43aac4f1
URL:		http://pcsclite.alioth.debian.org/ccid.html
BuildRequires:	libusb-devel >= 0.1.7
BuildRequires:	pcsc-lite-devel >= 1.2.9-0.beta5
Requires:	pcsc-lite >= 1.2.9-0.beta3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		usbdropdir	/usr/%{_lib}/pcsc/drivers
%define		ccidtwindir	/usr/%{_lib}/pcsc/drivers

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver. Supported CCID readers:
- Gemplus: GemPC 433 SL, GemPC Key, GemPC Twin
- C3PO LTC31
- OmniKey CardMan 3121
- SCM Micro: SCR 331, SCR 335, SCR 331-DI, SPR 532
- ActivCard USB reader 2.0
- Silitek SK-3105 keyboard

%description -l pl
Ten pakiet zawiera ogólny sterownik USB CCID (Chip/Smart Card
Interface Devices). Obs³ugiwane czytniki CCID:
- Gemplus: GemPC 433 SL, GemPC Key, GemPC Twin
- C3PO LTC31
- OmniKey CardMan 3121
- SCM Micro: SCR 331, SCR 335, SCR 331-DI, SPR 532
- ActivCard USB reader 2.0
- klawiatura Silitek SK-3105

%package serial
Summary:	Generic USB CCID driver for readers connected to serial port
Summary(pl):	Ogólny sterownik USB CCID dla czytników pod³±czonych przez port szeregowy
Group:		Libraries
Requires:	pcsc-lite >= 1.2.9-0.beta3

%description serial
Generic USB CCID driver for readers connected to serial port.
Supported CCID readers:
- Gemplus GemPC Twin

%description serial -l pl
Ogólny sterownik USB CCID dla czytników pod³±czonych przez port
szeregowy. Obs³ugiwane czytniki CCID:
- Gemplus GemPC Twin

%prep
%setup -q -n ccid-%{version}

%build
%configure \
	--enable-usbdropdir=%{usbdropdir} \
	--enable-ccidtwindir=%{ccidtwindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C src install_ccidtwin \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/reader.conf .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README readers/*.txt
%dir %{usbdropdir}/ifd-ccid.bundle
%dir %{usbdropdir}/ifd-ccid.bundle/Contents
%{usbdropdir}/ifd-ccid.bundle/Contents/Info.plist
%dir %{usbdropdir}/ifd-ccid.bundle/Contents/Linux
%attr(755,root,root) %{usbdropdir}/ifd-ccid.bundle/Contents/Linux/libccid.so.*.*.*

%files serial
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README readers/GemPCTwin.txt readers/supported_readers.txt reader.conf
%attr(755,root,root) %{ccidtwindir}/libccidtwin.so.*
