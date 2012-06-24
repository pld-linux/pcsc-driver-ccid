Summary:	Generic USB CCID (Chip/Smart Card Interface Devices) driver
Summary(pl):	Og�lny sterownik USB CCID (Chip/Smart Card Interface Devices)
Name:		pcsc-driver-ccid
Version:	0.9.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://alioth.debian.org/project/showfiles.php?group_id=30105
Source0:	http://alioth.debian.org/download.php/1291/ccid-%{version}.tar.gz
# Source0-md5:	9c73165ceb105b648847bc6ded747209
URL:		http://pcsclite.alioth.debian.org/ccid.html
BuildRequires:	libusb-devel >= 0.1.7
BuildRequires:	pcsc-lite-devel >= 1.2.9-0.beta9
Requires:	pcsc-lite >= 1.2.9-0.beta9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		usbdropdir	/usr/%{_lib}/pcsc/drivers
%define		ccidtwindir	/usr/%{_lib}/pcsc/drivers

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver. Supported CCID readers:
- ActivCard USB reader 2.0
- Advanced Card Systems ACR 38
- C3PO: LTC31, TLTC2USB
- Cherry: XX33, XX44, SmartTerminal ST2XX, ST-1044U
- Dell: SK-3106 keyboard
- Eutron: SIM Pocket Combo, CryptoIdentity
- Gemplus: GemPC 433 SL, GemPC Key, GemPC Twin
- Kobil: KAAN Base, KAAN Advanced, KAAN SIM III, mIDentity
- OmniKey CardMan 3121
- SCM Micro: SCR 331, SCR 331-DI, SCR 333, SCR 335, SCR 3310, SPR 532
- Silitek SK-3105 keyboard
- Verisign: Secure Storage Token, Secure Token

%description -l pl
Ten pakiet zawiera og�lny sterownik USB CCID (Chip/Smart Card
Interface Devices). Obs�ugiwane czytniki CCID:
- ActivCard USB reader 2.0
- Advanced Card Systems ACR 38
- C3PO: LTC32, TLTC2USB
- Cherry: XX33, XX44, SmartTerminal ST2XX, ST-1044U
- Dell: klawiatura SK-3106
- Eutron: SIM Pocket Combo, CryptoIdentity
- Gemplus: GemPC 433 SL, GemPC Key, GemPC Twin
- Kobil: KAAN Base, KAAN Advanced, KAAN SIM III, mIDentity
- OmniKey CardMan 3121
- SCM Micro: SCR 331, SCR 331-DI, SCR 333, SCR 335, SCR 3310, SPR 532
- Silitek: klawiatura SK-3105
- Verisign: Secure Storage Token, Secure Token

%package serial
Summary:	Generic USB CCID driver for readers connected to serial port
Summary(pl):	Og�lny sterownik USB CCID dla czytnik�w pod��czonych przez port szeregowy
Group:		Libraries
Requires:	pcsc-lite >= 1.2.9-0.beta9

%description serial
Generic USB CCID driver for readers connected to serial port.
Supported CCID readers:
- Gemplus GemPC Twin

%description serial -l pl
Og�lny sterownik USB CCID dla czytnik�w pod��czonych przez port
szeregowy. Obs�ugiwane czytniki CCID:
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
